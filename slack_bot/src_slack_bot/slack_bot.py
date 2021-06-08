# imports
import os
import requests
import pandas as pd
from dotenv import load_dotenv
from sqlalchemy import create_engine

# function to desgin the post 
def post_designer(time_tweet, text_tweet, sentiment_tweet):
    data = {
        "blocks": [
            {
                "type": "header",
                "text": {
                    "type": "plain_text",
                    "text": time_tweet,
                }
            },
            {
                "type": "section",
                "text": {
                    "type": "mrkdwn",
                    "text": text_tweet
                }
            },
            {
                "type": "section",
                "text": {
                    "type": "mrkdwn",
                    "text": sentiment_tweet
                }
            }
        ]
    }
    return data

# import data from sql 
engine = create_engine("postgresql://marco:affffen10@postgres_sql:5432/analysis_results_d")
query = "SELECT * FROM tweets;"
tweeties = pd.read_sql(query, engine)

# load the url_code
load_dotenv()
url_code = os.getenv('web_hook')

# make the post
for pos in range(len(tweeties)):
    text_tweet = f"{tweeties['text'][pos]}"
    time_tweet = f"{tweeties['time'][pos]}"
    sentiment_tweet = f"{tweeties['sentiment'][pos]}"
    post = post_designer(time_tweet, text_tweet, sentiment_tweet)
    requests.post(url=url_code, json = post)

# to see if everything is fine
if len(tweeties) == 1:
    print(" I've made a post for you")
else: 
    print(f"I made {len(tweeties)} posts for you")






