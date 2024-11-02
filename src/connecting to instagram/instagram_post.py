import requests
import time

ACCESS_TOKEN = ''
INSTAGRAM_BUSINESS_ACCOUNT_ID = ''
VIDEO_URL = ''  # The video should be publicly accessible
CAPTION = 'testing for captions'

def create_media_container(instagram_account_id, video_url, caption, access_token):
    url = f"https://graph.facebook.com/v17.0/{instagram_account_id}/media"
    
    # The payload to create the media container
    payload = {
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
    url = f"https://graph.facebook.com/v17.0/{instagram_account_id}/media_publish"
    
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
    url = f"https://graph.facebook.com/v17.0/{media_container_id}"
    
    # Payload to check the status
    params = {
        'fields': 'status',
        'access_token': access_token
    }
    
    response = requests.get(url, params=params)
    if response.status_code == 200:
        status = response.json().get('status')
        print(f"Upload status: {status}")
        return status
    else:
        print(f"Failed to check upload status: {response.status_code}")
        print(response.json())
        return None

if __name__ == "__main__":
    # Step 1: Create media container
    media_container_id = create_media_container(INSTAGRAM_BUSINESS_ACCOUNT_ID, VIDEO_URL, CAPTION, ACCESS_TOKEN)
    
    while (media_container_id):
        # Step 2: Wait for the video to be processed
        time.sleep(10)  # Give it a few seconds to process the media container
        
        # Step 3: Check upload status
        status = check_upload_status(media_container_id, ACCESS_TOKEN)
        
        # Step 4: If the media is processed, publish it
        if status == 'FINISHED':
            publish_video(INSTAGRAM_BUSINESS_ACCOUNT_ID, media_container_id, ACCESS_TOKEN)
            break
        else:
            print(f"Media is not ready for publishing. Status: {status}")
            print("Trying again.")
