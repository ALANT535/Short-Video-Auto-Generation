import subprocess,os
from moviepy.editor import VideoFileClip,concatenate_videoclips

def download_video_with_ytdlp(url, output_file):
    # CMD command to download the video using yt-dlp
    command = f'yt-dlp -o "{output_file}" {url}'
    
    # command = f'yt-dlp -o "{output_file}" --format "bestvideo[height={"1080x1920"}]+bestaudio" {url}'
    
    # Use subprocess module to run cli commands
    try:
        subprocess.run(command, shell=True, check=True)
        print(f"Video downloaded successfully as '{output_file}'")
    except subprocess.CalledProcessError as e:
        print(f"Failed to download video: {e}")

# example usage
# reddit_post_url = 'https://www.reddit.com/r/Unexpected/comments/1ccf3qm/wasnt_even_speeding/'  # Replace this with the URL of the Reddit post
# download_video_with_ytdlp(reddit_post_url, 'Output\\video15.mp4')


# width * height
def get_clip_dimensions(output_path):
    clip_names = list(os.listdir(output_path))
    
    clip_dimensions = [[clip_name.split("_")[1],clip_name.split("_")[2]] for clip_name in clip_names]
    
    return clip_dimensions


# first approach
def resize_clips(output_path,resized_path,standard_width = 720):
    # initializing it to a negative number
    max_height = -1
    
    clip_names = list(os.listdir(output_path))
    
    for clip_name in clip_names:
        clip = VideoFileClip(os.path.join("output",clip_name))
        
        clip_width = clip.size[0]
        clip_height = clip.size[1]
        
        # we multiply original height by factor (720 / clip width)
        new_height = clip_height * (standard_width / clip_width)
        try:
            resized_clip = clip.resize((standard_width, new_height))
        except:
            print("Error when trying to resize.")

        resized_clip_name = os.path.join("resized_clips","resized_" + str(standard_width) + "_" + str(new_height) + "_.mp4")
        
        try:
            resized_clip.write_videofile(resized_clip_name, codec='libx264')
        except:
            print("Error when trying to write resized file.")


#to merge the resized videos
def merge_videos(video_clip_list, output_path):
    
    video_clips = [VideoFileClip(video_clip) for video_clip in video_clip_list]


    final_clip = concatenate_videoclips(video_clips,method="compose")


    final_clip.write_videofile(output_path, codec="libx264", audio_codec="aac")

resize_clips("output","resized",720)
videos = list(os.listdir(r"resized_clips"))
video_paths = [os.path.join("resized_clips",video) for video in videos]

output_path = os.path.join("resized_clips","merged_testing.mp4")
merge_videos(video_paths,output_path)