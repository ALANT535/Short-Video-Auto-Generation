import dropbox
from fastapi import HTTPException
import os
import requests
from requests.auth import HTTPBasicAuth

def upload_to_dropbox(APP_KEY , APP_SECRET , REFRESH_TOKEN):
    
    # get a new short lived access token
    short_access_key = get_new_access_token(APP_KEY , APP_SECRET , REFRESH_TOKEN)

    if (short_access_key == None):
        print("Was not able to generate a short-lived token.")
        raise KeyError("Error code - 100")
    

    db = dropbox.Dropbox(short_access_key)
    
    parent_directory = "\\".join(os.path.abspath(__file__).split("\\")[:-3])
    file_path = os.path.join(parent_directory,"output","merged_.mp4")

    # The folder where the video will be saved
    dropbox_destination_path = "/genreel_content/merged_.mp4"
    dropbox_folder_path = "/genreel_content"


    # Make sure that the folder exists
    def ensure_folder_exists(path):
        try:
            db.files_get_metadata(path)
            print("Folder exists already.")
        except dropbox.exceptions.ApiError as e:
            if e.error.is_path() and e.error.get_path().is_not_found():
                db.files_create_folder_v2(path)
                print(f"Folder doesn't exist. Created new folder: {path}")
            else:
                print(e,"\nCouldnt create the folder.")
                raise

    # Ensure the folder structure exists first, otherwise quit
    try:
        ensure_folder_exists(dropbox_folder_path)
    except Exception as e:
        print("Error when trying to check if folder exists.")
        raise

    try:
        with open(file_path, 'rb') as f:
            db.files_upload(f.read(), dropbox_destination_path, mode=dropbox.files.WriteMode("overwrite"))
    except Exception as e:
        print(e)
        print("Error when trying to upload to dropbox")
        raise
    
    print("Wrote the file into dropbox.\nFetching public video url now.")
    
    try:
        public_link = get_public_link(db , dropbox_destination_path)
    except:
        print("Error creating shared link.")
        raise
    
    return public_link
    
def get_public_link(db , file_path):
    try:
        shared_links = db.sharing_list_shared_links(file_path , direct_only = True)
        
        if (shared_links.links):
            return shared_links.links[0].url
        else:
            # Creates a new public URL for your file
            shared_link = db.sharing_create_shared_link_with_settings(file_path)
            return shared_link.url
    
    except dropbox.exceptions.ApiError as e:
        print(e)
        raise Exception(e)

    # Will always return "https://www.dropbox.com/scl/fi/d8m3tdjj8dpzky5fs513c/merged_.mp4?rlkey=f04kepn1hnwj4kyzyuj12g6ck&raw=1"
    # But, keep this code in case something changes

# Call thIS function to get a new access token
def get_new_access_token(APP_KEY , APP_SECRET , REFRESH_TOKEN):
    url = "https://api.dropbox.com/oauth2/token"
    
    params = {
        'grant_type': 'refresh_token',
        'refresh_token': REFRESH_TOKEN
    }

    auth = HTTPBasicAuth(APP_KEY, APP_SECRET)
    
    response = requests.post(url, data=params, auth=auth)

    # Got the new access token
    if response.status_code == 200:
        data = response.json()
        access_token = data['access_token']
        print("New access token:", access_token)
        return access_token
    else:
        print("Failed to refresh token:", response.json())
        return None

# sample usage
# get_new_access_token(APP_KEY , APP_SECRET , REFRESH_TOKEN)