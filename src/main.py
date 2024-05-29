# import praw
import pandas as pd
import os,time
from excel_operations import *
from download_video import *
from get_details import *
from video_operations import *


# Take 25 links more than the current counter
# Assuming that the video duration constraint is 20 sec, a 60 second video will be 3 videos
def create(subreddit):
    
    # deleting any temporary video clips
    delete_files(r"output")
    delete_files(r"resized_clips")
    
    counter = get_counter(subreddit)
    post_links = generate_links(subreddit,counter)

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
        
        if (is_valid(post_duration,post_flair,is_nsfw,post_height,post_width)):
            try:
                download_video_with_ytdlp(post_link,os.path.join(ouptut_directory,"video_" + str(post_width) + "_" + str(post_height) + "_"))
                
                current_duration_counter += post_duration
                
            except:
                print("Error when downloading video with link - ",post_link)
        
        # we got as many videos as we wanted
        if (current_duration_counter>60):
            break
            
        else:
            print("Skipping the video as not valid")
            continue
    
    video_width = 720
    resized_path = r"resized_clips"
    output_path = r"output"
    
    # resize all the clips to a standard width( may be 720p )
    resize_clips(output_path,resized_path,video_width)
    
    # merge all the clips together to get merged_.mp4
    # this will be stored in the resized_clisp folder
    merge_videos(resized_path,os.path.join("output","merged_.mp4"))
    
        
    try:
        write_counter(subreddit, counter)
        print("Successfully able to write the counter into the excel file.")
    except:
        print("There was an error while trying to write the counter")
        

if __name__ == "__main__":
    #Enter the subreddit you want to fetch top posts from here
    subreddit = "FunnyDogVideos"
    create(subreddit)