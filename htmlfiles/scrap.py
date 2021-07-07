from selenium.webdriver.firefox.options import Options as FirefoxOptions
from selenium import webdriver
from selenium.webdriver.common.by import By
import selenium.webdriver.support.ui as ui

import getpass
import datetime
# pip install selenium

class Edabit:
    def __init__(self):
        options = FirefoxOptions()
        # options.add_argument("--headless")
        self.driver = webdriver.Firefox(options=options)
        self.url = 'https://edabit.com'

    def create_html(self, html_file):
        fp = open(f'{html_file}_{datetime.datetime.now():%d%m%y%H%M}.html', 'w')
        wait = ui.WebDriverWait(self.driver, 10) # timeout after 10 seconds
        results = wait.until(lambda driver: self.driver.page_source)
        fp.write(results)

    def get_challenges(self):
        self.driver.get(f'{self.url}/challenges')
        # https://stackoverflow.com/a/16928204/2351696
        someVariable = getpass.getpass("Press Enter after clicking load_more button as much as you can.")
        self.create_html('challenges-python')

    def get_challenge(self, c_id):
        self.driver.get(f'{self.url}/challenge/{c_id}')
        self.create_html(c_id)
        # for solutions
        someVariable = getpass.getpass("Press Enter after You are done logging in and solution clicked") # login
        self.create_html(f'{c_id}_solution')


if __name__=='__main__':
    # get_html()
    scrapper = Edabit()
    # scrapper.get_challenges()
    scrapper.get_challenge('rZToTkR5eB9Zn4zLh') #ARr5tA458o2tC9FTN')