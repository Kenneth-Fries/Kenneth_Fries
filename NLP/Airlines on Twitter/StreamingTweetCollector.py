# Twitter Scraper
#Kenneth Fries 11-20-18
#Metis Data Science
#This program was written to operate on AWS to serve as a constant collector of tweets.


from pymongo import MongoClient
from tweepy import Stream
import tweepy
from tweepy.streaming import StreamListener
from textblob import TextBlob
import json
import cnfg
client = MongoClient('localhost', 27017)

# Connect to the database for the first time
airlines = client['airline_database']

# Create a collection
tweet_collection = airlines.tweets


#setting the twitter api
config = cnfg.load(".twitter.config")
auth = tweepy.OAuthHandler(config["consumer_key"],
                           config["consumer_secret"])
auth.set_access_token(config["access_token"],
                      config["access_token_secret"])
api=tweepy.API(auth)


class listener(StreamListener):

    def on_data(self, data):
        data = json.loads(data)
        tweetnum = 0
        # Pull the fields we want, and insert it into our mongodb database
        #first filter out any non english tweets.
        if data['lang'] == 'en':
            tweet_document = {}
            tweet_document['created_at'] = data['created_at']
            tweet_document['favorite_count'] = data['favorite_count']
            tweet_document['retweet_count'] = data['retweet_count']

            #Get full text if it is an extended tweet
            if 'extended_tweet' in data.keys():
                tweet_document['text'] = data['extended_tweet']['full_text']
            else:
                tweet_document['text'] = data['text']

            tweet_document['screen_name'] = data['user']['screen_name']

            #Text Sentiment
            text = TextBlob(tweet_document['text']).sentiment #I later found Vader to be more useful.
            tweet_document['sentiment'] = text.polarity
            tweet_document['subjectivity'] = text.subjectivity


            tweet_collection.insert_one(tweet_document)
            tweetnum +=1
            print(tweet_collection.count())
            
            #useing this limit to allow the program to run a very long time, but not forever.  
        if tweet_collection.count() < 1000000:
            return True
        else:
            return False

    def on_error(self, status):
        print(status)


twitterStream = Stream(auth, listener())
data = twitterStream.filter(track=['@AmericanAir', '@Delta', '@USAirways', '@united', '@AlaskaAir', '@VirginAmerica', '@SouthwestAir', '@JetBlue',
                                   'American Airlines', 'Delta', 'US Air', 'United Airlines', 'Alaska Airlines', 'Virgin America', 'Southwest Air', 'Jet Blue'])
