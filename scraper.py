

def scrape(link):
    import pickle
    
    # TEMP!!!!!!!!
    # im just gonna use pre determinded content for now

    article_content = {
        "title": "The Sad Fate of the Ancient, Well-Shelled Mariners",
        "body": """
        In the Cambrian Period, 500 million years ago, the armored set ruled the seas. Soft-bodied animals secreted a mineral paste that hardened into protective shells of immense strength and deco beauty, some shaped like rams’ heads or eagles’ wings, others like champagne flutes studded with dagger-sharp spines.
But by the Devonian Period some 70 million years later, most of these brachiopods, briopods and related well-shelled mariners had gone extinct, victims of theft and their own extravagant ways."""
    }

    with open("./content/og_article_content.dat", "wb") as f:
        pickle.dump(article_content, f)

    return article_content