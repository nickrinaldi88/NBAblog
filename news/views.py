import os
import json
import requests
from django.http import HttpResponse
from django.shortcuts import render
from news import twitter
from news import reddit

# Create your views here.


def index(request):
    return HttpResponse("Hello, world. You're at the main index.")


def main_blog(request):

    here = os.path.dirname(os.path.abspath(__file__))
    filename = os.path.join(here, 'tweet_info.json')

    f = open(filename)
    data = json.load(f)

    tweets = twitter.connect(data['consumer_key'], data['consumer_secret'],
                             data['access_key'], data['access_secret'])

    reddit_posts = reddit.generate(reddit.posts)

    # I want the api to add tweets to this list.

    # I want previous tweets to be added to an archive

    return render(request, 'blog.html', dict(tweets=tweets, reddit=reddit_posts))
  # arg for tweet url?
    # do api requestS?

    # will contain main blog feed


def test(request):
    return HttpResponse('YERRRR')


def detail(request):
    return HttpResponse("This is a single post")


def archive(request):
    return HttpResponse("Archive page")
    # will the page after a single post is clicked on

    # determine what pages I want


# LOOK UP HOW TO PASS IN CONTEXT
