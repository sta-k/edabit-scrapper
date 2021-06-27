from bs4 import BeautifulSoup
from django.shortcuts import redirect
from django.views import generic

from .models import Challenge



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
                'c_id':challenge_url.strip('/challenge/'),
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
                    print('ID:',challenge_url.strip('/challenge/'))
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

def sync_challenge(request):

    fp = open('static_htmls/ARr5tA458o2tC9FTN.html')
    soup = BeautifulSoup(fp.read(), 'html.parser')
    for challenge in soup.find_all("div", {"class": "rc-tabs-tabpane"}):
        print(challenge)

    return redirect('home')
    