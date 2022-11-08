from cgitb import text
import os
import pyttsx3

text_speech = pyttsx3.init()

def speak():
    title = input("Title: ")
    body = input("Body:")
    
    text_speech.say(answer)
    text_speech.runAndWait()