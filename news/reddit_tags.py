import requests
from django import template
import pprint

register = template.Library()


# @register.reddit_tag
def reddit_tags():
    sub = 'nba'

    reddit_request = requests.get(
        f'https://www.reddit.com/r/{sub}.json', headers={'User-agent': 'your bot 0.1'})

    print(reddit_request.url)


reddit_tags()
