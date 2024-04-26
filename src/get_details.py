import requests 

#input a link to a reddit post and return the duration, title and flair of the post
def get_post_details(link):
    raw_link = r"{}{}.json".format(link, "")
    resp = requests.get(raw_link + ".json")
    data = resp.json()
    #parse through the json file


    post_title = data[0]['data']['children'][0]['data']['title']
    post_duration = data[0]['data']['children'][0]['data']['secure_media']['reddit_video']['duration']
    post_flair = data[0]['data']['children'][0]['data']['link_flair_richtext'][0]['t']

    # print("Post Title is - ",post_title)
    # print("Post duration is - ",post_duration)
    # print("Post flair is - ",post_flair)
    
    return [post_title,post_duration,post_flair]

# get_post_details("https://www.reddit.com/r/MemeVideos/comments/194rf2t/happy_accident_for_him/")