import tweepy
import datetime
import csv

consumer_key="D5xNoFTpMAAsdEpT08ZSs1Wcj"
consumer_secret="xn3nmwcJEU6hfoH7NND8zX2aYbKwD3iEIQjlJFr6ouubWRNrJg"

access_token="925616599-u6yMmcLB3Ar9RZq80e0wUTCZjZp5TotXapkTOxyQ"
access_token_secret="E5DTEg4DGFmFGTKbCusko1tfjPgpWEvWLw68b6MCi64EB"

"""
search(hashtag)

Input:
hashtag - String that will be searched for.

Output:
Returns nothing, but writes search results in tweets.csv.
"""

def search(hashtag):
  auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
  auth.set_access_token(access_token, access_token_secret)

  api = tweepy.API(auth)
  
  result = api.search(q=hashtag, count = 15)

  with open('tweets.csv', 'wb') as csvfile:
      spamwriter = csv.writer(csvfile)
      for tweet in result:
        content = tweet.text.encode('utf-8').strip() + "<br><br>"
        #username = tweet.from_user
        time    = tweet.created_at
        #spamwriter.writerow((username, time, content))
        spamwriter.writerow((time,content))

#hashtag = raw_input("what hash do you want to search?\n")

#search(hashtag)
print 'Search Results Entered in tweets.csv'
