"""
    FileName:       redditAPI
    Author:         Devavrat Kalam
    Language:       Python3
    Description:    Code to get started with Reddit API.
                    Prints titles of covid19 subreddits
"""

# Import libraries
import json
import praw

# Open config file and set your Reddit App's unique keys with Reddit's API
with open("config.JSON") as f:
    data = json.load(f)
    reddit = praw.Reddit(client_id=data["client_id"], client_secret=data["client_secret"],
                         user_agent="dk")

# Define name of the subreddit
coronaSub = reddit.subreddit("covid19")

# Print the titles which are currently 'hot' on Reddit
for post in coronaSub.hot(limit=10):
    print(post.title, "\n")