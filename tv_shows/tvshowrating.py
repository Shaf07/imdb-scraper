import requests
from bs4 import BeautifulSoup
import time

floatRating = []
def getTVRatings(genre):
    all_ratings = []
    page = 51 
    scanContinue = True 
    start = time.perf_counter() #starts the counter to see how long results take
    print("Gathering Ratings (approx 30 seconds)...")

    genre = requests.get(f"https://www.imdb.com/search/title/?title_type=tv_series,tv_miniseries&genres={genre}&sort=num_votes,desc&explore=genres") #the main page for the genre with votes in descending order
    soup = BeautifulSoup(genre.content, 'html.parser') #will parse HTML content
    genre_body = soup.body 
    ratings = soup.findAll('div', attrs={'class' : 'inline-block ratings-imdb-rating'})
    for p in ratings:
        ratingsResults = p.text.replace(',', '').replace('"', '').replace("'", "").replace('?', '').replace("\n", "").replace('\r', '').replace(' ', '')
        all_ratings.append(ratingsResults)

    while scanContinue:
        genre = requests.get(f"https://www.imdb.com/search/title/?title_type=tv_series,tv_miniseries&genres={genre}&sort=num_votes,desc&start={page}&explore=gengenre&ref_=adv_nxt")
        soup = BeautifulSoup(genre.content, 'html.parser')
        genre_body = soup.body

        ratings = soup.findAll('div', attrs={'class' : 'inline-block ratings-imdb-rating'})
        for p in ratings:
            ratingsResults = p.text.replace(',', '').replace('"', '').replace("'", "").replace('?', '').replace("\n", "").replace('\r', '').replace(' ', '')
            all_ratings.append(ratingsResults)

        page = int(page) + 50
        if page > 101:
            scanContinue = False
      
    finish = time.perf_counter()
    print(f"Rating Results found in: {start - finish:0.4f} seconds")
    floatRatings = list(map(float, all_ratings))
    for i in floatRatings:
        floatRating.append(i)
    return(floatRating)

