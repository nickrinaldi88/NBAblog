import praw
import tweepy
# from .models import Tweet
import requests
import webbrowser
import pprint
import json
import os
import sys

here = os.path.dirname(os.path.abspath(__file__))
filename = os.path.join(here, 'tweet_info.json')

f = open(filename)
data = json.load(f)


def connect(key, secret, access_key, access_secret):

    auth = tweepy.OAuthHandler(key, secret)

    auth.set_access_token(access_key, access_secret)

    api = tweepy.API(auth, wait_on_rate_limit=True,
                     wait_on_rate_limit_notify=True)

    # pprint.pprint(dir(api))
    my_timeline = api.home_timeline(count=5)

    current_status = []

    default = 'https://twitter.com/twitter/statuses/'

    for status in my_timeline:
        print(status.id)
        url = default + str(status.id)

        current_status.append(url)

    return current_status

    # find tweet_id, store in local cache db 


result = connect(data['consumer_key'], data['consumer_secret'],
                 data['access_key'], data['access_secret'])

print(result)
