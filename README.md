# Short-Video-Auto-Generation

## Description

This is an attempt to automate generation of short videos that are prelevant in short-content type platforms like Instagram Reels, Youtube Shorts etc. The primary motivation is to handle videos of various dimensions and ensure that they compile in a proper manner without manual intervention. The only manual intervention involved in this project is just to run the 'main.py' script. The solution leverages FFmpeg for video processing and Python scripts to automate tasks, making it efficient and reliable. This project helped to explore the moviepy library and its capabilities.

## Technologies Used

   **Python:** <br>
    The application was built using Python 3.10.4 and its libraries.
<br>    
   **Reddit API Integration:** <br>
    Used to fetch video content directly from Reddit. This allows for automated retrieval and processing of videos posted on Reddit.
<br>    
   **FFmpeg:** <br>
    A powerful multimedia framework used to decode, encode, and merge layers of any multimedia content. It ensures videos are processed and encoded to meet Instagram's specifications.
 <br>   
   **MoviePy:** <br>
    A Python library for video editing, used for tasks like resizing and adding effects to videos. MoviePy simplifies complex video editing tasks with a straightforward API.
<br>    
   **Time Module:** <br>
    To add delays in the script where necessary. It is particularly useful for creating pauses between tasks to ensure proper sequencing and timing. <br>
<br>
   **Praw:** <br>
    This is a crucial library used to interact with the REDDIT API. <br>
<br>
   **Youtube-dlp:** <br>
    This is built on Youtube-dl which is further built on youtube-dlc as these libraries became inactive, It is a command-line interface that provides <br>
    support for hundreds of websites that have provide multimedia content. Using subprocess module, was able to simulate CLI commands through a python method itself.
    Github link - https://github.com/yt-dlp/yt-dlp


## Sample Output Videos Created

Find a few sample generated videos in the output folder of the repository
The file name of the file represents the subreddit it was picked up from.


## Prerequisites

  Python 3.6+: <br>
    Ensure you have Python installed on your machine. You can download it from Python's official site.
    
  FFmpeg: <br>
    Install FFmpeg on your machine as it will be needed for performing the resizing and merging opereations. 
    You can download it from FFmpeg's official site here - https://ffmpeg.org/download.html
    
  Dependency list: <br>
    You may download the libraries needed from the 'requirements.txt' file. Its preferred to do so in a virtual environment in order to avoid<br> 
    any dependency conflicts. <br> <br>
    For more information on how to use venv, refer the following resoure - https://docs.python.org/3/library/venv.html


## Installation Guide

Once you have downloaded all the pre requisited, you may proceed with installation.

### 1. Clone the Repository: <br>
Clone this repository to your local machine. Run the command in the command prompt or using git bash.

```
git clone https://github.com/ALANT535/Short-Video-Auto-Generation
```

### 2. Navigate to the Project Directory:

Run the following command to change the working directory
```
cd /path/to/your/downloaded/repo
```

### 3. Create your Reddit API key

1. Create / Log into your reddit account
2. Go to the following link - [https://www.reddit.com/prefs/apps]()
3. Create an app by filling in the details.
4. Once created, note down your secret key and secret client id.
5. These will be used to query Reddit through their API.


### 4. Update Reddit API details

Once received the client_id, client_secret, user_agent, update these details in the "get_details.py" file in the "src" folder.

Also update the "User Agent" key value pair in the get_post_details() function in the same file. Although you may use the same app name and the only reason to name is something is to make your requests to the REDDIT API unique. Otherwise, what was happening was that your request would be considered with every other person doing an API call which lead to data not being fetched due to the API's restrictions on the number of calls placed. By providing our own "User Agent" value as the app_name, we make our requests a part of requests that originate from our machine, thus ensuring that not too many calls are made and the data unfetchable.


### 5. Run the Script

Select the subreddit you want to select videos from by updating the "subreddit" variable in the main.py file.
Select the standard width you want to consider while merging and resizing of the video clips. By default, this is set to 720 and is advised to not modify this unless aware of possible implications.

Once these two variables have been set, execute the main.py script to process and generate the required video.

## NOTE

1. It's important that the code is run from the working directory of the project. As the paths have been built assuming that. Although it was possible to make the paths completely independent by using abspath(__file) function of the os module, I thought it would impact readability of the code and so choose to make that tradeoff.

2. Also note that once completed execution, the generated video is stored in the output folder of the project directory. Any temporary files used during the creation of the video are deleted and you dont have to be worried about them.

3. As for the excel file, I realise its not the best form of storing data, but it was the easiest at this time and thus chose to do it that way.

## Conclusion
This project simplifies the process of preparing videos of short-form content by automating resizing and posting. With Python scripts and multimedia tools, it ensures that videos meet the required specifications efficiently. Follow the installation and usage guide to set up and run the project seamlessly. It was fun working and looking forward to working on more of such.

***

## Future Scope
Will try to add a UI for this maybe.

Disclaimer: The proposed system should be deployed and used responsibly, adhering to all applicable laws and regulations regarding surveillance and privacy.
