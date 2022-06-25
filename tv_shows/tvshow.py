import requests
from bs4 import BeautifulSoup
import time

all_titles = []
def getTVShows(genre): 
    all_titles = []
    page = 51 
    scanContinue = True 
    start = time.perf_counter() #starts the counter to see how long results take
    print("Gathering Shows (approx 30 seconds)...")

    genre = requests.get(f"https://www.imdb.com/search/title/?title_type=tv_series,tv_miniseries&genres={genre}&sort=num_votes,desc&explore=genres") #the main page for the genre with votes in descending order
    soup = BeautifulSoup(genre.content, 'html.parser') #will parse HTML content
    genre_body = soup.body 
    content = soup.findAll('h3', attrs={'class' : 'lister-item-header'})
    for p in content:
        results = p.text.replace(',', '').replace('"', '').replace("'", "").replace('?', '').replace("\n", "").replace('\r', '')
        head, sep, tail = results.partition('.')
        all_titles.append(tail)

    while scanContinue:
        genre = requests.get(f"https://www.imdb.com/search/title/?title_type=tv_series,tv_miniseries&genres={genre}&sort=num_votes,desc&start={page}&explore=gengenre&ref_=adv_nxt")
        soup = BeautifulSoup(genre.content, 'html.parser')
        genre_body = soup.body

        content = soup.findAll('h3', attrs={'class' : 'lister-item-header'})
        for p in content:
            results = p.text.replace(',', '').replace('"', '').replace("'", "").replace('?', '').replace("\n", "").replace('\r', '')
            head, sep, tail = results.partition('.')
            all_titles.append(tail)

        page = int(page) + 50
        if page > 1001:
            scanContinue = False        
    finish = time.perf_counter()
    print(f"Results found in: {start - finish:0.4f} seconds")
    print(all_titles)

getTVShows('comedy')