import subprocess,os,time
from moviepy.editor import VideoFileClip,concatenate_videoclips

def download_video_with_ytdlp(url, output_file):
    # CMD command to download the video using yt-dlp
    command = f'yt-dlp -o "{output_file}" {url}'
    
    # Use subprocess module to run cli commands
    try:
        subprocess.run(command, shell=True, check=True)
        print(f"Video downloaded successfully as '{output_file}'")
    except subprocess.CalledProcessError as e:
        print(f"Failed to download video using ytdlp: {e}")
        raise

# example usage
# reddit_post_url = 'https://www.reddit.com/r/Unexpected/comments/1ccf3qm/wasnt_even_speeding/'  # Replace this with the URL of the Reddit post
# download_video_with_ytdlp(reddit_post_url, 'Output\\video15.mp4')


# possible solution to some of the videos getting corrupted but since the final video is viewable despite the issue have not implemented this part
# but might be necessary at a later stage
def strip_metadata(input_path, output_path):
    os.system(f'ffmpeg -y -i "{input_path}" -vf "transpose=1,transpose=2" "{output_path}"')


# first approach
def resize_clips(output_directory,resized_path,standard_width = 720):

    
    clip_names = list(os.listdir(output_directory))
    
    for clip_name in clip_names:
        try:
            clip_path = os.path.join(output_directory,clip_name)
            
            clip = VideoFileClip(clip_path)
            
            clip_width = clip.size[0]
            clip_height = clip.size[1]
            
            # we multiply original height by factor (720 / clip width)
            new_height = clip_height * (standard_width / clip_width)
            try:
                resized_clip = clip.resize((standard_width, new_height))
            except:
                print("Error when trying to resize.")

            resized_clip_name = os.path.join(resized_path,"resized_" + str(standard_width) + "_" + str(new_height) + "_.mp4")
            
            try:
                resized_clip.write_videofile(resized_clip_name, codec='libx264')
            except Exception as e:
                print("The resized file was made but failed to write it to file system." , e)
                raise
        
        except Exception as e:
            print("Error when trying to resize clip with name -" , clip_name , "\n", e)
            updated_clip_name = os.path.join(resized_path,"resized_" + str(clip_width) + "_" + str(clip_height) + "original_.mp4")
            print("Trying to write the original file itself")
            try:
                clip.write_videofile(updated_clip_name , codec='libx264')
            except Exception as e:
                print("Error when trying to write the original video file as well." , e)
            continue
            
            
    
    print("Resized all clips\n Going for deleting the videos in output folder")
    time.sleep(3)
    delete_files(output_directory)
    
    
def delete_files(dir_path):
    for filename in os.listdir(dir_path):
        file_path = os.path.join(dir_path, filename)
        try:
            if os.path.isfile(file_path) or os.path.islink(file_path):
                os.unlink(file_path)
                print(f"Deleted file: {file_path}")
        except Exception as e:
            print(f"Failed to delete {file_path}due to reason: {e}")
            continue
    print("Deleted all videos in - " , dir_path)


#to merge the resized videos
def merge_videos(resized_path, merged_path):
    
    videos = list(os.listdir(resized_path))
    video_paths = [os.path.join(resized_path,video) for video in videos]
    
    video_clips = [VideoFileClip(video_clip) for video_clip in video_paths]

    try:
        final_clip = concatenate_videoclips(video_clips,method="compose")
    except Exception as e:
        print("Error when trying to concatenate file." , e)
        raise
    finally:
        time.sleep(3)
        delete_files(resized_path)
        

    try:
        final_clip.write_videofile(merged_path, codec="libx264")
    except Exception as e:
        print("Error when trying to concatenate file." , e)
        raise
    finally:
        time.sleep(3)
        delete_files(resized_path)

    
    # time.sleep(3)
    # delete_files(resized_path)


# example usage
# resize_clips("output","resized_clips",720)

# merge_videos(video_paths,os.path.join("resized_clips","merged_.mp4"))

# delete_videos(r"output")