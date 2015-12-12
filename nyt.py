import csv
import urllib2
import json,sys

nyt_api_key = "&api-key=e1d08e31fabebf4e6b531b2ee8b4b922:9:73464677"
url_init = "http://api.nytimes.com/svc/search/v2/articlesearch.json?q="

"""
search(topic)

Input:
topic - String that will be searched for.

Output:
Returns nothing, but writes search results in articles.csv.
"""

def search(topic):
    contyn = True
    for num in range(len(topic)):
        if(topic[num]==" "):
            search(topic[0:num]+"%20"+topic[num+1:len(topic)])
            contyn = False
    if(contyn==True):
        url = url_init+topic+nyt_api_key
        request = urllib2.urlopen(url)
        result = request.read()
        r = json.loads(result)
        s = r['response']
        t = s['docs']
        with open('articles.csv','wb') as csvfile:
            spamwriter = csv.writer(csvfile)
            for entry in t:
                excerpt = (entry['snippet']+"<br>").encode('utf-8')
                theurl = (entry['web_url']+"<br><br>").encode('utf-8')
                spamwriter.writerow((excerpt,theurl))
                print 'Search Results Entered in articles.csv'
