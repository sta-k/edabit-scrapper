from django.http import HttpResponse
from django.views import generic

from bs4 import BeautifulSoup

html_file = 't3.html'

class ChallengesListView(generic.list.ListView):
    model = Challenges

def sync_db(request):
    fp = open(html_file)
    soup = BeautifulSoup(fp.read(), 'html.parser')
    n=0 # total challenges
    for challenge in soup('a'):
        challenge_url = challenge.get('href')
        if 'challenge' in challenge_url:
            items = challenge.find_all(['div','h3'])
            for i,txt in enumerate(items):
                if i==0: 
                    n+=1
                    print(txt.string)
                    print('='*20)
                    print('ID:',challenge_url.strip('/challenge/'))
                if i==1: print('Desc:',txt.string[:20])
                if i==2: print('Tags:',[t.contents[1] for t in txt('div')]) #'/'.join([t.string for t in txt('div') if t]))
                if i==len(items)-1: print('Difficulty:', txt.string)
            print()

    print(f'Total challenges: {n}')
    return HttpResponse('success')
