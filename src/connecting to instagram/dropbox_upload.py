import dropbox

db = dropbox.Dropbox("dn0bcugrtiw3mju")

file_path = r"C:\Users\LENOVO\Documents\Important_documents\VIT\Projects\REEL_AUTOMATION\output\merged_.mp4"

# The folder where the video will be saved
dropbox_destination_path = r"genreel_content/merged_.mp4"


with open(file_path, 'rb') as f:
    db.files_upload(f.read(), dropbox_destination_path, mode=dropbox.files.WriteMode("overwrite"))

