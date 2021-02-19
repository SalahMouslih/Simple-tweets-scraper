from bs4 import BeautifulSoup
import requests
import json

# a scrapper needs The URL, RESPONSE & CONTENT

# The URL is simply a string that contains the address of the HTML page we intend to scrape.
# The RESPONSE is the result of a GET request. We’ll actually use the URL variable in the GET request here.
# CONTENT is the content of the response. If we print the entire response content, we’ll get all the content on the entire page of the url we’ve requested.

url = 'http://ethans_fake_twitter_site.surge.sh/'
response = requests.get(url, timeout=5)
content = BeautifulSoup(response.content, "html.parser")

tweetArr = []
for tweet in content.findAll('div', attrs={"class": "tweetcontainer"}):
    tweetObject = {
        "author": tweet.find('h2', attrs={"class": "author"}).text.encode('utf-8'),
        "date": tweet.find('h5', attrs={"class": "dateTime"}).text.encode('utf-8'),
        "tweet": tweet.find('p', attrs={"class": "content"}).text.encode('utf-8'),
        "likes": tweet.find('p', attrs={"class": "likes"}).text.encode('utf-8'),
        "shares": tweet.find('p', attrs={"class": "shares"}).text.encode('utf-8')
    }
    tweetArr.append(tweetObject)
with open('twitterData.json', 'w') as outfile:
    json.dump(tweetArr, outfile)


# parsing json file
import json
with open('twitterData.json') as json_data:
    jsonData = json.load(json_data)

# Now, we can use the variable jsonData. This should contain all of the information we scraped, but in JSON format. Let’s start with something simple, printing all of the dates of all the tweets:

for i in jsonData:
    print (i['date'])