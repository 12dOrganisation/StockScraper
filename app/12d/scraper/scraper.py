import praw
import pandas as pd
import datetime as dt
reddit = praw.Reddit(
    client_id="qMLQNap3Yn5knA",
    client_secret="tNGtBkbwD4wOzaWszjRvDwM5_ReH6g",
    user_agent="StockScraper"
)
WSB = reddit.subreddit('wallstreetbets')

for submission in WSB.hot(limit=10):
    print(submission.title)
