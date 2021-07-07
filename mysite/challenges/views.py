from bs4 import BeautifulSoup
import os
from django.shortcuts import redirect, reverse
from django.views import generic
from django.views import View
from django.conf import settings

from .models import Challenge, Solution

class ChallengesListView(generic.list.ListView):
    model = Challenge


class ChallengeDetailView(generic.detail.DetailView):
    model = Challenge

def sync_db(request):
    syncer = SyncChallenge()
    syncer.sync()
    return redirect('home')


class SyncChallenge:
    def __init__(self):
        print(settings.BASE_DIR)
        self.folder = os.path.join(settings.BASE_DIR, '..','htmlfiles')


    def sync(self):
        for lang in ['Cplusplus','C#','Java','JavaScript','PHP','Python','Ruby','Swift']:
            fn = f'languages/challenges_{lang.lower()}.html'
            if os.path.exists(f'{self.folder}/{fn}'):
                self.parse_challenge_list(fn)

        for challenge in Challenge.objects.all():
            self.parse_instruction(challenge)
            self.parse_solution(challenge)

    def parse_challenge_list(self, fn):
        soup = self.get_soup(fn)
        n=0 # total challenges
        challenges_list=[]
        for challenge in soup('a'):
            challenge_url = challenge.get('href')
            if challenge_url and 'challenge' in challenge_url:
                items = challenge.find_all(['div','h3'])
                challenge_data = {
                    'url':challenge_url,
                    'c_id':challenge_url.replace('/challenge/',''),
                    'lang': fn.split('_')[1].split('.')[0]
                } # c_id,lang,title,url,desc,tags,difficulty
                if Challenge.objects.filter(c_id=challenge_data['c_id'], lang=challenge_data['lang']):
                    print('Challenge already exists.')
                    continue
                for i,txt in enumerate(items):
                    if i==0: 
                        n+=1
                        challenge_data['title'] = txt.string
                        print(txt.string)
                        print('='*20)
                        print('ID:',challenge_url.replace('/challenge/',''))
                    if i==1: 
                        challenge_data['desc'] = txt.string
                        print('Desc:',txt.string[:20])
                    if i==2: 
                        challenge_data['tags'] = ','.join([t.contents[1] for t in txt('div')])
                        print('Tags:',[t.contents[1] for t in txt('div')]) #'/'.join([t.string for t in txt('div') if t]))
                    if i==len(items)-1: 
                        challenge_data['difficulty'] = txt.string
                        print('Difficulty:', txt.string)
                
                if 'title' in challenge_data:
                    print(challenge_data)
                    challenges_list.append(Challenge(**challenge_data))
                print()

        Challenge.objects.bulk_create(challenges_list)

    def get_soup(self,fn):
        fp = open(f'{self.folder}/{fn}')
        return BeautifulSoup(fp.read(), 'html.parser')
    
    def parse_instruction(self, challenge):
        # Parse Instruction
        soup = self.get_soup(f'challenges/{challenge.c_id}.html')
        # remove dropdown: python, javascript... etc
        # soup.find('div',{"class": "dropdown"}).decompose() #  attrs={'style':'font-size: 1.05rem;margin-bottom:8px;margin-top:-10px;'}).decompose()
        instructions=soup.find_all("div", {"class": "instructions"})
        if instructions:
            # challenge=Challenge.objects.get(c_id=c_id)
            challenge.instructions= str(instructions[0])
            challenge.save()

    def parse_solution(self, challenge):
        # Parse Solution
        soup = self.get_soup(f'challenges/{challenge.c_id}_solution.html')
        solutions = [
            Solution.objects.get_or_create(challenge=challenge, text=sol.text) 
            for sol in soup.find_all("div", {"class": "CodeMirror-code"})
        ]
        print(Solution.objects.filter(challenge=challenge).count())


# class SyncChallengeView(View):
#     def get(self, request):

#         challenge = Challenge.objects.get(c_id=request.GET["c"])
#         return redirect(reverse('challenge-detail', args=[challenge.id]))
#     