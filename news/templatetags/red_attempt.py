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
def red_attempt(url):  # what is passed into tweet_tags tho?
    """ Requests a tweet from oembed and returns the html element """

    # pprint.pprint(dir(item))
    # break
    endpoint = requests.get(
        f"https://www.reddit.com/oembed?url=https://www.reddit.com{url}")

    # endpoint_json = endpoint.json()
    return endpoint.json()


goal = red_attempt(
    '/r/nba/comments/n6l2zu/the_crew_lock_in_their_predictions_and_ernie_has/')

print(goal)
