def utf8len(s):
    return len(s.encode('utf-8'))

def speak(article):
    
    # imports
    from google.cloud import texttospeech
    import os
    import spliter

    # load env vars
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


    # spilt text into a lenght less than 5000 bytes and but it snaps to the nearest period
    title = article["title"]
    full_body = article["body"]

    split_text = spliter.split(full_body)

    # initialize client
    client = texttospeech.TextToSpeechClient()

    # create title object
    input_title = texttospeech.SynthesisInput(text=title)

    # Settings and configs for the voice
    voice = texttospeech.VoiceSelectionParams(
        language_code="en-US",
        name="en-US-Neural2-E",
    )
    audio_config = texttospeech.AudioConfig(pitch=0.00, 
        audio_encoding=texttospeech.AudioEncoding.MP3
    )

    # send title to get speech
    response_title = client.synthesize_speech(
        request={"input": input_title, "voice": voice, "audio_config": audio_config}
    )
    
    # send body to get speech
    audio_segments = []
    for item in split_text:
        item = texttospeech.SynthesisInput(text=item)
        response_body = client.synthesize_speech(
            request={"input": item, "voice": voice, "audio_config": audio_config}
        )
        audio_segments.append(response_body)

    # The response's audio_content is binary.
    with open(TITLE_AUDIO_LOC, "wb") as out:
        out.write(response_title.audio_content)
        print('Audio content written to file: ' + TITLE_AUDIO_LOC)
        
    # The response's audio_content is binary.
    i = 0
    titles = []
    for item in audio_segments:
        title = "./audio/body_" + str(i) + ".mp3"
        titles.append(title)
        with open(title, "wb") as out:
            out.write(item.audio_content)
            print('Audio content written to file: ' + BODY_AUDIO_LOC)
        i = i+1
    return titles