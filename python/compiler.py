from moviepy.editor import *

def compile():
    import pickle
    from dotenv import load_dotenv
    import os
    load_dotenv()
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
    
    # content I need to grab:
    # Background gameplay
    # Background Music
    # Title and body Audio
    # Caption data

    # make those locations into clips, aka reading the files and stuff
    bg_gameplay_clip = VideoFileClip(BACKGROUND_RETRO_CLIP_LOC)
    bg_music_clip = AudioFileClip(BACKGROUND_MUSIC_LOC)
    title_clip = AudioFileClip(TITLE_AUDIO_LOC)
    body_clip = AudioFileClip(BODY_AUDIO_LOC)
    silence_clip = AudioFileClip(SILENCE_AUDIO_LOC)

    # The plan:
    # layer 1: silence + title + silence + body
    # layer 2: background music overlaying the background video

    # layer 1
    layer_one_composite = concatenate_audioclips([silence_clip, title_clip, silence_clip.subclip(0, 1), body_clip])

    audio_duration = layer_one_composite.duration + 10

    # layer 2
    layer_two_audio = CompositeAudioClip([(bg_music_clip).fx(afx.volumex, 0.2), (layer_one_composite).fx(afx.volumex, 1.5)])

    final_composite = bg_gameplay_clip.set_audio(layer_two_audio).subclip(0, audio_duration)

    final_composite.write_videofile(NO_CAPS_VIDEO)
    
    
    video = VideoFileClip(NO_CAPS_VIDEO)
    video.audio.write_audiofile(NO_CAPS_AUDIO)