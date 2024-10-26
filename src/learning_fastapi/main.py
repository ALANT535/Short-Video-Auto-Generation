from typing import Annotated

from fastapi import FastAPI, File, UploadFile

app = FastAPI()

@app.get("/")
async def root_function():
    return {"This is the Index page, welcome here!"}


# This will be the endpoint to upload the files
@app.post("/uploadfiles/")
async def uploadfile(file:UploadFile):
    return {"name":file.filename}


# This will then be connected to a public server link
# This will be fetched using a GET method