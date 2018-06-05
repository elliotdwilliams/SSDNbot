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
  items = random.sample(result.items, 1)

  #print the id of the random item to the console - used for testing
  #print(items[0]["id"])

  #extract element from the record to use in tweet
  for item in items:
  #determine if description field is present, and compose tweety accordingly
    if "description" in item["sourceResource"]:
      url = "https://dp.la/item/" + item["id"]
      title = item["sourceResource"]["title"]
      title = str(title)[1:-1] #remove square brackets
      title = (title[:100] + '...\'') if len(title) > 100 else title
      
      description = item["sourceResource"]["description"]
      description = str(description)[1:-1] #remove square brackets
      description = (description[:130] + '...\'') if len(description) > 130 else description
      
      tweet_text = title + '\n' + description + '\n' + url
      
      #print(title)
      #print(description)
      
    else:
      url = "https://dp.la/item/" + item["id"]
      title = item["sourceResource"]["title"]
      title = str(title)[1:-1] #remove square brackets
      title = (title[:230] + '...') if len(title) > 230 else title
      tweet_text = "%s %s" % (title, url)
    
      #print(title)
	  
    print(tweet_text)
    api.update_status(tweet_text)

send_tweet()
