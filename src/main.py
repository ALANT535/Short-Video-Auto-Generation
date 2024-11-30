import requests , sys , os

curr_directory = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
sys.path.append(curr_directory)

from building_video.excel_operations import *
from building_video.download_video_mine import *
from building_video.video_operations import *
from building_video.get_details import *
from building_video.merging import *


# from excel_operations import *
# from download_video_mine import *
# from get_details_mine import *
# from video_operations import *


# Take 25 links more than the current counter
# Assuming that the video duration constraint is 20 sec, a 60 second video will be 3 videos
def create(subreddit):
    
    # Deleting any temporary video clips
    delete_files(r"output")
    delete_files(r"resized_clips")
    
    root_directory = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
    output_directory = os.path.join(root_directory,"output")
    
    try:
        counter = get_counter(subreddit)
        
    except Exception as e:
        print(f"Error when trying to read counter.\n{e}\n\n","Error Code - 101")
        sys.exit(1)
    
    try:
        post_links = generate_links(subreddit,counter)
        
    except requests.exceptions.ConnectionError as e:
        print(f"Connection error: {e}")
        print("Connect the Internet")
        sys.exit(1)
        
    except Exception as e:
        print(f"A non-connection related error occurred when trying to fetch post details.\n{e}")
        sys.exit(1)


    current_duration_counter = 0
    # used to keep track of the current video duration
    required_duration = 60
    # Change this as per your use case
    # want it to be 60 seconds

    for post_link in post_links:
        # keep track of the counter so that you can update the same in the database
        counter += 1
        
        post_link = r"{}{}.json".format(post_link, "")
        try:
            post_title,post_duration,post_flair,is_nsfw,post_height,post_width = get_post_details(post_link)
        except requests.exceptions.ConnectionError as e:
            print("Connection error: " , e)
            print("Connect to the internet")
            continue
            
        except Exception as e:
            print("A non connection related error has occured")
            continue
        
        if (is_valid(post_duration,post_flair,is_nsfw,post_height,post_width)):
            try:
                download_video_with_ytdlp(post_link,os.path.join(output_directory,"video_" + str(post_width) + "_" + str(post_height) + "_"))
                
                current_duration_counter += post_duration
                
            except:
                print("Error when downloading video with link - ",post_link)
        
        # we got as many videos as we wanted
        if (current_duration_counter > required_duration):
            break
            
        else:
            print("Skipping the video as not valid")
            continue
    
    video_count = len(os.listdir(output_directory))
    
    if (video_count == 0):
        print("There are no downloaded clips to make the video. Exiting.")
        sys.exit(1)
        
    
    video_width = 720
    resized_directory = os.path.join(root_directory , r"resized_clips")
    
    # resize all the clips to a standard width( may be 720p )
    resize_clips(output_directory, resized_directory, video_width)
    
    resized_video_count = len(os.listdir(resized_directory))
    
    if (resized_video_count == 0):
        print("There are no downloaded clips to make the video. Exiting.")
        sys.exit(1)
    
    # merge all the clips together to get merged_.mp4
    # this will be stored in the resized_clisp folder
    try:
        merge_videos(resized_directory,os.path.join("output","merged_.mp4"))
    except Exception as e:
        print("Got the above error when trying to merge the videos. " ,e)
    
        
    try:
        write_counter(subreddit, counter)
        print("Successfully able to write the counter into the excel file.")
    except:
        print("There was an error while trying to write the counter")
        
        
    # Stage 2 of the project commences here
    # We have to 1. upload it onto dropbox, 2. get the link and then 3. push it onto instagram using the Graph API
    
    # STEP 1 - Upload it onto dropbox
    # try:
    #     public_link = upload_to_dropbox()
    # except KeyError as e:
    #     print("Error when uploading to dropbox.")
    
    
        

if __name__ == "__main__":
    #Enter the subreddit you want to fetch top posts from here
    subreddit = "FunnyDogVideos"
    # create(subreddit)