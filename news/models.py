from enum import unique
from django.db import models
import json
import sys
# import tweets.py and reddit.py to do api calls

# do API calls, collect various data that fits model parameters

# Create your models here.


def red_connect():
    # reddit_login
    # mac reddit
    # red_datafile = "/Users/nick/Desktop/NBAblog-1/news/red_info.json"

    red_datafile = "C:\\Users\\Nick\\Desktop\\2021 Python\\NBA_Project\\NBAblog\\news\\red_info.json"
    red_f = open(red_datafile)
    red_data = json.load(red_f)

    red = services.reddit_connect(red_data['client_id'], red_data['client_secret'],
                                  red_data['username'], red_data['password'], red_data['user_agent'])  # will return reddit posts


def twit_connect():
     # twitter login

    sys.path.insert(
        0, 'C:\\Users\\Nick\\Desktop\\2021 Python\\NBA_Project\\NBAblog\\news')

    # sys.path.insert(
    # 0, '/Users/nick/Desktop/NBAblog-1/news')

    here = os.path.dirname(os.path.abspath(__file__))
    filename = os.path.join(here, 'tweet_info.json')

    tweet_f = open(filename)
    tweet_data = json.load(tweet_f)

    twit = services.tweet_connect(tweet_data['consumer_key'],
                                  tweet_data['consumer_secret'], tweet_data['access_key'], tweet_data['access_secret'])  # will return url's


class Post(models.Model):
    # Reddit, Twitter, Youtube
    post_type = models.CharField(
        max_length=20, null=True, blank=True)
    root_url = models.CharField(max_length=200, default="", unique=True)
    html = models.TextField(default="")
    created_at = models.DateTimeField(auto_now_add=True)


'''I need to learn how to integrate models with our api data'''
'''store api data in models'''

# class BlogPost(models.Model):
#     # Reddit, Twitter, Youtube, etc.
#     post_id = models.CharField(
#         max_length=250, null=True, blank=True, unique=True)
#     post_title = models.CharField(max_length=200, null=True, blank=True)
#     item_text = models.TextField()
#     published_date = models.DateTimeField(blank=True, null=True)

#     def __str__(self):
#         return self.post_title


# class Product(models.Model):
#     title = models.CharField(max_length=120),
#     description = models.TextField(blank=True, null=True),
#     price = models.DecimalField(decimal_places=2, max_digits=1000),
#     summary = models.TextField(blank=False, null=False)
#     featured = models.BooleanField()

# Create Tweet and Reddit posts as models, because they will be stored as DB info
