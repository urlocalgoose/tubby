def rewrite(og_article_content):
    import openai
    import os
    import pickle
    import os

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
    openai.api_key = "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"

    rw_title = openai.Completion.create(
      model="text-davinci-002",
      prompt="rewrite text below in one sentence but keep the same length\n"+ og_article_content["title"] +"",
      temperature=1,
      max_tokens=2355,
      top_p=1,
      frequency_penalty=0.2,
      presence_penalty=0
    )
    title_response = dict(rw_title)
    openai_response = title_response['choices']
    wr_title = openai_response[-1]['text']

    # rewrite the body
    rw_body = openai.Completion.create(
      model="text-davinci-002",
      prompt="rewrite the text below in the style of a youtube video\n"+ og_article_content["body"] + "",
      temperature=1,
      max_tokens=2355,
      top_p=1,
      frequency_penalty=0.2,
      presence_penalty=0
    )
    body_response = dict(rw_body)
    openai_response = body_response['choices']
    wr_body = openai_response[-1]['text']

    wr_article_content = {
        "title": wr_title,
        "body": wr_body
    }

    return wr_article_content