import requests


def test_get():

    url = 'https://twitter.com/minakimes/status/1379945821022474240'

    tweet_request = requests.get(
        'https://publish.twitter.com/oembed?url=' + url + '&omit_script=true')
    tweet_json = tweet_request.json()
    return tweet_json


# parsing a request response
