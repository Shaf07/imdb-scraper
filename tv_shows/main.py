import requests
from bs4 import BeautifulSoup
import time
import csv

from tvshow import getTVShows
from tvshowrating import getTVRatings
from tvshowvotings import getVotesTV
import pandas as pd

#tvDictionary = {}
#intVotings = []
#all_titles = []
#floatRating = []
def tvDict(genre):
    all_titles = getTVShows(genre)
    intVotings = getVotesTV(genre)
    floatRatings = getTVRatings(genre)
    #tvDictionary = {f'{getTVShows(genre)}' : [], 'floatRatings' : [getTVRatings(genre)], 'intVotings' : [getVotesTV(genre)]}
    #tvDictionary = {dict(zip(all_titles,zip(floatRatings, intVotings)))}
    #print(tvDictionary)
    #with open('tvshow.csv', "w") as f:
       # writer = csv.writer(f)
       # for row in rows:
       #     writer.writerow(row)
    df = pd.DataFrame(list(zip(*[all_titles, floatRatings, intVotings]))).add_prefix('Col')

    df.to_csv('file.csv', index=False)

    print(df)



tvDict('comedy')
