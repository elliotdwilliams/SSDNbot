import tweepy, random, time
from dpla.api import DPLA 
from credentials import *

#authenticate with Twitter api using credentials.py
auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_KEY, ACCESS_SECRET)
api = tweepy.API(auth)

#create DPLA object using dpla module and your API key
dpla = DPLA(DPLA_KEY)

def send_tweet():
  #create results set of all DPLA items where provider is SSDN 
  #result set is limited to 500 results, per DPLA API rules
  fields = {"provider" : "Sunshine State Digital Network"}
  result = dpla.search(searchFields=fields, page_size=10)

  #get random item from the results
  item = random.sample(result.items, 1)

  #print the id of the random item to the console - used for testing
  #print item[0]["id"]

  #extract elements from the record to use in tweet
  url = "https://dp.la/item/" + item[0]["id"]
  title = item[0]["sourceResource"]["title"]
  title = str(title)[2:-1] #remove square brackets and 'u'
  tweet_text = "%s %s" % (title, url)

  print tweet_text
  #api.update_status(tweet_text)
  
send_tweet()

#while True:
#  send_tweet()
#  print 'hi'
#  time.sleep(10)