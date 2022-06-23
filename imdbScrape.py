import requests
from bs4 import BeautifulSoup
import time
 

def getTop10ComediesX():
    print("Retrieving")
    start = time.perf_counter()
    all_titles = []
    title_ratings = []
    votes = []
    page = 51
    scanContinue = True
    res = requests.get("https://www.imdb.com/search/title/?title_type=movie&genres=adventure&sort=num_votes,desc&explore=title_type,genres&ref_=adv_prv")
    soup = BeautifulSoup(res.content, 'html.parser')
    res_body = soup.body
    content = soup.findAll('h3', attrs={'class' : 'lister-item-header'})
    for p in content:
        results = p.text.replace(',', '').replace('"', '').replace('.', '').replace("'", "").replace('?', '').replace("\n", "").replace('\r', '')
        all_titles.append(results)

    ratings = soup.findAll('div', attrs={'class' : 'inline-block ratings-imdb-rating'})
    for p in ratings:
        ratingsResults = p.text.replace(',', '').replace('"', '').replace("'", "").replace('?', '').replace("\n", "").replace('\r', '').replace(' ', '')
        title_ratings.append(ratingsResults)

    voteCount = soup.findAll('span', attrs={'name' : 'nv'})
    for p in voteCount:
        results = p.text.replace(',', '').replace('"', '').replace('.', '').replace("'", "").replace('?', '').replace("\n", "").replace('\r', '').replace(" ","")
        votes.append(results)

    while scanContinue:
        res = requests.get(f"https://www.imdb.com/search/title/?title_type=movie&genres=adventure&sort=num_votes,desc&start={page}&explore=title_type,genres&view=advanced")
        soup = BeautifulSoup(res.content, 'html.parser')
        res_body = soup.body

        content = soup.findAll('h3', attrs={'class' : 'lister-item-header'})
        for p in content:
            results = p.text.replace(',', '').replace('"', '').replace('.', '').replace("'", "").replace('?', '').replace("\n", "").replace('\r', '')
            all_titles.append(results)

        ratings = soup.findAll('div', attrs={'class' : 'inline-block ratings-imdb-rating'})
        for p in ratings:
            ratingsResults = p.text.replace(',', '').replace('"', '').replace("'", "").replace('?', '').replace("\n", "").replace('\r', '').replace(' ', '')
            title_ratings.append(ratingsResults)

        voteCount = soup.findAll('span', attrs={'name' : 'nv'})
        for p in voteCount:
            results = p.text.replace(',', '').replace('"', '').replace('.', '').replace("'", "").replace('?', '').replace("\n", "").replace('\r', '')
            head, sep, tail = results.partition('$')
            votes.append(head)

        page = int(page) + 50
        if page > 100:
            scanContinue = False
    combined = dict(zip(all_titles, zip(title_ratings, votes)))

    for key, value in combined.items():
        print(f"{key} : {value}")
        
    finish = time.perf_counter()
    print(f"{len(all_titles)}Results found in: {start - finish:0.4f} seconds")

def getTop10Comedies1():
    start = time.perf_counter()
    all_titles = []
    page = 51
    scanContinue = True
    res = requests.get("https://www.imdb.com/search/title/?title_type=movie&genres=comedy,romance&view=simple&sort=user_rating,desc&explore=title_type,genres&ref_=adv_prv")
    soup = BeautifulSoup(res.content, 'html.parser')
    res_body = soup.body
    content = soup.findAll('div', attrs={'class' : 'col-imdb-rating'})
    for p in content:
        results = p.text.replace(',', '').replace('"', '').replace("'", "").replace('?', '').replace("\n", "").replace('\r', '')
        all_titles.append(results)
    while scanContinue:
        res = requests.get(f"https://www.imdb.com/search/title/?title_type=movie&genres=comedy,romance&view=simple&sort=user_rating,desc&start={page}&explore=title_type,genres&ref_=adv_nxt")
        soup = BeautifulSoup(res.content, 'html.parser')
        res_body = soup.body
        content = soup.findAll('div', attrs={'class' : 'col-imdb-rating'})
        for p in content:
            results = p.text.replace(',', '').replace('"', '').replace("'", "").replace('?', '').replace("\n", "").replace('\r', '')
            all_titles.append(results)
        page = int(page) + 50
        if page > 100:
            scanContinue = False
    for i in all_titles[0:100]:
            print(i)
    finish = time.perf_counter() 
    print(f"{len(all_titles)}Results found in: {start - finish:0.4f} seconds")

getTop10ComediesX()

