from re import I
from webbrowser import get
import requests
from bs4 import BeautifulSoup
import time

intVotings = []
def getVotesTV(genre): 
    all_votings = []
    page = 51 
    scanContinue = True 
    start = time.perf_counter() #starts the counter to see how long results take
    print("Gathering Votes (approx 30 seconds)...")

    genre = requests.get(f"https://www.imdb.com/search/title/?title_type=tv_series,tv_miniseries&genres={genre}&sort=num_votes,desc&explore=genres") #the main page for the genre with votes in descending order
    soup = BeautifulSoup(genre.content, 'html.parser') #will parse HTML content
    genre_body = soup.body 
    voteCount = soup.findAll('p', attrs={'class' : 'sort-num_votes-visible'})
    for p in voteCount:
        results = p.text.replace(',', '').replace('"', '').replace('.', '').replace("'", "").replace('?', '').replace("\n", "").replace('\r', '').replace(" ","").replace("Votes:","")
        head, sep, tail = results.partition('|')
        all_votings.append(head)

    while scanContinue:
        genre = requests.get(f"https://www.imdb.com/search/title/?title_type=tv_series,tv_miniseries&genres={genre}&sort=num_votes,desc&start={page}&explore=gengenre&ref_=adv_nxt")
        soup = BeautifulSoup(genre.content, 'html.parser')
        genre_body = soup.body

        voteCount = soup.findAll('p', attrs={'class' : 'sort-num_votes-visible'})    
        for p in voteCount:
            results = p.text.replace(',', '').replace('"', '').replace('.', '').replace("'", "").replace('?', '').replace("\n", "").replace('\r', '').replace(" ","").replace("Votes:","")
            head, sep, tail = results.partition('|')
            almost, sep, tail = head.partition('G')
            all_votings.append(almost)

        page = int(page) + 50
        if page > 101:
            scanContinue = False
          
    finish = time.perf_counter()
    print(f"Voting Results found in: {start - finish:0.4f} seconds")
    intVote = list(map(int, all_votings))
    for i in intVote:
        intVotings.append(i)
    return(intVotings)