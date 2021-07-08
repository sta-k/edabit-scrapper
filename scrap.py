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
            challenges = ['8ym3dKrL3svkYr4h4', 'zeuvB4YRvu47w8e8f', 'RB6iWFrCd6rXWH3vi', 'KveKxSD9t8fX7ybSt', 'jecvfH5eyGLrSwzNh', 'XQwPPHE6ZSu4Er9ht', 'L2nw2N2YqZCboiaYM', '4AjWvJdZpFEMbGALd', 'YDgtdP69Mn9pC73xN', 'Yp8crKmgxZ3HiSBAZ', 'BfSj2nBc33aCQrbSg', 'aFLqW5hqqRmM4QXZq', 'grorumaEjyFDmZQCx', 'j9zed4GnykS48W6vh', 'BDjhphREEa6Ds44Ty', 'JzXH3QnwHmpptadQr', 'c6FoPFprcNW6u5oAn', 'rihSbQq6x8R2D4aoa', 'eHwd6medMrY3QXM8k', '6RHxTTndfASnPyp8Z', 'T4q8P8cxvBtaLPW4q', 'TsRjbMRoNCM3GHuDk', '9Px2rkc9TPhK54wDb', 'i7TaDyRQQZCY3g2JG', '4AzBbuPLxKfJd7aeG', 'HqpZQPZiHbPK4HgEB', '2C3gtb4treAFyWJMg', 'siuKPSYXjjic9zEF2', '58RNhygGNrKjPXwna', '9iLhKgqZn5exBrmWm', 'C6pHyc4iN6BNzmhsM', '28mJ6NgqbQS4YRgDc', '2rQcGmSYvXRtxSuHn', 'xEGFoPmMm28h7HQ7a', 'Zx9L2dpHr2nMjaKXp', 'fbqmyDjCigbYhWLJa', 'xXenZR2hWFE7Jb9vR', 'cvA35yPFAggr7rtve', 'EWZqYT4QGMYotfQTu', '5S97Me79PDAefLEXv', 'L9Zh7dWsENnE9P6qc', 'Y4gwcGfcGb3SKz6Tu', 'KETgxWCWtrk7oLM49', 'cBzYRBbBA7gHwKpor', 'k2aWnLjrFoXbvjJdb', 'ZsAXt5Kj5EP4v3ack', 'CMDy4pvnTZkFwJmmx', 'Kv8DMmwfuKTLyZD5E', '4xZFisQX8NnYB3nv4', 'pmYNSpKyijrq2i5nu', 'E9Wkppxyo763XywBe', 'rFK7WftrcrEu6rbu8', 'uusYhAkGc9W2ufBwc', 'H7Z8enQWipfBMXTx7', 'zhqL89ZWgbxbixsdD', 'CMqa7tAtffudQ7hs4', 'eoK63mG5tJDu439nJ', 'vcFgGJHxhTwRiLK5d', 'YxnrZQwKyrzgcMvT4', 'ntpgCFga2rRzB53QZ', 'sKKSaJfQNfc2oc7BS', 'qNQkYzY8GpiFMmndh', 'FEK7892zgj4nPJvkE', 'cHzvB5KCWCK3oCLGL', '6kseWBaSTv6GgaKDS', 'RoEn338P4xAf7mNNg', 'Mb8KmicGqpP3zDcQ5', 'oFqkxLiqeSGL8xmBn', 'Sjti2fmLY6sLJHr9p', 'BHBXNfeMsA43d8Tys', '88WesDgd2Ge9JEiJM', 'bmYrX5N9DBF27Fx63', 'tftN3EdkSPfXxzWpi', 'xzaREqFLW3tZdGnTA', 'YcKh5TokDmm8MZ9Dk', 'FnyAGdwgcH4whynjR', 'Z2mhqFLe9g9ouZY64', 'jyHs9YRnrPgLwKiaL', '3ucrYGBkvJwjbFL4G', '9cY7ymbp5mtrKdxyR', 'B5J4Bfgg7PoDHBBZQ', 'JHubqEB54KxbWP3sR', 'qosZ7W2qppFo7MhNB', 'FGzWE8vNyxtTrw3Qg']
            
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
        
    