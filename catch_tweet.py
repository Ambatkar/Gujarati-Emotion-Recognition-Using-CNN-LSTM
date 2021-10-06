import tweepy
import webbrowser
import time
import re
import Prediction
import sys

n = len(sys.argv)
print("Total arguments passed:", n)
if (n > 1):
    t_query = sys.argv[1]
    t_date = sys.argv[2]
else:
    t_query = 'Covid'
    t_date = '2021-06-28'
    
consumer_key = "Enter_Your_Consumer_key_Here"
consumer_secret = "Enter_Your_Secret_key_Here"
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(auth.access_token, auth.access_token_secret)
api = tweepy.API(auth)

search_words= t_query + " -filter:retweets"
date_since= t_date

tweets = tweepy.Cursor(api.search,
              q=search_words,
              lang="gu",
              since=date_since).items(10)
gu_tweets = [tweet.text for tweet in tweets]
#print(gu_tweets)
ask = []
for i in gu_tweets:
  i = re.sub(r"[a-zA-Z0-9://.@#.…,-_\n|]+", '', i)
  ask.append(i)
  
#print(ask)
Prediction.predicted(ask)
