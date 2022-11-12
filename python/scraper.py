

def scrape(link):
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
    
    # TEMP!!!!!!!!
    # im just gonna use pre determinded content for now

    article_content = {
        "title": "Astronomers May Have Just Discovered The Most Dangerous Object In The Universe",
        "body": """
       There are some terrifying things in deep space, including supermassive black holes, magnetars, and gamma-ray bursts. But for years, astronomers and physicists have theorised that something even more terrifying could be lurking out there…
       """
    }

    with open(OG_ARTICLE_LOC, "wb") as f:
        pickle.dump(article_content, f)

    return article_content