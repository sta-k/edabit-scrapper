from selenium.webdriver.firefox.options import Options as FirefoxOptions
from selenium import webdriver
from selenium.webdriver.common.by import By
import selenium.webdriver.support.ui as ui

import getpass

# pip install selenium

url = 'https://edabit.com/challenges'
html_file = 'challenges.html'

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


if __name__=='__main__':
    get_html()