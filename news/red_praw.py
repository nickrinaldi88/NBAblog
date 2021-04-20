import praw
import os
import sys
import json
import pprint



here = os.path.dirname(os.path.abspath(__file__))
filename = os.path.join(here, 'red_info.json')
f = open(filename)
data = json.load(f)


def connect(client_id, secret, username, password, user_agent):

    sub = 'nba'

    reddit = praw.Reddit(
        client_id = client_id,
        client_secret=secret,
        username=username,
        password=password,
        user_agent=user_agent)

    id_list = []
    # pprint.pprint(dir(reddit))

    for r in reddit.subreddit('nba').hot(limit=9):
        id_list.append(r.id)

    return id_list[2:]
            

    


    # for r in reddit.subreddit('nba').hot(limit=7):
    #     if not r.stickied:

    #         print(r.url) # grab 5 hottest posts
    #                                     # return the url 
    #         print(r.title)
    #         print(r.id)
    #         # pprint.pprint(dir(r))
    #         id_list.append(r.id)

    # print(id_list)

    

connect(data['client_id'], data['client_secret'], data['username'], data['password'], data['user_agent'])