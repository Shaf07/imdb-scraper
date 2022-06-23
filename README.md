# imdb-scraper
This code will scrape out the titles of each movie and their rating and put them into a dictionary. 

Follow the URL in the code. It will take you to IMDB where a list of all movies can be seen by genre. To adapt it to whatever genre you pick, you will have to reenter the new url into the code. Also you will have to insert {page} where the page number would be in the url slightly further down. This is because the code exists in a while loop where after every scrape, the page number will increase (thus taking to you to the next page) to scrape the next set of movie titles. This loop will keep going until whatever limited you have set on the quantity of results you want (default is 100). 

By running the code as it is, you will get a list of rom com films sorted by their ratings put into a dictionary and then printed to the console.

I am working on making the code more universal and I am going to clean it up soon.
