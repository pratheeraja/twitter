import tweepy
import sys
import os

arguments = sys.argv

repo = ' '.join(arguments)[11:160]




CONSUMER_KEY = 'Enter ur consumer key'
CONSUMER_SECRET = '#'
ACCESS_TOKEN = '#'
ACCESS_TOKEN_SECRET = '#'

auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_TOKEN, ACCESS_TOKEN_SECRET)
api = tweepy.API(auth)

status = repo
api.update_status(status=status)
