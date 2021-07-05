###
# PAUL BOT
###

# Libraries

import praw
import os


# Connection

__author__ = "CLYDE"

reddit = praw.Reddit(
  client_id=os.environ['clientid'],
  client_secret=os.environ['clientsecret'],
  user_agent="<console:paul:1.3.1> (by /u/Among_Joe)",
  username="Among_Joe",
  password=os.environ['password']
)

# definitions

def space():
  print(" ")

def paul(msg):
  print(msg)

# Functions

paul("Welcome to Paul. Please input the subreddit you would like to collect data from.")
the_sub = input(" ")
paul("How much posts will you like to read? (enter an integer)")
post_amount = input(" ")

subreddit = reddit.subreddit(the_sub) # r/okbuddyretard will be used for this experiment

for submission in reddit.subreddit(the_sub).hot(limit=int(post_amount)):
  paul("----------------------")
  print(submission.title)
  space()
  print(submission.url)
  space()
  print(submission.author)