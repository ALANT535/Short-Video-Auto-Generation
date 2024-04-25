import praw
import requests
import os

def generate_links(reddit,subreddit_name,limit_number):
    subreddit = reddit.subreddit(subreddit_name)

    top_posts = subreddit.top(limit=limit_number)
    post_links = []

    for post in top_posts:
        post_links.append(f"https://www.reddit.com{post.permalink}")
    
    return post_links

def download_video(url, output_file):
    response = requests.get(url)
    
    if response.status_code == 200:
        with open(output_file, 'wb') as f:
            f.write(response.content)
        print(f"Video downloaded successfully as '{output_file}'")
    else:
        print(f"Failed to download video. Status code: {response.status_code}")

# Replace the empty strings with your details
# Refer Readme for more info
reddit = praw.Reddit(client_id='',client_secret='',user_agent='')
 
post_links = generate_links(reddit,"Unexpected",3)

for post_link in post_links:
    unique_post_id = post_link.split("/")[-3]
    post_title = post_link.split("/")[-2]
    print("Downloading video titled - ",post_title)
    download_video(post_link,os.path.join("output",unique_post_id))