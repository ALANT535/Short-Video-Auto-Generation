from typing import Annotated
from fastapi.responses import FileResponse
from fastapi import FastAPI, File, UploadFile, HTTPException
from pathlib import Path 

app = FastAPI()

UPLOAD_FILE_PATH = Path("uploaded_files/merged.mp4")
UPLOAD_FILE_PATH.parent.mkdir(parents=True,exist_ok = True)

@app.get("/")
async def root_function():
    return {"This is the Index page, welcome here!"}

# This is the endpoint that will upload the actual video file
@app.post("/uploadfile/")
async def upload_file(file:UploadFile):
    try:
        with open(UPLOAD_FILE_PATH , "wb") as f:
            f.write(await file.read())
            
    except Exception as e:  # Catch any file related exceptions
        raise HTTPException(status_code=400, detail=str(e))
    
    return {"filename":file.filename , "Status":200}

# 400 status code means not successful - ERROR
# 200 status code means was successful - OKAY    


# This will be fetched using a GET method
@app.get("/download/")
async def download_file():
    if not UPLOAD_FILE_PATH.exists():
        raise HTTPException(status_code=404, detail="File not found")
    
    return FileResponse(UPLOAD_FILE_PATH)
# This will then be connected to a public server link

# This is used to return the Public Video Link
@app.get("/video_url/")
async def get_video_url():
    return {"video_url": f"http://127.0.0.1:8000/download/"}