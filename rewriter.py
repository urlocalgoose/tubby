def rewrite(og_article_content):
    import openai
    import os
    import pickle
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
  prompt="edit the text below\n"+ og_article_content["body"] +"",
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