import praw
import tweepy
# from .models import Tweet
import requests
import webbrowser
import pprint
import json
import os
import sys

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

    return current_status # passes into the tweet_tags


# reddit

def reddit_connect(client_id, secret, username, password, user_agent):

    sub = 'nba'

    reddit = praw.Reddit(
        client_id=client_id,
        client_secret=secret,
        username=username,
        password=password,
        user_agent=user_agent)

    id_list = []
    # pprint.pprint(dir(reddit))

    for r in reddit.subreddit('nba').hot(limit=9):
        id_list.append(r.id)

    return id_list[2:] # eliminate the two pinned threads


red_datafile = "C:\\Users\\Nick\\Desktop\\2021 Python\\NBA_Project\\NBAblog\\news\\red_info.json"

red_f = open(red_datafile)
data = json.load(red_f)

reddit = praw.Reddit(
    client_id=data['client_id'],
    client_secret=data['client_secret'],
    username=data['username'],
    password=data['password'],
    user_agent=data['user_agent'])

submission = reddit.submission(id=)

title = submission.title
the_url = submission.url

print(submission)

sub_url = "https://www.reddit.com/r/nba"
