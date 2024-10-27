from typing import Annotated

from fastapi import FastAPI, File, UploadFile, HTTPException
from pathlib import Path 

app = FastAPI()

UPLOAD_FILE_PATH = Path("uploaded_files/merged.txt")
UPLOAD_FILE_PATH.parent.mkdir(exist_ok = True)

@app.get("/")
async def root_function():
    return {"This is the Index page, welcome here!"}

# This is the endpoint that will upload the actual video file
@app.post("/uploadfile/")
async def upload_file(file:Annotated[UploadFile , File("This file is being uploaded and is of type UploadFile")]):
    try:
        with open(UPLOAD_FILE_PATH , "w") as f:
            f.write(await file.read())
    except:
        return {"filename":file.filename , "Status":400}
    
    return {"filename":file.filename , "Status":200}

# 400 status code means not successful - ERROR
# 200 status code means was successful - OKAY    

@app.get("uploaded_files")
async def get_details():
    if not UPLOAD_FILE_PATH.exists():
        raise HTTPException(status_code=404, detail="File not found")

    with open(UPLOAD_FILE_PATH , "r") as f:
        text_read = f.read()
    
    return {"content read":text_read}

# This will then be connected to a public server link
# This will be fetched using a GET method