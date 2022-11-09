def check(json_caption_data):
    
    import pickle
    
    with open("./content/og_article_content.dat", "rb") as f:
        article_content = pickle.load(f)
        
    
    
    for name in json_caption_data:
        text = article_content[name]
        caption_data = json_caption_data[name]