import dropbox
from fastapi import HTTPException
from generate_access_token import *


APP_KEY = ''
APP_SECRET = ''

REFRESH_TOKEN = ''

def upload_to_dropbox():
    
    # get a new short lived access token
    short_access_key = get_new_access_token(APP_KEY , APP_SECRET , REFRESH_TOKEN)

    if (short_access_key == None):
        raise KeyError("Error code - 100")

    db = dropbox.Dropbox(short_access_key)

    file_path = r"C:\Users\LENOVO\Documents\Important_documents\VIT\Projects\REEL_AUTOMATION\output\merged_.mp4"

    # The folder where the video will be saved
    dropbox_destination_path = "/genreel_content/merged_.mp4"
    dropbox_folder_path = "/genreel_content"


    # Make sure that the folder exists
    def ensure_folder_exists(path):
        try:
            db.files_get_metadata(path)
            print("Folder exists already")
        except dropbox.exceptions.ApiError as e:
            if e.error.is_path() and e.error.get_path().is_not_found():
                db.files_create_folder_v2(path)
                print(f"Created folder: {path}")
            else:
                print("Couldnt create the folder")
                raise HTTPException(status_code=400, detail=str(e))

    # Ensure the folder structure exists first, otherwise quit
    ensure_folder_exists(dropbox_folder_path)

    with open(file_path, 'rb') as f:
        db.files_upload(f.read(), dropbox_destination_path, mode=dropbox.files.WriteMode("overwrite"))
    
    print("Wrote the file into dropbox.\nFetching public video url now.")
    
    public_link = get_public_link(db , dropbox_destination_path)
    
    return public_link
    
def get_public_link(db , file_path):
    try:
        shared_links = db.sharing_list_shared_links(file_path , direct_only = True)
        print(shared_links)
        
        if (shared_links.links):
            return shared_links.links[0].url
        else:
            shared_link = db.sharing_create_shared_link_with_settings(file_path)
            return shared_link.url  # The public URL for your file
    
    except dropbox.exceptions.ApiError as e:
        raise Exception(f"Error creating shared link: {e}")
        
public_link = upload_to_dropbox()
print("\nThe public link is - " , public_link)