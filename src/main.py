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

os.path.abspath(__file__)
ouptut_directory = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))),"output")
# print(post_links[2])
# print(get_post_details(post_links[2]))
# exit()

for post_link in post_links:
    # keep track of the counter so that you can update the same in the database
    counter += 1
    
    if (is_valid(post_link)):
        
        download_video_with_ytdlp(post_link,os.path.join(ouptut_directory,"video" + str(counter)))
          
    else:
        print("Skipping the video as not valid")
        continue
    
    # 1080 pixels x 1920 pixels
    # aspect ratio of 16:9
    
    
    
    # break
    


# generate_links