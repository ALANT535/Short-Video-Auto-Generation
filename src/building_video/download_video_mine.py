import praw

def generate_links(subreddit_name, limit_number):
    reddit = praw.Reddit(client_id='DVRt4brRO5KCCi4YSt1E-g', client_secret='qWCthQ9lapzgBlQNQnbrsAMWQ58ygQ', user_agent='GENREEL')
    subreddit = reddit.subreddit(subreddit_name)

    top_posts = subreddit.top(limit=limit_number)
    post_details = []

    for post in top_posts:
        post_details.append(f"https://www.reddit.com{post.permalink}",)
    
    return post_details