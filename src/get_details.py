import requests 
import praw
import os

# generate the top posts of all time from a subreddit with a certain limit
def generate_links(subreddit_name, limit_number):
    reddit = praw.Reddit(client_id='DVRt4brRO5KCCi4YSt1E-g', client_secret='qWCthQ9lapzgBlQNQnbrsAMWQ58ygQ', user_agent='GENREEL')
    subreddit = reddit.subreddit(subreddit_name)

    top_posts = subreddit.top(limit=limit_number)
    post_details = []

    for post in top_posts:
        post_details.append(f"https://www.reddit.com{post.permalink}",)
    
    return post_details

#input a link to a reddit post and return the duration, title and flair of the post
def get_post_details(link):
    raw_link = r"{}{}.json".format(link, "")
    resp = requests.get(raw_link + ".json")
    data = resp.json()
    #parse through the json file


    post_title = data[0]['data']['children'][0]['data']['title']
    post_duration = data[0]['data']['children'][0]['data']['secure_media']['reddit_video']['duration']
    post_flair = data[0]['data']['children'][0]['data']['link_flair_richtext'][0]['t']
    is_nsfw = "nsfw" in str(data)

    # print("Post Title is - ",post_title)
    # print("Post duration is - ",post_duration)
    # print("Post flair is - ",post_flair)
    
    return [post_title,post_duration,post_flair,is_nsfw]

get_post_details("https://www.reddit.com/r/MemeVideos/comments/1ce1o3z/verbelase_50k_best_part/")