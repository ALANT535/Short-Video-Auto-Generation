import praw
import requests
import os

def generate_links(reddit, subreddit_name, limit_number):
    subreddit = reddit.subreddit(subreddit_name)

    top_posts = subreddit.top(limit=limit_number)
    post_details = []

    for post in top_posts:
        post_details.append({
            'permalink': f"https://www.reddit.com{post.permalink}",
            'flair': post.link_flair_text,
            'duration': post.media.duration if hasattr(post.media, 'duration') else None,
            # 'has_audio': post.media is not None and post.media.get('reddit_video', {}).get('is_gif', False) is False
        })
    
    return post_details

reddit = praw.Reddit(client_id='DVRt4brRO5KCCi4YSt1E-g', client_secret='qWCthQ9lapzgBlQNQnbrsAMWQ58ygQ', user_agent='GENREEL')
 
post_details = generate_links(reddit, "MemeVideos", 3)

for post_detail in post_details:
    unique_post_id = post_detail['permalink'].split("/")[-3]
    post_title = post_detail['permalink'].split("/")[-2]
    print("Post Title:", post_title)
    print("Flair:", post_detail['flair'])
    print("Duration:", post_detail['duration'])
    print("Downloading video...\n\n")
    # download_video(post_detail['permalink'], os.path.join("output", unique_post_id))
