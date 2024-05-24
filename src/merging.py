from moviepy.editor import VideoFileClip, concatenate_videoclips
import os

def merge_videos(video_clip_list, output_path):
    
    video_clips = [VideoFileClip(video_clip) for video_clip in video_clip_list]


    final_clip = concatenate_videoclips(video_clips,method="compose")


    final_clip.write_videofile(output_path, codec="libx264", audio_codec="aac")

videos = list(os.listdir(r"output"))
video_paths = [os.path.join("output",video) for video in videos]


output_path = os.path.join("output","merged_testing.mp4")

merge_videos(video_paths , output_path)
