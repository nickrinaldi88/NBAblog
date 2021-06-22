import requests
from django import template
import pprint
import praw
import os
import sys
import json

register = template.Library()


@register.simple_tag
def reddit_tag_test(the_id):

    file = "C:\\Users\\Nick\\Desktop\\2021 Python\\NBA_Project\\NBAblog\\news\\red_info.json"
    # mac file
    # file = "/Users/nick/Desktop/NBAblog-1/news/red_info.json"

    f = open(file)
    data = json.load(f)

    reddit = praw.Reddit(
        client_id=data['client_id'],
        client_secret=data['client_secret'],
        username=data['username'],
        password=data['password'],
        user_agent=data['user_agent'])

    submission = reddit.submission(id=the_id)
    title = submission.title
    the_url = submission.url

    sub_url = "https://www.reddit.com/r/nba"

    the_html = f"<blockquote class='reddit-card' data-card-created='1490648549'> <a href={the_url}>{title}</a> from <a href={sub_url}>nba</a></blockquote>"
    print(sub_url)

    return the_html
