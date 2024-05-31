# Short-Video-Auto-Generation

## Description

This is an attempt to automate generation of short videos that are prelevant in short-content type platforms like Instagram Reels, Youtube Shorts etc. The primary motivation is to handle videos of various dimensions and ensure that they compile and in a proper manner without manual intervention. The only manual intervention involved in this project is just to run the 'main.py' script. The solution leverages tools like FFmpeg for video processing and Python scripts to automate tasks, making it efficient and reliable. This project helped to explore the moviepy library in addition to the FFmpeg software which helped to understand how the audio and video layers interact and merge with each other to form a video with sound.

## Technologies Used

**Python:** The application was built using Python and its libraries. Python's extensive standard library and third-party modules facilitate the development of robust automation scripts.
**Reddit API Integration:** Used to fetch video content directly from Reddit. This allows for automated retrieval and processing of videos posted on Reddit, enhancing the automation pipeline.
**FFmpeg:** A powerful multimedia framework used to decode, encode, and merge layers of any multimedia content. It ensures videos are processed and encoded to meet Instagram's specifications.
**MoviePy:** A Python library for video editing, used for tasks like resizing and adding effects to videos. MoviePy simplifies complex video editing tasks with a straightforward API.
**Time Module:** To add delays in the script where necessary. It is particularly useful for creating pauses between tasks to ensure proper sequencing and timing.

## How to create and Use Reddit API

1. Create / Log into your reddit account
2. Go to the following link - [https://www.reddit.com/prefs/apps]()
3. Create an app by filling in the details.
4. Once created, note down your secret key and secret client id.
5. These will be used to query Reddit through their API.


## Sample Output Videos Created

Find a few sample generated videos in the output folder in repository
The file name of the file represents the subreddit it was picked up from.

Introduction
This project aims to automate the process of resizing videos and posting them on Instagram. The primary motivation is to handle videos of various dimensions and ensure they meet Instagram's requirements without manual intervention. The solution leverages tools like FFmpeg for video processing and Python scripts to automate tasks, making it efficient and reliable.

Instagram API: For posting videos directly to Instagram.
Installation Guide
Prerequisites
Python 3.6+: Ensure you have Python installed on your machine. You can download it from Python's official site.
FFmpeg: Install FFmpeg on your machine. You can download it from FFmpeg's official site.
MoviePy: Install the MoviePy library using pip:
bash
Copy code
pip install moviepy
Other Python Packages: Ensure the required Python packages are installed:
bash
Copy code
pip install os time
How to Use
Clone the Repository: Clone this repository to your local machine.

bash
Copy code
git clone https://github.com/yourusername/yourrepository.git
Navigate to the Project Directory:

bash
Copy code
cd yourrepository
Run the Script: Execute the main script to process and post videos.

bash
Copy code
python main.py
Configuration: Ensure you configure your Instagram API credentials and any other necessary settings in the script.

Detailed Steps for Video Processing
Video Resizing
The project handles video resizing using MoviePy and FFmpeg. Here is an example of how to resize a video using FFmpeg:

python
Copy code
from moviepy.editor import VideoFileClip

def resize_video(input_path, output_path, width, height):
    clip = VideoFileClip(input_path)
    resized_clip = clip.resize(newsize=(width, height))
    resized_clip.write_videofile(output_path, codec='libx264')
Handling Errors
During the resizing process, errors such as 0x80004005 can occur. Ensure your video dimensions and format are supported:

Check the video codec and format.
Validate the aspect ratio and resolution.
Additional Functionalities
File Management
A function to delete files in a directory:

python
Copy code
import os

def delete_files_in_folder(folder_path):
    for filename in os.listdir(folder_path):
        file_path = os.path.join(folder_path, filename)
        if os.path.isfile(file_path):
            os.remove(file_path)
        elif os.path.isdir(file_path):
            delete_files_in_folder(file_path)
    os.rmdir(folder_path)
Adding Delays
A function to add a delay:

python
Copy code
import time

def wait_for_seconds(seconds):
    time.sleep(seconds)
Conclusion
This project simplifies the process of preparing videos for Instagram by automating resizing and posting. With Python scripts and multimedia tools, it ensures that videos meet the required specifications efficiently. Follow the installation and usage guide to set up and run the project seamlessly.
