def caption():
    
    # imports
    from rev_ai import apiclient
    import time
    import pickle
    from dotenv import load_dotenv
    import os

    # configs and stuff
    token = "02SWtG8u58xDydJP1F2xW8HbsVANF2JcC9d55DidBkN-1uhlKGxZTDm-bm2QikZ-RT43O_TImRg3ZZV8SdINKy4hBe1TM"
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
    
    # create your client
    client = apiclient.RevAiAPIClient(token)

    # try to send a local file
    try:
        # send a local file
        job = client.submit_job_local_file(NO_CAPS_AUDIO)
    except:
        print("failed, trying again...")
        time.sleep(1)
        job = client.submit_job_local_file(NO_CAPS_AUDIO)
        print("working...")
    # wait until the file is finished being transcribed
    job_details = client.get_job_details(job.id)
    while job_details.status.name != "TRANSCRIBED":
        # check job status
        job_details = client.get_job_details(job.id)
        print(job_details.status.name + "...")
        time.sleep(1)
    # retrieve transcript as JSON
    transcript_json = client.get_transcript_json(job.id)
    captions = client.get_captions(job.id)
    # delete the transcript from api server cause its not needed anymore
    client.delete_job(job.id)
        
    with open(CAPTION_DATA, 'w') as f:
        f.write(captions)

    #return transcript_json
    return captions
