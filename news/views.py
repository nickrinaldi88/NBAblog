from django.http.response import HttpResponseRedirect
from news import serializers
from news.serializers import PostSerializer, CreatePostSerializer
import os
import json
import requests
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from rest_framework import generics, status
from rest_framework.views import APIView
from rest_framework.response import Response
from news import twitter
from news import reddit
from news import red_praw
from .models import Post
from news import services
import sys
from .forms import PlayerStats
from .bball_refparser import main
from django.core.paginator import Paginator
from .tasks import sleepy

# Create your views here.

# create api view


def test(request):

    form = PlayerStats()

    if request.method == "POST":
        form = PlayerStats(request.POST)

        if form.is_valid():
            p1 = form.cleaned_data['Player1']
            s1 = form.cleaned_data['Season1']
            p2 = form.cleaned_data['Player2']
            s2 = form.cleaned_data['Season2']

            stats = main(p1, p2, s1, s2)

            return render(request, 'test.html', {"form": form, "p1_stats": stats[0], "p2_stats": stats[1]})

    else:
        form = form = PlayerStats()

  # call main with parameters

    # call function

    return render(request, 'test.html', {"form": form})


def mainpage(request):
    all_posts = Post.objects.all()
    context = {'posts': all_posts}
    return render(request, "mainpage.html", context)


def main(request):

    sys.path.insert(
        0, 'C:\\Users\\Nick\\Desktop\\2021 Python\\NBA_Project\\NBAblog\\news')

    here = os.path.dirname(os.path.abspath(__file__))
    all_posts = Post.objects.all()
    context = {'posts': all_posts, }

    return render(request, 'main.html', context)


def index(request):
    sleepy(10)
    return HttpResponse("Hello, world. You're at the main index.")


# def main_blog(request):

#     here = os.path.dirname(os.path.abspath(__file__))
#     filename = os.path.join(here, 'tweet_info.json')

#     f = open(filename)
#     data = json.load(f)

#     tweets = twitter.connect(data['consumer_key'], data['consumer_secret'],
#                              data['access_key'], data['access_secret'])

#     return render(request, 'blog.html', dict(tweets=tweets))
#   # arg for tweet url?
#     # do api requestS?

#     # will contain main blog feed


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
