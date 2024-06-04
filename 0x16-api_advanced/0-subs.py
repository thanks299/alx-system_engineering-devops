#!/usr/bin/python3
"""
A Script that queries subscribers on a given Reddit subreddit.
"""

import requests

def number_of_subscribers(subreddit):
    url = "https://www.reddit.com/r/programming/about.json"
    headers = {"User-Agent": "Your custom user agent here"}
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        data = response.json()
        return data["data"]["subscribers"]
    else:
        return 0
