
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time

def scrapeID(genre):
    options = Options()
    options.add_argument("start-minimized")
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
    urls = []
    page = 51 
    scanContinue = True
    start = time.perf_counter()
    driver.get(f"https://www.imdb.com/search/title/?title_type=tv_series,tv_miniseries&genres={genre}&sort=num_votes,desc&explore=genres")
    links = driver.find_elements_by_xpath("//*[@class='loadlate']")
    for link in links:
        url = link.get_attribute('data-tconst')
        if '|' in url:
            urls.append(url.split('|')[1])  # saves in a list only the numbers you want i.e. 55.68799,12.596316
        print(url)
    print(urls)
    while scanContinue:
            driver.get(f"https://www.imdb.com/search/title/?title_type=tv_series,tv_miniseries&genres={genre}&sort=num_votes,desc&start={page}&explore=gengenre&ref_=adv_nxt")
            links = driver.find_elements_by_xpath("//*[@class='loadlate']")
            for link in links:
                url = link.get_attribute('data-tconst')
                if '|' in url:
                    urls.append(url.split('|')[1])  # saves in a list only the numbers you want i.e. 55.68799,12.596316
                print(url)
            print(urls)
            page = int(page) + 50
            if page > 1001:
                scanContinue = False
            print("NEXT PAGE")
    finish = time.perf_counter()
    print(f"Results found in: {start - finish:0.4f} seconds")
    print(urls)
        


scrapeID('comedy')



