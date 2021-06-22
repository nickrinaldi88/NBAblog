from news import serializers
from news.serializers import PostSerializer, CreatePostSerializer
import os
import json
import requests
from django.http import HttpResponse
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

# Create your views here.

# create api view


class PostView(generics.CreateAPIView):
    queryset = Post.objects.all()  # all objects (all posts?) We want all the posts
    serializer_class = PostSerializer  # should return json response


class CreatePostView(APIView):
    serializer_class = CreatePostSerializer

    def post(self, request, format=None):
        # if our user doesn't have an active session with our server, create one
        if not self.request.session.exists(self.request.session.session_key):
            self.request.session.create()

        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():  # if our fields in CreatePostSerializer are valid or received,
            post_type = serializer.data.post_type
            root_url = serializer.data.root_url
            html = serializer.data.html
            created_at = serializer.data.created_at
            user_sesh = self.request.session.session_key

        return PostSerializer


def main(request):

    # reddit_login
    # mac reddit
    # red_datafile = "/Users/nick/Desktop/NBAblog-1/news/red_info.json"

    red_datafile = "C:\\Users\\Nick\\Desktop\\2021 Python\\NBA_Project\\NBAblog\\news\\red_info.json"
    red_f = open(red_datafile)
    red_data = json.load(red_f)

    red = services.reddit_connect(red_data['client_id'], red_data['client_secret'],
                                  red_data['username'], red_data['password'], red_data['user_agent'])
    # twitter login

    sys.path.insert(
        0, 'C:\\Users\\Nick\\Desktop\\2021 Python\\NBA_Project\\NBAblog\\news')

    # sys.path.insert(
    # 0, '/Users/nick/Desktop/NBAblog-1/news')

    here = os.path.dirname(os.path.abspath(__file__))
    filename = os.path.join(here, 'tweet_info.json')

    tweet_f = open(filename)
    tweet_data = json.load(tweet_f)

    twit = services.tweet_connect(tweet_data['consumer_key'],
                                  tweet_data['consumer_secret'], tweet_data['access_key'], tweet_data['access_secret'])

    return render(request, 'main.html', {'reddit': red, 'twitter': twit})


def index(request):
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
    all_posts = Post.objects.all()
    context = {'posts': all_posts}
    return render(request, "test.html", context)
