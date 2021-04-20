import os
import json
import requests
from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
from news import twitter
from news import reddit
from news import red_praw
from .models import BlogPost
from .forms import BlogPostForm

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

    return render(request, 'blog.html', dict(tweets=tweets))
  # arg for tweet url?
    # do api requestS?

    # will contain main blog feed


def test(request, my_id):
    # obj = BlogPost.objects.get(id=my_id)
    obj = get_object_or_404(BlogPost, id=my_id)

    my_context = {
        "object": obj
    }

    return render(request, 'test.html', my_context)


def detail(request):
    return HttpResponse("This is a single post")


def blog_post_view(request):
    obj = BlogPost.objects.get(id=1)

    context = {
        'object': obj
    }

    # context = {
    #     "title": obj.post_title,
    #     "text": obj.item_text

    # }
    return render(request, "blogpost/blog_post_test.html", context)


def archive(request):
    return HttpResponse("Archive page")
    # will the page after a single post is clicked on


def joke(request):

    here = os.path.dirname(os.path.abspath(__file__))
    filename = os.path.join(here, 'red_info.json')

    f = open(filename)
    data = json.load(f)

    id_list = red_praw.connect(data['client_id'], data['client_secret'],
                               data['username'], data['password'], data['user_agent'])
    # items
    return render(request, 'joke.html', dict(id_list=id_list))
    # determine what pages I want


# LOOK UP HOW TO PASS IN CONTEXT
