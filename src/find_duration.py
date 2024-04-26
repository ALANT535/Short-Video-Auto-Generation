import requests 

resp = requests.get("https://www.reddit.com/r/MemeVideos/comments/194rf2t/happy_accident_for_him/.json")
data = resp.json()
# r[0]['data']['children'][0]['data']['secure_media']['reddit_video']['duration']
post_title = data[0]['data']['children'][0]['data']['title']
post_duration = data[0]['data']['children'][0]['data']['secure_media']['reddit_video']['duration']
post_title = data[0]['data']['children'][0]['data']['secure_media']['reddit_video']['duration']

print(post_title)