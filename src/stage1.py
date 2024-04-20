from pytube import YouTube
from moviepy.video.io.VideoFileClip import VideoFileClip
from moviepy.video.fx.all import resize
from moviepy.editor import VideoFileClip, ImageSequenceClip, ImageClip,clips_array
import cv2
import numpy as np

def download_youtube_video(video_id, output_path='downloaded_video.mp4'):
    youtube_url = f'https://www.youtube.com/shorts/ysA0u_wKg1Q'
    yt = YouTube(youtube_url)
    ys = yt.streams.get_highest_resolution()
    ys.download(output_path)


def crop_video(input_path, output_path, crop_coordinates):
    # Load the video clip
    clip = VideoFileClip(input_path)

    # Crop the video based on the specified coordinates
    cropped_clip = clip.crop(x1=crop_coordinates[0], y1=crop_coordinates[1], x2=crop_coordinates[2], y2=crop_coordinates[3])

    # Write the cropped video to a file
    cropped_clip.write_videofile(output_path, codec='libx264', audio_codec='aac')

# y coordinate is 1280
#x coordinate is 720
# Example usage: Crop from (100, 100) to (1100, 620)
crop_coordinates = (0, 200, 720, 960)
crop_video(r'C:\Users\LENOVO\Documents\Important_documents\VIT\Projects\IG_RIYAL\Project_Files\Output\Youre Describing My Dog.mp4', r'C:\Users\LENOVO\Documents\Important_documents\VIT\Projects\IG_RIYAL\Project_Files\Output\cropped.mp4', crop_coordinates)


#520 is left for the GTA video

#TESTING HOW TO DOWNLOAD A VIDEOaaaaas
# download_youtube_video('your_video_id', r'C:\Users\LENOVO\Documents\Important_documents\VIT\Projects\IG RIYAL\Virtual Environment\Output')

