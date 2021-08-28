import praw
import tweepy
# from .models import Tweet
import requests
import webbrowser
import pprint
import json
import os
import sys

sys.path.insert(
    0, 'C:\\Users\\Nick\\Desktop\\2021 Python\\NBA_Project\\NBAblog\\news')

here = os.path.dirname(os.path.abspath(__file__))
filename = os.path.join(here, 'tweet_info.json')

f = open(filename)
data = json.load(f)

try:
    with open('twit_db.json') as json_file:
        db = json.load(json_file)
except:
    db = []


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
        print(status.created_at)
        break

    # for status in my_timeline:
    #     if status.id not in db:
    #         db.append(status.id)
    #         url = default + str(status.id)
    #         current_status.append(url)

    # return current_status # returns a list containing urls to our view
    # pass this list into our context
    # our template parses the contents of the context in a loop
    # passes in argument to tweet_tag argument which generates html

    # find tweet_id, store in local cache db
result = connect(data['consumer_key'], data['consumer_secret'],
                 data['access_key'], data['access_secret'])

with open('twit_db.json', 'w') as outfile:
    json.dump(db, outfile, indent=2)
