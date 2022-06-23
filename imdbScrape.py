import requests
from bs4 import BeautifulSoup
import time
 

def getTop10ComediesX():
    print("Retrieving results...")
    start = time.perf_counter() #starts the counter to see how long results take
    all_titles = [] 
    title_ratings = []
    votes = []
    page = 51 
    scanContinue = True 

    res = requests.get("https://www.imdb.com/search/title/?title_type=movie&genres=sci-fi&sort=num_votes,desc&explore=title_type,genres") #the main page for the genre with votes in descending order
    soup = BeautifulSoup(res.content, 'html.parser') #will parse HTML content
    res_body = soup.body 
    content = soup.findAll('h3', attrs={'class' : 'lister-item-header'})
    for p in content:
        results = p.text.replace(',', '').replace('"', '').replace('.', '').replace("'", "").replace('?', '').replace("\n", "").replace('\r', '')
        all_titles.append(results)

    ratings = soup.findAll('div', attrs={'class' : 'inline-block ratings-imdb-rating'})
    for p in ratings:
        ratingsResults = p.text.replace(',', '').replace('"', '').replace("'", "").replace('?', '').replace("\n", "").replace('\r', '').replace(' ', '')
        title_ratings.append(ratingsResults)

    voteCount = soup.findAll('p', attrs={'class' : 'sort-num_votes-visible'})
    for p in voteCount:
        results = p.text.replace(',', '').replace('"', '').replace('.', '').replace("'", "").replace('?', '').replace("\n", "").replace('\r', '').replace(" ","").replace("Votes:","")
        head, sep, tail = results.partition('|')
        votes.append(head)

    while scanContinue:
        res = requests.get(f"https://www.imdb.com/search/title/?title_type=movie&genres=sci-fi&sort=num_votes,desc&start={page}&explore=title_type,genres&view=advanced")
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

        voteCount = soup.findAll('p', attrs={'class' : 'sort-num_votes-visible'})
        for p in voteCount:
            results = p.text.replace(',', '').replace('"', '').replace('.', '').replace("'", "").replace('?', '').replace("\n", "").replace('\r', '').replace(" ","").replace("Votes:","")
            head, sep, tail = results.partition('|')
            almost, sep, tail = head.partition('G')
            votes.append(almost)

        page = int(page) + 50
        if page > 1451:
            scanContinue = False
    
    intVote = list(map(int, votes))
    floatRating = list(map(float, title_ratings))

    combined = dict(zip(all_titles, zip(floatRating, intVote)))

    for key, values in combined.items():
        if values[1] > 50000 and values[1] < 80000:
            if values[0] >= 7.5:
                print(f"{key} : {values[0]}*rating with {values[1]} votes.")

    #for element in intVote:
       # if isinstance(element, int):
       #     print("It's an Integer")
      ##  if isinstance(element, str):
        #    print("It's a string")
     #   if isinstance(element, float):
      #      print("It's an floating number")
        
    finish = time.perf_counter()
    print(f"Results found in: {start - finish:0.4f} seconds")








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



def getTop10ComediesX2():
    print("Retrieving")
    res = requests.get("https://www.imdb.com/search/title/?title_type=movie&genres=adventure&sort=num_votes,desc&start=1051&explore=title_type,genres&ref_=adv_nxt")
    soup = BeautifulSoup(res.content, 'html.parser')
    res_body = soup.body
    voteCount = soup.findAll('p', attrs={'class' : 'sort-num_votes-visible'})
    for p in voteCount:
        results = p.text.replace(',', '').replace('"', '').replace('.', '').replace("'", "").replace('?', '').replace("\n", "").replace('\r', '').replace(" ","").replace("Votes:","")
        head, sep, tail = results.partition('|')
        print(head)

getTop10ComediesX()