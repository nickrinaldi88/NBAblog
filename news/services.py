import praw
import tweepy
# from .models import Tweet
import requests
import webbrowser
import pprint
import json
import os
import sys

sources = {}

# twitter
sys.path.insert(
    0, 'C:\\Users\\Nick\\Desktop\\2021 Python\\NBA_Project\\NBAblog\\news')

here = os.path.dirname(os.path.abspath(__file__))
filename = os.path.join(here, 'tweet_info.json')

tweet_f = open(filename)
tweet_data = json.load(tweet_f)

try:
    with open('twit_db.json') as json_file:
        db = json.load(json_file)
except:
    db = []


def tweet_connect(key, secret, access_key, access_secret):

    auth = tweepy.OAuthHandler(key, secret)

    auth.set_access_token(access_key, access_secret)

    api = tweepy.API(auth, wait_on_rate_limit=True,
                     wait_on_rate_limit_notify=True)

    # pprint.pprint(dir(api))
    my_timeline = api.home_timeline(count=5)

    current_status = []

    default = 'https://twitter.com/twitter/statuses/'

    for status in my_timeline:
        if status.id not in db:
            db.append(status.id)
            url = default + str(status.id)
            current_status.append(url)

    return current_status  # passes into the tweet_tags


tweet_result = tweet_connect(tweet_data['consumer_key'],
                             tweet_data['consumer_secret'], tweet_data['access_key'], tweet_data['access_secret'])


# reddit

def reddit_connect(client_id, secret, username, password, user_agent):

    # the sub

    sub = 'nba'

    # connection instance
    reddit = praw.Reddit(
        client_id=client_id,
        client_secret=secret,
        username=username,
        password=password,
        user_agent=user_agent)

    # list of id's
    id_list = []
    # pprint.pprint(dir(reddit))

    # appending id's
    for r in reddit.subreddit('nba').hot(limit=9):
        id_list.append(r.id)

    return id_list[2:]  # eliminate the two pinned threads


# client_id and secret

red_datafile = "C:\\Users\\Nick\\Desktop\\2021 Python\\NBA_Project\\NBAblog\\news\\red_info.json"

red_f = open(red_datafile)
red_data = json.load(red_f)

red_result = reddit_connect(red_data['client_id'], red_data['client_secret'],
                            red_data['username'], red_data['password'], red_data['user_agent'])


sources['twitter'] = tweet_result
sources['reddit'] = red_result

print(sources)
