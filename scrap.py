from selenium.webdriver.firefox.options import Options as FirefoxOptions
from selenium import webdriver
from selenium.webdriver.common.by import By
import selenium.webdriver.support.ui as ui

import getpass
import datetime
import os
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

    def get_challenge(self, c_id):
        folder = os.path.join(self.folder,'challenges')
        if not os.path.exists(f'{folder}/{c_id}.html'):
            self.driver.get(f'{self.url}/challenge/{c_id}')
            someVariable = input("Press Enter after page fully loads.")
            self.create_html(f'{folder}/{c_id}.html')
            yesno = input('if you want to scrap solution press y after navigation.?')
            if yesno in ['y','Y']:
                self.create_html(f'{folder}/{c_id}_solution.html')
        


if __name__=='__main__':
    # get_html()
    scrapper = Edabit()
    scrapper.get_challenges()
    chs = ['8ym3dKrL3svkYr4h4'] # '8ym3dKrL3svkYr4h4', 'rZToTkR5eB9Zn4zL']
    for challenge in chs:
        print(challenge)
        scrapper.get_challenge(challenge)