import json
import requests
import pprint

sub = 'nba'

response = requests.get(
    f'https://www.reddit.com/r/{sub}.json', headers={'User-agent': 'your bot 0.1'})


try:
    with open('red_db.json') as json_file:
        db = json.load(json_file)
except:
    db = []

posts = response.json()['data']['children']


def generate(posts):

    post_url = posts[0]['data']['url']
    sub_url = f"http: // www.reddit.com/r/{sub}"
    title = posts[0]['data']['title']
    # time_stamp = post[0]['data']['created']

    items = [post_url, sub_url, title]
    return items


# check post['data']['created'] timestamp, check whether or not post was created in the last minute, display it.

# grab subreddit url
# grab url
# grab title
# grab timestamps

# create similar script to tweet_tags.py
