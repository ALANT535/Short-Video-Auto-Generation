import praw
import pandas as pd
import os
from excel_operataions import *
# from download_video import *

subreddit = "MemeVideos"

counter = get_counter(subreddit)

print(counter)
# print(df.columns)

# generate_links