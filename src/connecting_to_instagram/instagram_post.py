import requests
import time
import sys

ACCESS_TOKEN = 'EAAYMpfZBSVSQBOZBJgEbrKcZAeBgk3iZAhSri5QEHrb5WMTKtXrp479CfnKu3drraGriKaGDKXWJOAgDv0lbvMve6ohH1e7xfHB1GwMCXECSQZAIEPdyRxCE4bWsYAWPmUhMTA7wskhyTMD1o4B1mfe6reMvZB5kvcVxexaCbQCn08JD8AfUrrUs9toSgjqG5W'
INSTAGRAM_BUSINESS_ACCOUNT_ID = '17841454975440576'
VIDEO_URL = 'https://www.dropbox.com/scl/fi/d8m3tdjj8dpzky5fs513c/merged_.mp4?rlkey=f04kepn1hnwj4kyzyuj12g6ck&raw=1'
# convert it to raw form (just in case)
CAPTION = '''CURSED MEMES YOU CANNOT UNSEE

#meme #doge #video #funnyvideos #funny #elonmusk'''

# Step 1
def create_media_container(instagram_account_id, video_url, caption, access_token):
    url = f"https://graph.facebook.com/v21.0/{instagram_account_id}/media"
    
    # The payload to create the media container
    payload = {
        'media_type': 'REELS',
        'video_url': video_url,
        'caption': caption,
        'access_token': access_token
    }
    
    response = requests.post(url, data=payload)
    if response.status_code == 200:
        media_container_id = response.json().get('id')
        print(f"Media container created. ID: {media_container_id}")
        return media_container_id
    else:
        print(f"Failed to create media container: {response.status_code}")
        print(response.json())
        return None

def publish_video(instagram_account_id, media_container_id, access_token):
    url = f"https://graph.facebook.com/v21.0/{instagram_account_id}/media_publish"
    
    # The payload to publish the video
    payload = {
        'creation_id': media_container_id,
        'access_token': access_token
    }
    
    response = requests.post(url, data=payload)
    if response.status_code == 200:
        print(f"Video published successfully!")
        print(response.json())
    else:
        print(f"Failed to publish video: {response.status_code}")
        print(response.json())

def check_upload_status(media_container_id, access_token):
    url = f"https://graph.facebook.com/v21.0/{media_container_id}"
    
    params = {
        'fields': 'status',
        'access_token': access_token
    }
    
    response = requests.get(url, params=params)
    if response.status_code == 200:
        status = response.json().get('status')
        return status
    else:
        print(f"Failed to check upload status: {response.status_code}")
        print(response.json())
        return None

if __name__ == "__main__":
    # Step 1: Create media container
    media_container_id = create_media_container(INSTAGRAM_BUSINESS_ACCOUNT_ID, VIDEO_URL, CAPTION, ACCESS_TOKEN)
    
    if (media_container_id == None):
        print("Exiting.")
        sys.exit(1)
        
    
    while (media_container_id):
        # Step 2: Wait for the video to be processed
        time.sleep(10)  # Give it a few seconds to process the media container
        
        # Step 3: Check upload status and proceed into next step when processed the video
        status = check_upload_status(media_container_id, ACCESS_TOKEN)
        
        print("Current status :" , status)
        
        # Step 4: If the media is processed, publish it
        if ('Finished' in status):
            print("Finished creating the media container.")
            break
        
        elif('Failed' in status or 'failed' in status or status == None):
            print("Was not able to process the media container. Exiting.")
            sys.exit(1)
        
    publish_video(INSTAGRAM_BUSINESS_ACCOUNT_ID, media_container_id, ACCESS_TOKEN)