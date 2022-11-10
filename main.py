# this file is like a controller for the flow of the entire app, controlling user inout and stuff like that

# import local modules
import scraper
import rewriter
import speech
import captions
import checker
import compiler
import videoCaps
import srtParser

# import foreign modules

# configs and stuff
#wr_article_file_location = './content/article.txt'

# actually cool code

# scrape content
article_link = input("What do you wanna steal: ")
# returns a dictionary with title and body values
print("Scraping Content...")
og_article_content = scraper.scrape(article_link)
#
# rewrite content, just sends article content over to an AI rewriter, also saves the rewritten article to a file
# once again returns a dictionary, but with the rewritten contents
print("Rewriting Content...")
wr_article_content = rewriter.rewrite(og_article_content)

# make the text to speech audio files of our content and save them, returns dict of where the audio files are
print("Converting text to audio...")
audio_file_locations = speech.speak(wr_article_content)

# checks and ajusts the captions to make sure all of the words are accurate
#checker.check(wr_article_file_location, json_caption_data)

# compile all of the cool stuff we just made into one dope video
print("Compiling into pre caption video...")
video_file_location = compiler.compile()

# make the captions based off of the video, it saves them to a file as well, returns dictionary with json data of the captions
print("Getting speech to text data of video...")
video_file_location = "hsdhsbhdbhsb"
caption_data_unparsed = captions.caption(video_file_location)

caption_data_parsed = srtParser.pasre(caption_data_unparsed)

# creates the actauly final video based on the captions
print("Adding captions to video and rendering final product...")
videoCaps.caption(caption_data_parsed)