# import praw
import pandas as pd
import os
from excel_operataions import *
from download_video_mine import *
from get_details import *
from using_yt_dlp import *

subreddit = "MemeVideos"


# Take 15 links more than the curernt counter
# Assuming that the video duration constraint is 20 sec, a 60 second video will be 3 videos
def create(subreddit):
    counter = get_counter(subreddit)
    post_links = generate_links(subreddit,counter + 25)

    os.path.abspath(__file__)
    ouptut_directory = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))),"output")

    current_duration_counter = 0
    # used to keep track of the current video duration
    # want it to be 120 seconds

    for post_link in post_links:
        # keep track of the counter so that you can update the same in the database
        counter += 1
        
        post_link = r"{}{}.json".format(post_link, "")
        post_title,post_duration,post_flair,is_nsfw,post_height,post_width = get_post_details(post_link)
        
        if (is_valid(post_duration,post_flair,is_nsfw)):
            try:
                download_video_with_ytdlp(post_link,os.path.join(ouptut_directory,"video" + str(counter)))
                
                current_duration_counter += post_duration
                
            except:
                print("Error when downloading video with link - ",post_link)
        
        # we got as many videos as we wanted
        if (current_duration_counter>60):
            break
            
        else:
            print("Skipping the video as not valid")
            continue
        
    try:
        write_counter(subreddit, counter)
    except:
        print("There was an error while trying to write the counter")

# okay now have to work on the merging part
#WILL CONTINUE TO WORK AFTER EXAMS

# 2 cases

# either its in the shorts format and we can just scale it up to the required resolution of 1080 * 1920p
# or we would have to take the minimmum of the length, breadth and then scale it up as per whichever one is minimum

# we then merge the videos

# this is the opposite of 1920 * 1080p as it is in laptops

# a main issue is that we wouldnt know which

# one of the resolutions observed was 792*480
# height * width
# 1920*1080 - aspect ratio of 1.77778
# 792   

if __name__ == "__main__":
    subreddit = "MemeVideos"
    create(subreddit)
    