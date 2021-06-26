from selenium.webdriver.firefox.options import Options as FirefoxOptions
from selenium import webdriver
from selenium.webdriver.common.by import By
import selenium.webdriver.support.ui as ui

import getpass
from bs4 import BeautifulSoup

# beautifulsoup4
# selenium

url = 'https://edabit.com/challenges'
html_file = 't3.html'

def get_html():
    options = FirefoxOptions()
    # options.add_argument("--headless")
    driver = webdriver.Firefox(options=options)
    driver.get(url)

    # https://stackoverflow.com/a/16928204/2351696
    someVariable = getpass.getpass("Press Enter after You are done logging in")

    # load_more = driver.findElement(By.cssSelector('.ui.fluid.button'))
    # webdriver.ActionChains(driver).click(load_more).perform()

    fp = open(html_file, 'w')
    wait = ui.WebDriverWait(driver, 10) # timeout after 10 seconds
    results = wait.until(lambda driver: driver.page_source)
    fp.write(results)

def parse():
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


if __name__=='__main__':
    get_html()
    parse()