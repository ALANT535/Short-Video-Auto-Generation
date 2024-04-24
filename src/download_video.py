import praw
from pytube import Reddit

def download_reddit_video(url, output_file):
    reddit = Reddit()
    video = reddit.from_url(url)
    stream = video.streams.filter(progressive=True).first()
    if stream:
        stream.download(output_path='.', filename=output_file)
        print(f"Video downloaded successfully as '{output_file}'")
    else:
        print("No stream available for download")

# REPLACE THE EMPTY STRINGS WITH YOUR CREDENTIALS
# GO THROUGH README FILE FOR REDDIT API
reddit = praw.Reddit(client_id='',
                     client_secret='',
                     user_agent='')

subreddit = reddit.subreddit('Unexpected')

top_posts = subreddit.top(limit=3)


for post in top_posts:
    if post.is_video:
        download_reddit_video(post.media['reddit_video']['fallback_url'], f'{post.id}.mp4')
