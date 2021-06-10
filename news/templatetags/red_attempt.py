import requests
from django import template
import pprint
import praw
import os
import sys
import json

register = template.Library()

# loaded into our blog.html


@register.simple_tag
def red_attempt(url):  
    """ Requests a tweet from oembed and returns the html element """

    headers = {
        'User-Agent': 'nba_comp app',
        'From': 'nickiscool88',
        'Accept': 'application/json'  
    }

    endpoint = requests.get(
        f"https://www.reddit.com/oembed?url=https://www.reddit.com{url}", headers=headers)

    return endpoint.json()['html']

# todo
# I keep getting a 429 error. It's because I'm sending too many requests. A 200 code is the one I want. That's a successful code
# read stack overflow page, might have to pass in endpoint.text to be loaded as a json

# so im passing a url into the view
