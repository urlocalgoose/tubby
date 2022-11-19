# Import everything needed to edit video clips 
from moviepy.editor import *

def caption(caption_data):

    import os

    GOOGLE_APPLICATION_CREDENTIALS = os.getenv('GOOGLE_APPLICATION_CREDENTIALS')
    BACKGROUND_RETRO_CLIP_LOC = os.getenv('BACKGROUND_RETRO_CLIP_LOC')
    BACKGROUND_MUSIC_LOC = os.getenv('BACKGROUND_MUSIC_LOC')
    SILENCE_AUDIO_LOC = os.getenv('SILENCE_AUDIO_LOC')
    CAPTION_DATA_LOC = os.getenv('CAPTION_DATA_LOC')
    TITLE_AUDIO_LOC = os.getenv('TITLE_AUDIO_LOC')
    BODY_AUDIO_LOC = os.getenv('BODY_AUDIO_LOC')
    OG_ARTICLE_LOC = os.getenv('OG_ARTICLE_LOC')
    NO_CAPS_AUDIO = os.getenv('NO_CAPS_AUDIO')
    NO_CAPS_VIDEO = os.getenv('NO_CAPS_VIDEO')
    FINAL_VIDEO = os.getenv('FINAL_VIDEO')
    CAPTION_DATA = os.getenv('CAPTION_DATA')

    # loading video
    clip = VideoFileClip(NO_CAPS_VIDEO)

    text_clips = []

    #print(json_caption_data)

    for segment in caption_data:

        txt_clip = TextClip(segment["Content"], fontsize = 100, color='white', align='center', size=(3000, 500), stroke_color='black', stroke_width=0)
        txt_clip = txt_clip.set_start(segment["Start"])
        duration = segment["Duration"]
        txt_clip = txt_clip.set_duration(duration)
        text_clips.append(txt_clip)
        #print("APPENDED!")

    segment_list=[]

    # Overlay the text clip on the first video clip 
    all_texts = CompositeVideoClip(text_clips)
    
    video = CompositeVideoClip([clip, all_texts.set_pos('center')])
    
    video.write_videofile(FINAL_VIDEO)