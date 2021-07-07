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
        someVariable = getpass.getpass("Press Enter after clicking load_more button as much as you can.")
        self.create_html('challenges-python')

    def get_challenge(self, c_id):
        
        if not os.path.exists(f'{c_id}.html'):
            print(c_id)
            self.driver.get(f'{self.url}/challenge/{c_id}')
            someVariable = getpass.getpass("Press Enter after clicking load_more button as much as you can.")
            self.create_html(f'{c_id}.html')
        

    def get_challenge_solution(self, c_id):
        self.driver.get(f'{self.url}/challenge/{c_id}')
        # for solutions
        someVariable = getpass.getpass("Press Enter after You are done logging in and solution clicked") # login
        self.create_html(f'{c_id}_solution.html')



if __name__=='__main__':
    # get_html()
    scrapper = Edabit()
    # scrapper.get_challenges()
    chs = ['8ym3dKrL3svkYr4h4', 'rZToTkR5eB9Zn4zL', 'KjCS7occ9hfu5snpb', 'FQyaaJx7orS7tiwz8', 'WLTzrRsrw7RakYrN', 'CjXamaNRmKxwkmBxq', 'yeNvKWdDFKRAk4D', 'Zerwo2AENbvRZTe83', 'KWoj7kWiHRqJtG6S2', 'GPmoRCZKkyNtoJMcN', 'xbZR26rHMNo32yz35', 'Yx2a9B57vXRuPevG', 'v5gc8FQkDEepkqpfp', 'mDzheHpwtqyXePEBE', 'xWSjvoH7mEkSnqS7H', 'QQp2o22huzBCkHesy', 'sLkTkfLgZYs5wejs', 'EQ3rBrKrztQK8qAd', 'wqqc5p3oiFXRJAQm', 'QzXtDnSZL6y4ZcEvT', 'YN9mNNc4mMPDxyhFf', 'PjcKZRx8YE5KzRN63', 'WKJwo2xDNjKxwtGoH', 'XXJbGFEkrMWCp8yF', 'KWnJrMzK9CumnfxTF', 'jKAjLk5epb8XDzTwC', 'yfooETHj3sHoHTJsv', 'Rx2pkSA9dCmtwS8xt', 'D2Hvq6NZchp7Q6ftR', 'A7hyDnb72prWryeuY', 'SZ5kDBwCD3ctjE6', 'XsJLwhAddzbxdQqr4', 'CWMeiJCP9Ef8XMq8', '6fx8iNCHETW8KqAui', 'pZ3HxBfvejsvkEDo4', 'uPtuNNTuASzPZMQrW', 'ZAYqnMhmqT5K3JWu8', 'QJiqdu9QGMmAgK5Fi', 'oRuMC4Ykksti8Z47', 'SNM5EZ3FePECt2HQ', '49pyDP8dE3pJ2dYMW', 'foFKdr68vSENQ9AYB', 'Yj2Rew5XQYpu7Nosq', 'NebFhjXTn8NEbhYXY', 'bWDtMHtZARm7sdNA', 'HuWQaCpFR7iTeCvTm', 'pKyeEDkNqZraqS3rW', 'F5ycABGyZtghMpYjr', 'C3N2JEfFQoh4cqQ98', 'NRxWszQRw5JqSDmQS', 'iBL3eDRWzpxgfQyHx', 'WYq4aFwSNuoyFCW5G', 'wtu32ZFxHJsuQnogX', '2BvLTb49ywi2vubpm', 'QKmETue6fMTdcB8Rq', 'vBEm4jimnvxaFhdgs', 'dP9osvXn6r6F36wYF', '8rcrBw82sfHyCmJMG', 'Qei2FyKLmSCbYDkbm', 'HRu9WggWxdSpYjxNf', 'pFQPcaaASgHuACbaS', 'XRfoKp8m9Q6qvpRv', 'Z6zaRiKn7dfvJhnF', 'YEwPHzQ5XJCafCQmE', 'JCZqhijycsNizczsR', 'EkhfsvH6drYCLmAbL', 'EPS5tFxKQB7vWXLs6', 'yQTiQAcFJhtauhe3', 'StXTiYtCwyY4tEpP', '2HhmMdGPSpJ8EFrZ', '2XLjgZhmACph76Pkr', 'F7qjLMhPzJgyNEqdi', 'j9hv6sXmfvqkicLJC', 'LRevQqmaH78mwyYXi', 'iwtHzRDB6pMKoBL', 'vFFsWbTX2JuvjKZvf', 'YSJjPdkwrhQCfnkcZ', 'jcAfvJxEqA2fuE2qZ', '6YN2ww3B4cQZ6rTmN', 'f3jm7sk7LaYttYyLP', 'ogjDWJAT2kTXEzkD5', 'ZGezQDXsturZGpQcS', 'YWoJkmMHYEENCvgRP', 'DruRW8YM8PNiH9Kg7', 'jozLzME3YptxydiQm', 'HQXRKxQXECFTCFTt', '8rXfBzRZbgZP7mzyR', 'Ne2LgRan7bZWs7BS7', 'r3T23PTQnZRgjWGFH', 'irb783PpFTDqnumhN', '9wfEZ4898nnpa9wL5', '3JbLM2bRh8XNDABTH', '7shokLkiNu2PEpWtP', 'CmiYBGTCXxPoHBio', 'QM6ZgHxvQCDX9Tzo', 'jmn5FDFyLDPA4t6zP', 'F7iLaLDBHqshWSZz5', 'xNxZx7DDr6BumJLaB', 'yeqgXCk6NTpsexQ5B', 'DgL3Ka5tBwF9SC6z', '7ECZC8CBEhy5QkvN3', 'KthyMugQzDEFJT', 'pAFxfge35bT3zj4Bs', 'xdSKkXQkkMroNzq8C', 'u68XgCZcWGphs5R54', 'PaBJ7KJZ8fZtjJgL', 'pfuxt3J2p2tph3LJQ', 'CHwX2o6rqrBsL4gzr', 'y9Rans4Ry5oW74cat', 'rR2qf7ELnXoXESiz2', 'sLb2Fs6aGRQBYAXqQ', 'Fej5HSzcvHMdm2i4N', 'PtrPzWCWrPW54xfxK', 'PE8XQipGLS5bhpLZ5', 'YA5sLYuTzQpWLF8xP', 'MNrEx87Bzsg6TfuMY', 'Mm4BaYNPaXHJKWA7M', 'SKdpWwgKMAwMPHvRK', 'mvH3d8E2pKhCjsu3', '9kkSyfN62E4At9wcy', 'bGHnhQr5bjH8kd8rG', 'phEQ7teNSYSQdDHPr', 'MSjfXQ4gvMzeezFgB', 'fBzF8TuQQxx6C7dWm', 'Fe4dD4xrdBJjQ7H9', 'fHwaeLLz2vN9XzFft', '2vvfEodtq4RYsbcr', 'YsYysHoxaHZbv3vS8', 'DbFcBJiRz3GDm6xns', '9zsDKijmBffmnk9AP', '5HP8CmfXd7am7NtX', 'F4iemEeFfsaFoMpAF', 'D6Qbh5doP6RvopoF3', 'F3M4PhqC4JdX28Qmx', 'Xrftj2hA822v4AKcK', 'iipAZ7sK8C5sRF8K6', 'Jm4eKTENReSiQFw9t', 'vAk9SBqYmj6hXKfrD', 'Luhb2KStP2wiX6FMp', 'fqn5FcLzEb4RBH9w7', 'mcC546MLnBjNLXTb8', 'zdo6JCL6Z5d2fT8JB', 'BajbSekxzL2hudEW', 'j7JPnAuW8dy4ggdp', 'dTxY9oQuNHAovpDCm', 'u5WsfTX8rXb2phrNp', 'MaekZ28kEvH9ZxP', '3XYv6RZbrbaoTWJ4H', 'ZF6vZwPc5He5u5EF', 'oZAkiD6H7sf7zpZp', 'CAgmHcypCLFDSadGp', '38oPds8QTdn7mhGsR', 'FtwouqMohuumDZh23', 'EMjazHJw24y93kyD4', 'GuoJCiRJkr9CLRqJ', 'SFE4q5pFTi8TBwj76', 'ove5xwGAKfMxRmcbF', 'Ti98ADcrmxi3NP68f', '7ujabrnbRK9w6Z5xb', 'vJrhnikLPK9jhFbyH', 'rZToTkR5eB9Zn4zLh', 'aWLTzrRsrw7RakYrN', 'nyeNvKWdDFKRAk4Da', 'Yx2a9B57vXRuPevGh', 'sLkTkfLgZYs5wejsg', 'hEQ3rBrKrztQK8qAd', 'gwqqc5p3oiFXRJAQm', 'XXJbGFEkrMWCp8yFn', 'ecSZ5kDBwCD3ctjE6', 'cCWMeiJCP9Ef8XMq8', 'coRuMC4Ykksti8Z47', 'SNM5EZ3FePECt2HQn', 'gbWDtMHtZARm7sdNA', 'eXRfoKp8m9Q6qvpRv', 'cZ6zaRiKn7dfvJhnF', 'ayQTiQAcFJhtauhe3', 'cStXTiYtCwyY4tEpP', '2HhmMdGPSpJ8EFrZe', 'iwtHzRDB6pMKoBLaa', 'HQXRKxQXECFTCFTtn', 'hCmiYBGTCXxPoHBio', 'QM6ZgHxvQCDX9Tzoa', 'DgL3Ka5tBwF9SC6zn', 'gcKthyMugQzDEFJTg', 'hPaBJ7KJZ8fZtjJgL', 'hmvH3d8E2pKhCjsu3', 'Fe4dD4xrdBJjQ7H9a', '2vvfEodtq4RYsbcrh', 'g5HP8CmfXd7am7NtX', 'BajbSekxzL2hudEWe', 'aj7JPnAuW8dy4ggdp', 'MaekZ28kEvH9ZxPga', 'ZF6vZwPc5He5u5EFe', 'oZAkiD6H7sf7zpZpn', 'GuoJCiRJkr9CLRqJa']
    for challenge in chs:
        scrapper.get_challenge(challenge) #rZToTkR5eB9Zn4zLh') #ARr5tA458o2tC9FTN')