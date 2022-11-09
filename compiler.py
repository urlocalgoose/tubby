from moviepy.editor import *

def compile():
    import pickle
    
    # content I need to grab:
    # Background gameplay
    # Background Music
    # Title and body Audio
    # Caption data

    # assign all the clip and audio locations
    bg_gameplay_location = './video/BackgroundDrivng.mp4'
    bg_music_location = './audio/Background.wav'
    title_audio_location = './audio/title.mp3'
    body_audio_location = './audio/body.mp3'
    two_second_silence_location = './audio/silent.mp3'

    # make those locations into clips, aka reading the files and stuff
    bg_gameplay_clip = VideoFileClip(bg_gameplay_location)
    bg_music_clip = AudioFileClip(bg_music_location)
    title_clip = AudioFileClip(title_audio_location)
    body_clip = AudioFileClip(body_audio_location)
    silence_clip = AudioFileClip(two_second_silence_location)

    # The plan:
    # layer 1: silence + title + silence + body
    # layer 2: background music overlaying the background video

    # layer 1
    layer_one_composite = concatenate_audioclips([silence_clip, title_clip, silence_clip.subclip(0, 1), body_clip])

    audio_duration = layer_one_composite.duration + 10

    # layer 2
    layer_two_audio = CompositeAudioClip([(bg_music_clip).fx(afx.volumex, 0.2), (layer_one_composite).fx(afx.volumex, 1.5)])

    final_composite = bg_gameplay_clip.set_audio(layer_two_audio).subclip(0, audio_duration)

    final_composite.write_videofile("no_captions.mp4")
    
    
    video = VideoFileClip("no_captions.mp4")
    video.audio.write_audiofile("no_captions_audio.mp3")

    return "./no_captions.mp4"