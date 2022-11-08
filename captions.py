
from rev_ai import apiclient
import time

token = "02SWtG8u58xDydJP1F2xW8HbsVANF2JcC9d55DidBkN-1uhlKGxZTDm-bm2QikZ-RT43O_TImRg3ZZV8SdINKy4hBe1TM"
filePath = "./audio/body.mp3"

# create your client
client = apiclient.RevAiAPIClient(token)

# send a local file
job = client.submit_job_local_file(filePath)

# check job status
job_details = client.get_job_details(job.id)

print(type(job_details))

time.sleep(100)

# retrieve transcript as JSON
transcript_json = client.get_transcript_json(job.id)

## retrieve transcript as a Python object
#transcript_object = client.get_transcript_object(job.id)
