# To be used as a tool on django site

import requests
from bs4 import BeautifulSoup
import pandas as pd


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


p1 = input("Enter player 1's name: ")  # first input box
p2 = input("Enter player 2's name: ")  # second input box


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


def test_request(player_suffix):
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

    df = pd.read_html(str(all_tables[0]))

    print(df)

    # link = f'https://www.basketball-reference.com/players/{initial}/{suffix}01.html'


test_request(p_suf)

# test_request()


'''
6/30/21:
-Refer to bball ref github code to implant correct season for player
-Or create player match function
'''

'''
7/7/21
-Create a gui to simulate what I want, 
then implement on website
'''


# Normalize name string


# Create options that user can select with drop down


# seasons = []


# year = 2020
# # year = 2021

# url = "https://www.basketball-reference.com/leagues/NBA_{}_per_game.html".format(
#     year)

# # store webpage in variable

# html = urlopen(url)

# # convert webpage to soup object

# soup = BeautifulSoup(html)

# # print(soup)


# headers = [th.getText() for th in soup.findAll('tr', limit=2)[0].findAll('th')]

# # exclude first column
# headers = headers[1:]

# rows = soup.findAll('tr')[1:]

# player_stats = [[td.getText() for td in rows[i].findAll('td')]
#                 for i in range(len(rows))]

# stats = pd.DataFrame(player_stats, columns=headers)

# # print(headers)
# # print(stats.head(10))

# # print(stats['Player'][0])

# names = ["Zach Lavine", "Brandon Ingram", "Jayson Tatum", "Jaylen Brown"]

# # print(stats[stats['Player'].str.contains(name)])

# for name in names:
#     if stats['Player'].str.contains(name):
#         print(name)


# rook_url = "https://www.basketball-reference.com/leagues/NBA_2021_rookies-season-stats.html"

# rook_html = urlopen(rook_url)

# rook_soup = BeautifulSoup(rook_html)

# r_headers = [th.getText() for th in rook_soup.findAll('tr', limit=2)[1].findAll('th')]

# r_headers = r_headers[1]
# print(r_headers)

# r_rows = soup.findAll('tr')[1:]

# print(r_rows)

# player_names = [[td.getText() for td in ]]

# extract nba rookie names
