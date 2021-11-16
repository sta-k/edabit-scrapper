from bs4 import BeautifulSoup

"""
update solutions.html by coping from console
now run:
    >>> python parse_solutions.py
"""
def get_solutions():
    fp = open(f'solutions.html')
    soup = BeautifulSoup(fp.read(), 'html.parser')
    for sol in soup.find_all("div", {"class": "CodeMirror-code"}):
        print('<pre><code>')
        print(sol.text)
        print('</code></pre>')

if __name__=='__main__':
    get_solutions()