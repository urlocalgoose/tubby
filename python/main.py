# this file is like a controller for the flow of the entire app, controlling user inout and stuff like that

# import local modules
import scraper
import rewriter
import speech
import captions
import checker
import compiler
import addCaps
import srtParser
import parseOmatic

# import foreign modules
from dotenv import load_dotenv
import os

# configs and stuff
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

# scrape content
article_link = input("What do you wanna steal: ")
# returns a dictionary with title and body values
print("Scraping Content...")
og_article_content = scraper.scrape(article_link)


# rewrite content, just sends article content over to an AI rewriter, also saves the rewritten article to a file
# once again returns a dictionary, but with the rewritten contents
#print("Rewriting Content...")
#wr_article_content = rewriter.rewrite(og_article_content)

parseOmatic.weightLoss(og_article_content)

# make the text to speech audio files of our content and save them, returns dict of where the audio files are
#print("Converting text to audio...")
#audio_locs = speech.speak(wr_article_content)
#
## compile all of the cool stuff we just made into one dope video
#print("Compiling into pre caption video...")
#compiler.compile(audio_locs)
#
## make the captions based off of the video, it saves them to a file as well, returns dictionary with json data of the captions
#print("Getting speech to text data of video...")
#caption_data_unparsed = captions.caption()
#
#caption_data_parsed = srtParser.pasre(caption_data_unparsed)
#
## creates the actauly final video based on the captions
#print("Adding captions to video and rendering final product...")
#addCaps.caption(caption_data_parsed)