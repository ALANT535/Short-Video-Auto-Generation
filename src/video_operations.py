import subprocess,os

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



def get_clip_dimensions(output_path):
    clip_names = list(os.listdir(output_path))
    
    clip_dimensions = [[clip_name.split("_")[1],clip_name.split("_")[2]] for clip_name in clip_names]
    
    return clip_dimensions