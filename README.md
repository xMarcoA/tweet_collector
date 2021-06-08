tweet collector is a program with a data pippeline that collect tweets and stores them in a database. Next, the sentiment of tweets is analyzed and the annotated tweets are stored in a second database. Finally, the best or worst sentiment for a given is published on Slack.

tweet_collector.py :
 - scrapes tweets from twitter 
 - upload data into mongo db
 
 sentiment_analysis.py :
 - download data from mongo db
 - analyze tweet with vaderSentiment package
 - upload data into sql db
 
 slack_bot.py :
 - download data from sql db
 - post tweet on slack channel
 