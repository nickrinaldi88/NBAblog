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

name = "bobby portis"


def create_suff(name):
    '''
    Creates suffix for nonexistent players
    '''
    pass


def get_suff(name):
    initial = name.split(' ')[1][0].lower()

    print(initial)


# get_suff(name)

def remove(name):

    alphabet = set('abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXZY ')

    the_name = set(name)

    print(the_name)

    if len(set(name).difference(alphabet)) == 0:
        return name
    else:
        return "hi"


def test_request():
    '''
    Make sure to add initial and suffix args

    # Steps for website
    # -Intake Player Name input
    # -Generate List of Seasons for each player onto screen
    # -Intake Season for each
    # -Generate initial and suffix, then make a request on each player's page
    # -Grab the table element for each page 
    '''

    parsed_link = "https://www.basketball-reference.com/players/t/tatumja01.html"

    response = requests.get(parsed_link)

    if response.status_code == 200:

        soup = BeautifulSoup(response.content, 'html.parser')

        all_tables = soup.find_all('table')

    df = pd.read_html(str(all_tables[0]))

    print(df)

    # link = f'https://www.basketball-reference.com/players/{initial}/{suffix}01.html'


test_request()


'''
6/30/21:
-Refer to bball ref github code to implant correct season for player
-Or create player match function
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
