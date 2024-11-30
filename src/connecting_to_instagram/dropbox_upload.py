import dropbox
from fastapi import HTTPException
from generate_access_token import *
import os


APP_KEY = 'dn0bcugrtiw3mju'
APP_SECRET = '848vzcex6fymjfb'

REFRESH_TOKEN = 'Itu-8RIbsBgAAAAAAAAAAc2xSEVuQec84gJJsOFcAXYbLFAzJQm7MH9RTADFufMS'

def upload_to_dropbox():
    
    # get a new short lived access token
    short_access_key = get_new_access_token(APP_KEY , APP_SECRET , REFRESH_TOKEN)

    if (short_access_key == None):
        print("Was not able to generate a short-lived token.")
        raise KeyError("Error code - 100")
    

    db = dropbox.Dropbox(short_access_key)

    # file_path = r"C:\Users\LENOVO\Documents\Important_documents\VIT\Projects\REEL_AUTOMATION\output\merged_.mp4"
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
                raise HTTPException(status_code=400, detail=str(e))

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
        raise Exception(e)

try:    
    public_link = upload_to_dropbox()
except KeyError as e:
    print("Error when uploading to dropbox.")

# We replace the "&dl" paramater to get the raw video file
public_link = public_link.replace("&dl=0","&raw=1")

print("\nThe public link is - " , public_link)