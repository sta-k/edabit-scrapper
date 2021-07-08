from selenium.webdriver.firefox.options import Options as FirefoxOptions
from selenium import webdriver
from selenium.webdriver.common.by import By
import selenium.webdriver.support.ui as ui


import datetime
import os, sys
# pip install selenium

class Edabit:
    def __init__(self):
        options = FirefoxOptions()
        self.folder = 'htmlfiles'
        # options.add_argument("--headless")
        self.driver = webdriver.Firefox(options=options)
        self.url = 'https://edabit.com'

    def create_html(self, html_file):
        fp = open(html_file, 'w') # open(f'{html_file}_{datetime.datetime.now():%d%m%y%H%M}.html', 'w')
        wait = ui.WebDriverWait(self.driver, 10) # timeout after 10 seconds
        results = wait.until(lambda driver: self.driver.page_source)
        fp.write(results)

    def get_challenges(self):
        self.driver.get(f'{self.url}/challenges')
        # https://stackoverflow.com/a/16928204/2351696
        langs = ['Cplusplus','C#','Java','JavaScript','PHP','Python','Ruby','Swift']      
        print(f'Options: '+'\n'.join([f'{int(i)+1}: {l}' for i,l in enumerate(langs)]))
        lang = input("Select an option after clicking load_more button as much as you can:")
        fp = os.path.join(self.folder,'languages',f'challenges_{langs[int(lang)-1].lower()}.html')
        self.create_html(fp)

    def get_challenge(self, c_id, folder):
        if os.path.exists(os.path.join(self.folder,'challenges',f'{c_id}.html')):
            print('File exists:'+c_id)
        else:
            self.driver.get(f'{self.url}/challenge/{c_id}')
            someVariable = input("Press Enter after page fully loads.")
            self.create_html(f'{folder}/{c_id}.html')
            someVariable = input('Press Enter after unlocking solution.')
            self.create_html(f'{folder}/{c_id}_solution.html')
        


if __name__=='__main__':
    if len(sys.argv) == 2 and sys.argv[1] in ['all','ids']:
        scrapper = Edabit()
        if sys.argv[1] == 'all':
            # get instructions and solutions
            challenges = ['8ym3dKrL3svkYr4h4']          
            challenges_dir ='challenges' 
            # create a new dir if challenges exists
            if os.path.exists(os.path.join(scrapper.folder,challenges_dir)):
                challenges_dir = f'old/{datetime.datetime.now():%d%m%y%H%M}'
            new_folder = os.path.join(scrapper.folder,challenges_dir)
            os.makedirs(new_folder)

            
            for challenge in challenges:
                print(f'{challenges.index(challenge)}/{len(challenges)}:{challenge}')
                scrapper.get_challenge(challenge, new_folder)

        elif sys.argv[1] == 'ids':
            # get ids
            scrapper.get_challenges()
    else:
        print('please call with args[ids,all]. eg: python scrap.py all')
        
    