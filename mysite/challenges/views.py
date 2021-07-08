from bs4 import BeautifulSoup
import os
from django.shortcuts import render
from django.views import generic
from django.views import View
from django.conf import settings
from ajax_datatable.views import AjaxDatatableView

from .models import Challenge, Solution

class ChallengesListView(generic.list.ListView):
    model = Challenge


class ChallengeDetailView(generic.detail.DetailView):
    model = Challenge

def sync_db(request):
    syncer = SyncChallenge()
    syncer.sync()
    return render(request,'challenges/sync_status.html', 
        {'errors':syncer.filesnotfound,'success': syncer.filessynced}) #('<br>'.join(syncer.filesnotfound))


class SyncChallenge:
    def __init__(self):
        self.folder = os.path.join(settings.BASE_DIR, '..','htmlfiles')
        self.filesnotfound = []
        self.filessynced = []

    def sync(self):
        for lang in ['Cplusplus','C#','Java','JavaScript','PHP','Python','Ruby','Swift']:
            fn = f'languages/challenges_{lang.lower()}.html'
            if os.path.exists(f'{self.folder}/{fn}'):
                self.parse_challenge_list(fn)

        for challenge in Challenge.objects.all():
            self.parse_challenge(challenge)

    def parse_challenge_list(self, fn):
        soup = self.get_soup(fn)
        challenges_list=[]
        for challenge in soup('a'):
            challenge_url = challenge.get('href')
            if challenge_url and 'challenge' in challenge_url:
                challenge_data = {
                    'c_id':challenge_url.replace('/challenge/',''),
                    'lang': fn.split('_')[1].split('.')[0]
                } # c_id,lang,title,url,desc,tags,difficulty
                if Challenge.objects.filter(c_id=challenge_data['c_id']): continue

                items = challenge.find_all(['div','h3'])
                for i,txt in enumerate(items):
                    if i==0: challenge_data['title'] = txt.string
                    if i==1: challenge_data['desc'] = txt.string
                    if i==2: challenge_data['tags'] = ','.join([t.contents[1] for t in txt('div')])
                    if i==len(items)-1: challenge_data['difficulty'] = txt.string
                
                if 'title' in challenge_data:
                    challenges_list.append(Challenge(**challenge_data))
        print('going to create:', challenges_list)
        Challenge.objects.bulk_create(challenges_list)

    def get_soup(self,fn):
        fp = open(f'{self.folder}/{fn}')
        return BeautifulSoup(fp.read(), 'html.parser')
    
    def parse_challenge(self,challenge):
        if not os.path.exists(f'{self.folder}/challenges/{challenge.c_id}.html'):
            self.filesnotfound.append(challenge.c_id)
            return

        # Parse Instruction
        soup = self.get_soup(f'challenges/{challenge.c_id}.html')
        instructions=soup.find_all("div", {"class": "instructions"})
        if instructions:
            challenge.instructions= str(instructions[0])
            challenge.save()

        # Parse Solution
        soup = self.get_soup(f'challenges/{challenge.c_id}_solution.html')
        solutions = [
            Solution.objects.get_or_create(challenge=challenge, text=sol.text, defaults={'html':str(sol)}) 
            for sol in soup.find_all("div", {"class": "CodeMirror-code"})
        ]

        self.filessynced.append(challenge.c_id)


class ChallengesAjaxDatatableView(AjaxDatatableView):
    model = Challenge
    initial_order = [["title", "asc"], ]

    column_defs = [
        AjaxDatatableView.render_row_tools_column_def(),
        {'name': 'id', 'visible': False, },
        {'name': 'title', 'visible': True },
        {'name': 'c_id', 'visible': True, },
        {'name': 'difficulty', 'visible': True, },
        {'name': 'desc', 'visible': False},
        {'name': 'lang', 'visible': False, },
        {'name': 'tags', 'visible': False, },        
        # {'name': 'app_label', 'foreign_field': 'content_type__app_label', 'visible': True, },
    ]
