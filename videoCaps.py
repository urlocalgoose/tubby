# Import everything needed to edit video clips 
from moviepy.editor import *

def caption(caption_data):

    # loading video
    clip = VideoFileClip("./no_captions.mp4")

    #jason_data = json.dumps(json_caption_data)

    text_clips = []

    #print(json_caption_data)

    for segment in caption_data:

        txt_clip = TextClip(segment["Content"], fontsize = 100, color='white', align='center', size=(3000, 500))
        txt_clip = txt_clip.set_start(segment["Start"])
        duration = segment["Duration"]
        txt_clip = txt_clip.set_duration(duration)
        text_clips.append(txt_clip)
        #print("APPENDED!")

    segment_list=[]

    #for monologue in json_caption_data["monologues"]:
    #    current_segment = {}

    #for monologue in json_caption_data["monologues"]:
    #    print(monologue["elements"])
    #    for item in monologue["elements"]:
    #        try:
    #            print(item["value"])
    #            txt_clip = TextClip(item["value"], fontsize = 200, color='white', align='center', size=(1000, 500))
    #            txt_clip = txt_clip.set_start(item["ts"])
    #            duration = item["end_ts"] - item["ts"]
    #            txt_clip = txt_clip.set_duration(duration)
    #            text_clips.append(txt_clip)
    #            print("APPENDED!")
    #        except Exception:
    #            pass

    # Overlay the text clip on the first video clip 
    all_texts = CompositeVideoClip(text_clips)
    
    video = CompositeVideoClip([clip, all_texts.set_pos('center')])
    
    video.write_videofile("final.mp4")
    
#caption({"monologues": [
#    {"speaker": 0, "elements": [
#        {"type": "text", "value": "The", "ts": 0.2, "end_ts": 0.62, "confidence": 0.98}, 
#        {"type": "punct", "value": " "}, 
#        {"type": "text", "value": "sad", "ts": 0.62, "end_ts": 0.82, "confidence": 0.99}, 
#        {"type": "punct", "value": " "}, 
#        {"type": "text", "value": "fate", "ts": 0.82, "end_ts": 1.06, "confidence": 0.99}, 
#        {"type": "punct", "value": " "}, 
#        {"type": "text", "value": "of", "ts": 1.06, "end_ts": 1.26, "confidence": 0.99}, 
#        {"type": "punct", "value": " "}, 
#        {"type": "text", "value": "the", "ts": 1.26, "end_ts": 1.38, "confidence": 0.99}, 
#        {"type": "punct", "value": " "}, 
#        {"type": "text", "value": "ancient", "ts": 1.38, "end_ts": 1.66, "confidence": 0.99}, 
#        {"type": "punct", "value": " "}, 
#        {"type": "text", "value": "well", "ts": 1.77, "end_ts": 2.26, "confidence": 0.99}, 
#        {"type": "punct", "value": " "}, 
#        {"type": "text", "value": "shelled", "ts": 2.26, "end_ts": 2.62, "confidence": 0.83}, 
#        {"type": "punct", "value": " "}, 
#        {"type": "text", "value": "mariners", "ts": 2.62, "end_ts": 3.1, "confidence": 0.99}, 
#        {"type": "punct", "value": " "}, 
#        {"type": "text", "value": "is", "ts": 3.1, "end_ts": 3.38, "confidence": 0.99}, 
#        {"type": "punct", "value": " "}, 
#        {"type": "text", "value": "that", "ts": 3.38, "end_ts": 3.54, "confidence": 0.99}, 
#        {"type": "punct", "value": " "}, 
#        {"type": "text", "value": "they", "ts": 3.54, "end_ts": 3.7, "confidence": 0.99}, 
#        {"type": "punct", "value": " "}, 
#        {"type": "text", "value": "all", "ts": 3.7, "end_ts": 3.9, "confidence": 0.99}, 
#        {"type": "punct", "value": " "}, 
#        {"type": "text", "value": "drowned", "ts": 3.9, "end_ts": 4.34, "confidence": 0.99}, 
#        {"type": "punct", "value": "."}]}]})