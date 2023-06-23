#amiralium or captainjelal

import tweepy
import time

# Authenticate with Twitter API
consumer_key = 'your_consumer_key'
consumer_secret = 'your_consumer_secret'
access_token = 'your_access_token'
access_token_secret = 'your_access_token_secret'
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

# Create API object
api = tweepy.API(auth)
 # Function to tweet
def tweet(message):
    try:
        api.update_status(message)
        print('Tweet sent successfully')
    except tweepy.TweepError as error:
        print('Error occurred while tweeting:', error)
 # Function to schedule tweets
def schedule_tweet(message, date_time):
    while True:
        now = time.strftime('%Y-%m-%d %H:%M:%S')
        if now == date_time:
            tweet(message)
            break
        time.sleep(1)
 # Tweet from command line
message = input('Enter your tweet: ')
tweet(message)
 # Schedule tweet
message = input('Enter your tweet: ')
date_time = input('Enter date and time in the format YYYY-MM-DD HH:MM:SS: ')
schedule_tweet(message, date_time)