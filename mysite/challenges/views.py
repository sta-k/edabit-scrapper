from bs4 import BeautifulSoup
from django.shortcuts import redirect
from django.views import generic
from django.views import View

from .models import Challenge, Solution

class ChallengesListView(generic.list.ListView):
    model = Challenge

def sync_db(request):
    # Challenge.objects.all().delete()
    html_file = 'static_htmls/challenges-python.html'
    fp = open(html_file)
    soup = BeautifulSoup(fp.read(), 'html.parser')
    n=0 # total challenges
    challenges_list=[]
    for challenge in soup('a'):
        challenge_url = challenge.get('href')
        if challenge_url and 'challenge' in challenge_url:
            items = challenge.find_all(['div','h3'])
            challenge_data = {
                'url':challenge_url,
                'c_id':challenge_url.replace('/challenge/',''),
                'lang': html_file.split('-')[1].split('.')[0]
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
    print(f'Total challenges: {n}')
    return redirect('home')


class SyncChallengeView(View):
    def get_soup(self,fn):
        fp = open(f'static_htmls/{fn}')
        return BeautifulSoup(fp.read(), 'html.parser')
    
    def parse_instruction(self, c_id):
        # Parse Instruction
        soup = self.get_soup(f'{c_id}.html')
        # remove dropdown: python, javascript... etc
        # soup.find('div',{"class": "dropdown"}).decompose() #  attrs={'style':'font-size: 1.05rem;margin-bottom:8px;margin-top:-10px;'}).decompose()
        instructions=soup.find_all("div", {"class": "instructions"})
        if instructions:
            challenge=Challenge.objects.get(c_id=c_id)
            challenge.instructions= str(instructions[0])
            challenge.save()

    def parse_solution(self, c_id):
        # Parse Solution
        soup = self.get_soup(f'{c_id}_solution.html')
        solutions = [
            Solution.objects.get_or_create(challenge=Challenge.objects.get(c_id=c_id), text=sol.text) 
            for sol in soup.find_all("div", {"class": "CodeMirror-code"})
        ]
        print(Solution.objects.filter(challenge=Challenge.objects.get(c_id=c_id)).count())

    def get(self, request):

        challenge_id = request.GET["c"]
        self.parse_instruction(challenge_id)
        self.parse_solution(challenge_id)
        return redirect('home')
    