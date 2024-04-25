import subprocess

def download_video_with_ytdlp(url, output_file):
    # Command to download the video using yt-dlp
    command = f'yt-dlp -o "{output_file}" {url}'
    
    # Execute the command using subprocess
    try:
        subprocess.run(command, shell=True, check=True)
        print(f"Video downloaded successfully as '{output_file}'")
    except subprocess.CalledProcessError as e:
        print(f"Failed to download video: {e}")

# Example usage
reddit_post_url = 'https://www.reddit.com/r/Unexpected/comments/1ccf3qm/wasnt_even_speeding/'  # Replace this with the URL of the Reddit post
output_file = 'downloaded_video.mp4'  # Specify the name of the output file

download_video_with_ytdlp(reddit_post_url, output_file)