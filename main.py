###
# PAUL BOT (SECURE EDITION)
###

# Libraries

import praw
import os
from replit import db

# Connection

__author__ = "YOUR NAME HERE"

print("WELCOME TO PAUL SECURE")

reddit = praw.Reddit(
  client_id=os.getenv("CLIENT_ID"),
  client_secret=os.getenv("CLIENT_SECRET"),
  user_agent=os.getenv("USER_AGENT"),
  username=os.getenv("USER_NAME") # put your uname here
  password=os.getenv("PASSWORD")
)

# variables



# definitions

def space():
  print(" ")

def paul(msg):
  print(msg)

# Functions

print("Welcome to Paul Secure v1.0. Because this is paul secure, please enter in your info before entering the db. ")
uname = input("USERNAME: ")
if uname == 

paul("Welcome to Paul Secure. Please input the subreddit you would like to collect data from.")
the_sub = input(" ")
paul("How much posts will you like to read? (enter an integer)")
post_amount = input(" ")

subreddit = reddit.subreddit(the_sub) 
for submission in reddit.subreddit(the_sub).hot(limit=int(post_amount)):
  submissionz = (
  paul("----------------------")
  print(submission.title)
  space()
  print(submission.url)
  space()
  print(submission.author)
  )
print("Write this to a file?")
filewrite = input("(y or n) ")
if filewrite == "y":
  pass
elif filewrite == "n":
  print("File has not been written.")
else:
  print("invalid answer; aborting (error code 100)")