import subprocess

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
# output_file = 'Output\\video15.mp4'  # Specify the name of the output file

# download_video_with_ytdlp(reddit_post_url, output_file)