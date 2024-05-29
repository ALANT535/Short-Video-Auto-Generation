import praw

def generate_links(subreddit_name, limit_number):
    
    #ENTER YOUR REDDIT API DETAILS HERE
    reddit = praw.Reddit(client_id='', client_secret='', user_agent='')
    subreddit = reddit.subreddit(subreddit_name)

    top_posts = subreddit.top(limit=limit_number)
    post_details = []

    for post in top_posts:
        post_details.append(f"https://www.reddit.com{post.permalink}",)
    
    return post_details