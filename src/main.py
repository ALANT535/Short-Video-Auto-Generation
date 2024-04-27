# import praw
import pandas as pd
import os
from excel_operataions import *
from download_video_mine import *
from get_details import *
from using_yt_dlp import *

subreddit = "MemeVideos"

counter = get_counter(subreddit)

# Take 15 links more than the curernt counter
# Assuming that the video duration constraint is 20 sec, a 120 second video will be 6 videos
post_links = generate_links(subreddit,counter + 15)


for post_link in post_links:
    # keep track of the counter so that you can update the same in the database
    counter += 1
    post_title,post_duration,post_flair,is_nsfw = get_post_details(post_link)
    
    # dont want nsfw content
    if (is_nsfw):
        continue
    
    # dont want videos longer thatn 20 seconds
    if (post_duration > 20):
        continue
    
    # dont want videos with this flair (inappropriate :skull:)
    if (post_flair == "Donald Trump leaked sex tapes "):
        continue
    
    print()
    
    
    
    break
    


# generate_links