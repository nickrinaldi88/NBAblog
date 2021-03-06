import praw
import tweepy
import requests
import webbrowser
import pprint
import json
import os
import sys
import datetime
from .models import Post

sources = {}

# twitter
sys.path.insert(
    0, 'C:\\Users\\Nick\\Desktop\\2021 Python\\NBA_Project\\NBAblog\\news')

# twitter mac

# sys.path.insert(
#     0, '/Users/nick/Desktop/NBAblog-1/news')

here = os.path.dirname(os.path.abspath(__file__))
filename = os.path.join(here, 'tweet_info.json')

tweet_f = open(filename)
tweet_data = json.load(tweet_f)

try:
    with open('twit_db.json') as json_file:
        db = json.load(json_file)
except:
    db = []


# connect to api 

def tweet_connect(key, secret, access_key, access_secret):

    auth = tweepy.OAuthHandler(key, secret)

    auth.set_access_token(access_key, access_secret)

    api = tweepy.API(auth, wait_on_rate_limit=True,
                     wait_on_rate_limit_notify=True)

    t_post_dict = {}

    # grab size count of tweets on home timeline

    my_timeline = api.home_timeline(count=50)

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
        # db.append(status.id)
        # t_post_dict[url] = str(status.created_at)
        # current_status.append(url)

    # return t_post_dict
    # return current_status


# generate list of tweet urls

tweet_result = tweet_connect(tweet_data['consumer_key'],
                             tweet_data['consumer_secret'], tweet_data['access_key'], tweet_data['access_secret'])



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

    for r in reddit.subreddit(sub).hot(limit=50):
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

red_f = open(red_datafile)
red_data = json.load(red_f)

# generate list of post id's

red_result = reddit_connect(red_data['client_id'], red_data['client_secret'],
                            red_data['username'], red_data['password'], red_data['user_agent'])


sources['twitter'] = tweet_result
sources['reddit'] = red_result

print(sources)

# print(date1)


# find difference between current time and values


# pprint.pprint(sources)
# print(date1)

# def connections():

#     time_assoc_dict = {}
#     times = []
#     src = []

#     for keys, value in sources.items():
#         for k, v in value.items():
#             time_posted = v
#             # find current time, # compare to time_posted. times[source] = time_difference
#             source = k
#             time_assoc_dict[source] = time_posted
#             times.append(time_posted)

#     for post in times:
#         newest_post = min(times)  # find the newest post
#         times.remove(newest_post)  # remove it from the list
#         for k, v in time_assoc_dict.items():
#             if newest_post == v:
#                 src.append(k)

#     src = src[::-1]

#     return src


# ans = connections()

# print(ans)

# sort times dict by shortest to longest
# post source based on time.


# on joke.html for item in srcs, if src starts with 'https' load tweet tag, else, load reddit tag
# pass in src as context
# print(min(times))


'''
Have services.py run everytime refresh button is hit. Populate Post objects with specific data
'''
