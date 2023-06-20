#!/usr/bin/python3
"""
   Module that defines an API query
"""
import requests
headers = {"User-Agent": "ubuntu:hbtn:v1.0 (by /u/piroli_)"}


def number_of_subscribers(subreddit):
    """
      function that queries the Reddit API and returns the number of
      subscribers (not active users, total subscribers) for a given subreddit.
    """
    url = "https://www.reddit.com/r/{}/about.json".format(subreddit)
    request = requests.get(url, headers=headers, allow_redirects=False)

    if request.status_code == 200:
        return request.json().get("data").get("subscribers")

    return 0
