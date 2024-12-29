import requests

# generate the top posts of all time from a subreddit with a certain limit
def generate_links(subreddit_name, limit_number, reddit):
    
    subreddit = reddit.subreddit(subreddit_name)

    top_posts = subreddit.top(limit=limit_number+25)
    post_details = []

    for post in top_posts:
        post_details.append(f"https://www.reddit.com{post.permalink}",)
    
    return post_details[limit_number+1:]

# trying new approach to work for the github actions
def new_approach(post_link , reddit):
    print("Post Link found - ",post_link)
    post = reddit.submission(id=post_link)
    try:
        post_title = post.title if post.title else None
        
        post_flair = post.link_flair_text if post.link_flair_text else None
        
        nsfw_status = post.over_18 if post.over_18 is not None else None

        video_info = post.media.get('reddit_video', None)
        
        if video_info:
            post_width = video_info.get('width', None)
            post_height = video_info.get('height', None)
            post_duration = video_info.get('duration', None)
        else:
            post_width = None
            post_height = None
            post_duration = None
            
        # Add the fetched details to the post_details list
        post_details = [post_title, post_flair, nsfw_status, post_height, post_width]
        
        print(f"Post Title - {post_title}")
        print(f"Post Flair - {post_flair}")
        print(f"NSFW: {nsfw_status}")
        print(f"Post Height: {post_height}")
        print(f"Post Width: {post_width}")
        print(f"Post Duration: {post_duration}")
        
    except Exception as e:
        print(f"An error occurred: {e}")
        raise
    return post_details
    

#input a link to a reddit post and return the duration, title and flair of the post
def get_post_details(post_link):
    print("Post Link found - ",post_link)
    resp = requests.get(post_link, headers = {'User-agent': 'GENREEL/0.1 by u/Kokki535'})
    print(f"Status Code - {resp.status_code}")
    print(resp)
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
    print("Post width is - ",post_width,end="\n\n")
    
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
