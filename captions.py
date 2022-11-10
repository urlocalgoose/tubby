def caption(video_file_location):
    
    print("CPATIONGSDSF")
    
    # imports
    from rev_ai import apiclient
    import time
    import pickle
    
    video_file_location = "./no_captions_audio.mp3"

    # configs and stuff
    token = "02SWtG8u58xDydJP1F2xW8HbsVANF2JcC9d55DidBkN-1uhlKGxZTDm-bm2QikZ-RT43O_TImRg3ZZV8SdINKy4hBe1TM"
    
    # create your client
    client = apiclient.RevAiAPIClient(token)

    # try to send a local file
    try:
        # send a local file
        job = client.submit_job_local_file(video_file_location)
    except:
        print("failed, trying again...")
        time.sleep(1)
        job = client.submit_job_local_file(video_file_location)
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
        
    with open('./content/caption_data.srt', 'w') as f:
        f.write(captions)

    #return transcript_json
    return './content/caption_data.srt'
