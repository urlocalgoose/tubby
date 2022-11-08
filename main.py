# this file is like a controller for the flow of the entire app, controlling user inout and stuff like that

# import local modules
import scraper
import rewriter
import speech
import captions
import checker
import compiler

# import foreign modules

# configs and stuff
wr_article_file_location = './content/article.txt'

# actually cool code

# scrape content
article_link = input("What do you wanna steal: ")
# returns a dictionary with title and body values
og_article_content = scraper.scrape(article_link)

# rewrite content, just sends article content over to an AI rewriter, also saves the rewritten article to a file
# once again returns a dictionary, but with the rewritten contents
wr_article_content = rewriter.rewrite(og_article_content)

## make the text to speech audio files of our content and save them, returns dict of where the audio files are
audio_file_locations = speech.speak(wr_article_content)

## make the captions based off of the audio recording, it saves them to a file as well, returns captions file locations
captions_file_location = captions.caption(audio_file_locations)

## checks and ajusts the captions to make sure all of the words are accurate
#checker.check(wr_article_file_location, captions_file_location)
#
## compile all of the cool stuff we just made into one dope video
#compiler.compile()