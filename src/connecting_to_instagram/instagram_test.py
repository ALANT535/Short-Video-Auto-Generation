import requests
import time


ACCESS_TOKEN = 'EAAYMpfZBSVSQBOxqqdExQTRveRSuXfb5L5RzBjSAgRGaOCsZCkLs7lZACuQGeN3uwMEwZCsfzBCAPQnLilIMOzI5njxmhz2sfJEhEPtZBYbWSeUG0599kzK4LmDVEDOiviL5lPRRsWsZAF7aYHjiij6NkS5ZBGGwTV972vsb4UQjwvTfqwYB90ZAywY5n0xiKHbV'
INSTAGRAM_BUSINESS_ACCOUNT_ID = 'your-instagram-business-account-id'
VIDEO_URL = 'your-public-video-url'
CAPTION = 'your-video-caption'

def create_media_container(instagram_account_id, video_url, caption, access_token):
    url = f"https://graph.facebook.com/v21.0/{instagram_account_id}/media"
    
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

    media_container_id = create_media_container(INSTAGRAM_BUSINESS_ACCOUNT_ID, VIDEO_URL, CAPTION, ACCESS_TOKEN)
    
    if media_container_id:
        time.sleep(10)

        status = check_upload_status(media_container_id, ACCESS_TOKEN)
        
        if status == 'FINISHED':
            publish_video(INSTAGRAM_BUSINESS_ACCOUNT_ID, media_container_id, ACCESS_TOKEN)
        else:
            print(f"Media is not ready for publishing. Status: {status}")
