import praw
import pandas as pd
import datetime as dt


def scaperFunction(numberOfPosts):
    reddit = praw.Reddit(
        client_id="qMLQNap3Yn5knA",
        client_secret="tNGtBkbwD4wOzaWszjRvDwM5_ReH6g",
        user_agent="StockScraper"
    )
    WSB = reddit.subreddit('wallstreetbets')

    topics_dict = {"title": [], \
                   "score": [], \
                   "id": [], "url": [], \
                   "comms_num": [], \
                   "created": [], \
                   "body": []}

    for submission in WSB.hot(limit=numberOfPosts):
        topics_dict["title"].append(submission.title)
        topics_dict["score"].append(submission.score)
        topics_dict["id"].append(submission.id)
        topics_dict["url"].append(submission.url)
        topics_dict["comms_num"].append(submission.num_comments)
        topics_dict["created"].append(submission.created)
        topics_dict["body"].append(submission.selftext)

    return topics_dict
