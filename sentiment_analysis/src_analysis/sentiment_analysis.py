# imort tools and libaries
import pandas as pd 
import pymongo
from sqlalchemy import create_engine
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer

# function to give the sentiment key with the highest probability back
def max_calc(dictionarie):
    del dictionarie['compound']
    sort = sorted(dictionarie, key=dictionarie.get, reverse=True)
    return sort[0]

# connection to mongo and postgres
client = pymongo.MongoClient("mongodb://mongo_db:27017/")
engine = create_engine("postgresql://marco:affffen10@postgres_sql:5432/analysis_results_d") # treiber://username:password@host:port/dbname""
print("You are connected to your databases (mongo,postges)")

# get Data from mongo 
mongo_data = client.db_tweets.col_tweets.find() 
print("and imported succesfully the Mongo Datas")

# Transform Data into a df
trans_data = {'text':[], 'time':[]}
for element in mongo_data:
    trans_data['text'].append(element['full_text'])
    trans_data['time'].append(element['created_at'])
dataframe = pd.DataFrame(trans_data) 
print("Tweets stored in a Dataframe")        

# label the data with vaderSentiment
text_col = dataframe['text']


senti  = SentimentIntensityAnalyzer()
sentiments = []
for text in text_col:
    sentiment = senti.polarity_scores(text)
    max_sen = max_calc(sentiment)
    sentiments.append(f'{max_sen} {sentiment[max_sen]}' )
dataframe['sentiment'] = sentiments
                   
print("Your tweets are labeled")

#upload to postgres
dataframe.to_sql('tweets', engine, if_exists='replace', index=False) # df.to_sql('NameOfTabelWichWillBeCreated', engine, ...)
print('and loaded into your analysis_results_d Database (sql).')

# why the programm runs through with out any problems but shows my warnings in logs?