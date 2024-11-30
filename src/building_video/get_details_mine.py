import requests 
import praw
import os

# generate the top posts of all time from a subreddit with a certain limit
def generate_links(subreddit_name, limit_number):

    #ENTER YOUR REDDIT API DETAILS HERE
    reddit = praw.Reddit(client_id='DVRt4brRO5KCCi4YSt1E-g', client_secret='qWCthQ9lapzgBlQNQnbrsAMWQ58ygQ', user_agent='GENREEL')
    subreddit = reddit.subreddit(subreddit_name)

    top_posts = subreddit.top(limit=limit_number+25)
    post_details = []

    for post in top_posts:
        post_details.append(f"https://www.reddit.com{post.permalink}",)
    
    return post_details[limit_number+1:]

#input a link to a reddit post and return the duration, title and flair of the post
def get_post_details(post_link):
    print("Post Link found - ",post_link)
    resp = requests.get(post_link, headers = {'User-agent': 'GENREEL'})
    data = resp.json()
    print(len(data))
    #Parse through the json file

    post_title = data[0]['data']['children'][0]['data']['title']
    
    try:
        post_duration = data[0]['data']['children'][0]['data']['secure_media']['reddit_video']['duration']
    except:
        post_duration = -1
    
    try:
        post_flair = data[0]['data']['children'][0]['data']['link_flair_richtext'][0]['t']
    except:
        post_flair = "None"
    
    try:
        post_height = data[0]['data']['children'][0]['data']['secure_media']['reddit_video']['height']
    except:
        post_height = -1
    
    try:
        
        post_width = data[0]['data']['children'][0]['data']['secure_media']['reddit_video']['width']
    except:
        post_width = -1
        
    is_nsfw = "nsfw" in str(data)

    print("Post Title is - ",post_title)
    print("Post duration is - ",post_duration)
    print("Post flair is - ",post_flair)
    print("Post height is - ",post_height)
    print("Post width is - ",post_width)
    
    return [post_title,post_duration,post_flair,is_nsfw,post_height,post_width]


def is_valid(post_duration,post_flair,is_nsfw,post_height,post_width):
    
    # dont want nsfw content
    if (is_nsfw):
        return False

    
    # dont want videos longer thatn 20 seconds
    if (post_duration > 20 or post_duration < 0):
        return False

    if (post_height < post_width or post_height < 0 or post_width < 0):
        return False
    
    
    return True

# example usage
# get_post_details(r"https://www.reddit.com/r/Unexpected/comments/1cuuxxa/they_better_tip_that_crab_good/.json")
# print(is_valid(17,"None",True))

# print(generate_links("Unexpected",10))