def speak(article):
    
    import os
    os.environ["GOOGLE_APPLICATION_CREDENTIALS"]="./keys.json"
    
    title_save_location = "./audio/title.mp3"
    body_save_location = "./audio/body.mp3"
    
    """Synthesizes speech from the input string of text."""
    from google.cloud import texttospeech

    client = texttospeech.TextToSpeechClient()

    input_title = texttospeech.SynthesisInput(text=article["title"])
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
    with open(title_save_location, "wb") as out:
        out.write(response_title.audio_content)
        print('Audio content written to file: ' + title_save_location)
        
    # The response's audio_content is binary.
    with open(body_save_location, "wb") as out:
        out.write(response_body.audio_content)
        print('Audio content written to file: ' + body_save_location)
        
    save_locations = {
        "title": title_save_location,
        "body": body_save_location
    }    
    
    return save_locations