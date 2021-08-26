# To be used as a tool on django site

import requests
from bs4 import BeautifulSoup
import pandas as pd


# also adding some comments here

'''
TODO:
1. Write a web scraper and parse this page: https://www.basketball-reference.com/players/
    and save a list of players names in text doc
2. Create function that takes in player name and creates suffix

-Parse bball ref scraper to see how code works
-A levenshtein score is needed to find player names specifically

'''

'''
TODO:
Annotate BBall ref scraper scripts.
Utils - DONE

'''

# player_name = input("Please enter a player's name: ")
player_name = "lebron james"

# name = "bobby portis"


def main(p1, p2, s1, s2):

    # list to be returned containing both player stats

    player_stats = []

    # create suffixes

    p1_suf = create_suff(p1)
    p2_suf = create_suff(p2)

    # player 1 request

    link1 = f"https://www.basketball-reference.com/players/{p1_suf[1]}/{p1_suf[0]}01.html"

    response1 = requests.get(link1)

    if response1.status_code == 200:

        soup = BeautifulSoup(response1.content, 'html.parser')

        all_tables = soup.find_all('table')

    df1 = pd.read_html(str(all_tables[0]))[0]

    year_suf1 = str(int(s1))[-2:]

    season1 = str(int(s1)-1) + "-" + year_suf1

    p1_stats = df1.loc[df1['Season'] == season1]

    # player 2 request

    link2 = f"https://www.basketball-reference.com/players/{p2_suf[1]}/{p2_suf[0]}01.html"

    response2 = requests.get(link2)

    if response2.status_code == 200:

        soup = BeautifulSoup(response2.content, 'html.parser')

        all_tables = soup.find_all('table')

    df2 = pd.read_html(str(all_tables[0]))[0]

    year_suf2 = str(int(s2))[-2:]

    season2 = str(int(s2)-1) + "-" + year_suf2

    p2_stats = df2.loc[df2['Season'] == season2]

    # print(p1_stats)
    # print("----")
    # print(p2_stats)

    player_stats.append(p1_stats)
    player_stats.append(p2_stats)

    return player_stats


def create_suff(name):

    text = []

    list_names = name.split()

    # print(list_names)

    first_half = list_names[1][:5].lower()

    last_half = list_names[0][:2].lower()
    initial = list_names[1][0].lower()

    suffix = first_half + last_half

    text.append(suffix)
    text.append(initial)

    '''
    Creates suffix for nonexistent players
    '''
    return text


p_suf = create_suff(player_name)


def remove(name):
    '''
    Remove accents
    '''

    alphabet = set('abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXZY ')

    the_name = set(name)

    print(the_name)

    if len(set(name).difference(alphabet)) == 0:
        return name
    else:
        return "hi"


def test_request(player_suffix, s1):
    '''
    Input is a list of the players suffix[0] + initial[1]
    '''

    '''
    Make sure to add initial and suffix args

    # Steps for website
    # -Intake Player Name input
    # -Generate List of Seasons for each player onto screen
    # -Intake Season for each
    # -Generate initial and suffix, then make a request on each player's page
    # -Grab the table element for each page
    '''
    the_link = f"https://www.basketball-reference.com/players/{player_suffix[1]}/{player_suffix[0]}01.html"

    # parsed_link = "https://www.basketball-reference.com/players/t/tatumja01.html"

    response = requests.get(the_link)

    if response.status_code == 200:

        soup = BeautifulSoup(response.content, 'html.parser')

        all_tables = soup.find_all('table')

    df = pd.read_html(str(all_tables[0]))[0]

    # convert to dataframe

    # dfs = df[0]

    year_suf = str(int(s1) + 1)[-2:]

    season = s1 + "-" + year_suf

    print(df.loc[df['Season'] == season])

    # for row in df[0]['Season']:
    #     if str(row).startswith(s1):
    #         print(row)
    # value = df[0]['Season']
    # print row where Season columns starts with season in put
    # print(value)

    # link = f'https://www.basketball-reference.com/players/{initial}/{suffix}01.html'


# test_request(p_suf, '2020')

# test_request()
