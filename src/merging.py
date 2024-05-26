from moviepy.editor import VideoFileClip, concatenate_videoclips
import os
from PIL import Image

def merge_videos(video_clip_list, output_path):
    
    video_clips = [VideoFileClip(video_clip) for video_clip in video_clip_list]


    final_clip = concatenate_videoclips(video_clips,method="compose")


    final_clip.write_videofile(output_path, codec="libx264", audio_codec="aac")

videos = list(os.listdir(r"resized_clips"))
video_paths = [os.path.join("resized_clips",video) for video in videos]


output_path = os.path.join("resized_clips","merged_testing.mp4")

# merge_videos(video_paths , output_path)


# resized_clip = clip.resize(newsize=(new_width, new_height))

def resize_clip(input_path, output_path):
    # Load the video clip
    clip = VideoFileClip(input_path)
    
    # print(clip.size[0],clip.size[1],sep=" * ")
    # return
    
    # Resize the clip
    resized_clip = clip.resize(newsize = (720, clip.size[1] * (720 / clip.size[0])))
    
    # resized_clip.write_videofile(output_path, codec='libx264')
    resized_clip.write_videofile(output_path,verbose=True,codec="libx264",audio_codec='aac',temp_audiofile='temp-audio.m4a',remove_temp=True, preset="medium",ffmpeg_params=["-profile:v","baseline", "-level","3.0","-pix_fmt", "yuv420p"])
    
    # the error is consistent with the videos not having any audio
    # has something to do with that i think
    # try variations
    # seems to be an issue

# Example usage
resize_clip(r"output\video_681_720_.mp4",r"output\testing_resizing_2.mp4")