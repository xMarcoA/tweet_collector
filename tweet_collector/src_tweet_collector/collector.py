# imports
import os
import tweepy
import pymongo
import json
from dotenv import load_dotenv

# makes your twitter cursor  
def cursor_maker(query):
    cursor = tweepy.Cursor(
                api.search,
                q = query,
                tweet_mode = 'extended',
                lang='en')
    return cursor

# get the data with the cursor and give it back as a json file
def tweet_to_json(cursor,times):
    tweets = [json.dumps(status._json) for status in cursor.items(times)]
    jason = [json.loads(tweet) for tweet in tweets]
    return jason

# uploads the data into mongo
def uploader(list_json):
    db.col_tweets.insert_many(list_json)
    return None

# combine the previous functions 
def hole_service(thema,times):

    # get the twitter cursor
    cursor = cursor_maker(f'{thema} -filter:retweets')

    # get the raw tweets with the cursor and convert them into json
    json_list = tweet_to_json(cursor,times)

    # merge neg and pos list to one and rload it up to mongo
    uploader(json_list)
    return print("Your desired tweets stored in your Mongo Database")
  
# authentification
load_dotenv() 
auth = tweepy.OAuthHandler(os.getenv('consumer_key'), os.getenv('consumer_secret')) # Authentification
api = tweepy.API(auth)    # get the api script
print("You got access to twitter")

# cennect to mongo docker
client = pymongo.MongoClient("mongodb://mongo_db:27017/")    # "treiber://service_name:port/"
db = client.db_tweets               # create a database called db_tweets
print("and connected to Mongo now")






# enter thema and how many tweets you want
hole_service("corona",2)  


