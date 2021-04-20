import requests
from django import template

register = template.Library()


# loaded into our blog.html

the_url = "https://twitter.com/NBABeau/status/1381729991067635713"


def tweet_tags(url):  # what is passed into tweet_tags tho?
    """ Requests a tweet from oembed and returns the html element """

    tweet_request = requests.get(
        'https://publish.twitter.com/oembed?url=' + url + '&omit_script=true')
    tweet_json = tweet_request.json()
    
    tweet_html = tweet_json['html']
    print(tweet_html)
    print(type(tweet_html))

    return tweet_html  # returns to our template


result = tweet_tags(the_url)

print(result)
# 1. grab a url
# 2. pass it into our tweet_tags function
# 3. Take the result and render into our view through context
# 4. for loop in the template to constanly generate
