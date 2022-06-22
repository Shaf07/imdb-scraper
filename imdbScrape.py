import requests
from bs4 import BeautifulSoup

import time

res = requests.get('https://www.imdb.com/search/title/?title_type=movie&genres=comedy&view=simple&sort=user_rating,desc&explore=title_type,genres')
soup = BeautifulSoup(res.content, 'html.parser')
res_body = soup.body

def getTop10Comedies():
    all_titles = []
    content = soup.findAll('span', attrs={'class' : 'lister-item-header'})
    for p in content:
        results = p.text.replace(',', '').replace('"', '').replace('.', '').replace("'", "").replace('?', '').replace("\n", "").replace('\r', '')
        all_titles.append(results)
    for i in all_titles[0:10]:
        print(i)


