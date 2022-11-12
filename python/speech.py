def utf8len(s):
    return len(s.encode('utf-8'))

def speak(article):
    
    """Synthesizes speech from the input string of text."""
    from google.cloud import texttospeech
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

    client = texttospeech.TextToSpeechClient()

    input_title = texttospeech.SynthesisInput(text=article["title"])
    #if utf8len(article["body"]) > 5000:

    input_body = texttospeech.SynthesisInput(text=article["body"])

    # Note: the voice can also be specified by name.
    # Names of voices can be retrieved with client.list_voices().
    voice = texttospeech.VoiceSelectionParams(
        language_code="en-US",
        name="en-US-Neural2-E",
    )

    audio_config = texttospeech.AudioConfig(pitch=0.00, 
        audio_encoding=texttospeech.AudioEncoding.MP3
    )

    response_title = client.synthesize_speech(
        request={"input": input_title, "voice": voice, "audio_config": audio_config}
    )
    
    response_body = client.synthesize_speech(
        request={"input": input_body, "voice": voice, "audio_config": audio_config}
    )

    # The response's audio_content is binary.
    with open(TITLE_AUDIO_LOC, "wb") as out:
        out.write(response_title.audio_content)
        print('Audio content written to file: ' + TITLE_AUDIO_LOC)
        
    # The response's audio_content is binary.
    with open(BODY_AUDIO_LOC, "wb") as out:
        out.write(response_body.audio_content)
        print('Audio content written to file: ' + BODY_AUDIO_LOC)