# -*- coding: utf-8 -*-
#   
#   snippet from my Artificially Intelligent Remote Assistant Robot Project, Ethiopia
#   created by Jamie Amdework
#   May 2015

#import libraries
import aiml
import sys
import time
import os
#prepare the brain (using aiml interpreter)
brain = aiml.Kernel()
#put conversation log on a test file
f = open("user_log.txt", "a")
print f
#identify user input and bot response
human = "you: "
humanstring = str(human)
bot = "bot: "
botstring = str(bot)
#load bunch of knowledge on brain
brain.learn("F:\python work\Standard\std-startup.aiml")
brain.learn("F:\python work\Standard\new_howmany.aiml")
brain.learn("F:\python work\Standard\jokes.aiml")
brain.learn("F:\python work\Standard\calendar.aiml")
brain.learn("F:\python work\Standard\warnings.aiml")
brain.learn("F:\python work\Standard\ai.aiml")
brain.learn("F:\python work\Standard\personality.aiml")
brain.learn("F:\python work\Standard\AIML\aiml-en-us-foundation-alice.v1-0/*")
brain.learn("F:\python work\std-startup.aiml")

#k.setBotPredicate("name", "Taitu")

while True:
    #assign whatever the user inputs to input
    input = raw_input ("you:")
    #write a log
    f.write(humanstring )
    f.write(input)
    #add new line
    f.write('\n')
    #if user inputs string exit, system will shutdown
    if input == "exit":
        f.write('\n')
        f.write('\n')
        #stop writing on file
        f.close
        #exit system
        sys.exit(0)
    #if user inputs play a music, it will seek for 1.mp3 in the user desktop and open it with default player    
    if input == "play a music":
        os.startfile('C:\\Users\\Jamie\\Desktop\\1.mp3')
    if input == "music":
        os.startfile('C:\\Users\\Jamie\\Desktop\\1.mp3')    
    #stop playing music
    if input == "enough":
        os.stopfile('C:\\Users\\Jamie\\Desktop\\1.mp3')    
    #bot's response
    response = brain.respond(input)
    #delay for response in ms
    time.sleep(1)
    #print bot's answer
    print response
    #write a log
    f.write(botstring)
    f.write(response)
    f.write('\n')
#watchout for "Warning: no match found for :" error. you need to handle your aiml script verywell.
#try updating the pyaiml version incase problem persists
    
#you may add espeak library if you want it to speak
#you may add GPIO pins commanding functions to acess raspberry pi     

