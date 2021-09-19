# module load

import praw
import tweepy
import requests
import webbrowser
import pprint
import json
import time
import os
import sys
import datetime
from celery import shared_task
from .models import Post



# twitter
sys.path.insert(
    0, 'C:\\Users\\Nick\\Desktop\\2021 Python\\NBA_Project\\NBAblog\\news')


here = os.path.dirname(os.path.abspath(__file__))


# celery instance

@shared_task
def sleepy(duration):
    time.sleep(duration)
    return None

# connect to api


def tweet_connect(key, secret, access_key, access_secret):

    auth = tweepy.OAuthHandler(key, secret)

    auth.set_access_token(access_key, access_secret)

    api = tweepy.API(auth, wait_on_rate_limit=True,
                     wait_on_rate_limit_notify=True)

    t_post_dict = {}

    # grab size count of tweets on home timeline

    my_timeline = api.home_timeline(count=10)

    current_status = []

    default = 'https://twitter.com/twitter/statuses/'

    # grab raw html of each tweet in timeline

    for status in my_timeline:
        url = default + str(status.id)
        tweet_request = requests.get(
            'https://publish.twitter.com/oembed?url=' + url + '&omit_script=true')
        tweet_json = tweet_request.json()
        tweet_html = tweet_json['html']

        # create Post object with extracted tweet data

        Post.objects.create(post_type='Twitter', root_url=url,
                            html=tweet_html)

# reddit


def reddit_connect(client_id, secret, username, password, user_agent):

    sub = 'nba'

    r_post_dict = {}

    reddit = praw.Reddit(
        client_id=client_id,
        client_secret=secret,
        username=username,
        password=password,
        user_agent=user_agent)

    id_list = []
    url_list = []

    for r in reddit.subreddit(sub).hot(limit=10):
        url = r.permalink
        headers = {
            'User-Agent': 'nba_comp app',
            'From': 'nickiscool88',
            'Accept': 'application/json'
        }

        endpoint = requests.get(
            f"https://www.reddit.com/oembed?url=https://www.reddit.com{url}", headers=headers)
        the_html = endpoint.json()['html']

        Post.objects.create(post_type='Reddit',
                            root_url=f"www.reddit.com{url}", html=the_html)


# client_id and secret

red_datafile = "C:\\Users\\Nick\\Desktop\\2021 Python\\NBA_Project\\NBAblog\\news\\red_info.json"


##################### Mac reddit #######################

# red_datafile = "/Users/nick/Desktop/NBAblog-1/news/red_info.json"

'''
Have services.py run everytime refresh button is hit. Populate Post objects with specific data
'''
