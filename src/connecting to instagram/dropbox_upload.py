import dropbox
from fastapi import HTTPException

db = dropbox.Dropbox("short_access_key")

file_path = r"C:\Users\LENOVO\Documents\Important_documents\VIT\Projects\REEL_AUTOMATION\output\merged_.mp4"

# The folder where the video will be saved
dropbox_destination_path = "/genreel_content/merged_.mp4"

def ensure_folder_exists(path):
    try:
        db.files_get_metadata(path)
    except dropbox.exceptions.ApiError as e:
        if e.error.is_path() and e.error.get_path().is_not_found():
            db.files_create_folder_v2(path)
            print(f"Created folder: {path}")
        else:
            raise HTTPException(status_code=400, detail=str(e))

# Ensure the folder structure exists first, otherwise quit
ensure_folder_exists('/genreel_content')

with open(file_path, 'rb') as f:
    db.files_upload(f.read(), dropbox_destination_path, mode=dropbox.files.WriteMode("overwrite"))

