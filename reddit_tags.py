import requests
from django import template
import pprint

register = template.Library()


@register.simple_tag
def reddit_tags():
    sub = 'nba'

    reddit_request = requests.get(
        f'https://www.reddit.com/r/{sub}.json', headers={'User-agent': 'your bot 0.1'})

    title = reddit_request.json()['data']['children'][0]['data']['title']
    the_url = reddit_request.json()['data']['children'][0]['data']['url']
    sub_url = "https://www.reddit.com/r/nba"

    # take parameters above, pass into string, return that string

    the_html = f"<blockquote class='reddit-card' data-card-created='1490648549'> <a href={the_url}>{title}</a> from <a href={sub_url}>nba</a></blockquote>"

    return the_html


reddit_tags()
