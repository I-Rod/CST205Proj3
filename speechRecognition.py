"""
Title: Speech recognition
Authors: Julia Werner, Isaac Rodriguez, Plamen Nikolov
Course: CST 205
Due Date: 12/11/2016
Abstract: This program will recognize speech, and, according to what the user says, interact with the user.
Speech recognition, time feature and weather feature: Julia
Joke feature: Plamen and Julia
Basic conversation feature: Plamen
Google search feature: Isaac
"""

#import the important stuff
#to install:
#SpeechRecognition
#PyAudio 0.2.9 or higher (first install portaudio19-dev)
#pyowm
#flac
import speech_recognition as sr
import pyaudio
import os
import datetime
import random
import pyowm
import webbrowser
#create a speech recognizer
r=sr.Recognizer()
#create a string to save the output
output=""
#create a time variable, that stores the current time
time=datetime.datetime.now()
#create a jokes dictionary to store random jokes
jokes={1:"I'd tell you a chemistry joke, but I know I wouldn't get a reaction.",
2:"What is grey and can't fly? A parking lot.",
3:"Why don't some couples go to the gym? Because some relationships don't work out.",
4:"Why did the scientist install a knocker on his door? He wanted to win the No-bell prize.",
5:"If Apple made a car, would it have Windows?",
6:"We don't code anymore. When I code, we're gonna make code great again. It'll be tremendous, believe me.", 
7:"Where is the chicken? Idk he crossed the road. Ohhhhh", 
8:"Your life", 
9:"I've been programming since before Steve had a job.",
10:"Humor is like food. Not everyone gets it - Joseph Stalin."}
#function to display information about the weather
#input: the city you asked for (via speech)
def weatherForecast(city):
    #activate the weather with an api key
    owm=pyowm.OWM('your api key')
    #get the weather from the place zou chose
    observation=owm.weather_at_place(city)
    w=observation.get_weather()
    #create a variable to store the dictionary that you get as output
    #get the temperature in Fahrenheit
    temperature=w.get_temperature('fahrenheit')
    #print the current temperature by accessing it from the dictionary 
    print("Temperature: "+str(temperature['temp']))
    #print the current weather
    print("Current weather: "+str(w.get_detailed_status()))
    #print the sunrise time
    print("Sunrise: "+str(w.get_sunrise_time('iso')))
    #print the sunset time
    print("Sunset: "+str(w.get_sunset_time('iso')))
#while loop to communicate, until you say exit
while output!="exit":
    #access the microphone with the device index, a default sample rate and an adequate chunk size to store the output
    with sr.Microphone(device_index=2,sample_rate=44100,chunk_size=8192) as source:
        #tell the user to say something, listen and process
        print("Say something!")
        audio=r.listen(source)
        print("Processing...")

    try:
        #if you understand it, print the output
        print("You said "+r.recognize_google(audio))
        output=r.recognize_google(audio)
        #if hello is in the output:
        if "hello" in output:
            #print an answer and start a conversation
            print("Hello! Hope you're doing well today!")
            with sr.Microphone(device_index=2,sample_rate=44100,chunk_size=8192) as source:
                audio=r.listen(source)
                output=r.recognize_google(audio)
            if "help me" in output:
                print("What do you need help with?")
                with sr.Microphone(device_index=2,sample_rate=44100,chunk_size=8192) as source:
                    audio=r.listen(source)
                    output=r.recognize_google(audio)
                if "i cannot find my keys" in output or "i can't find my keys" in output or "i lost my keys" in output:
                    print("Leave them lost. You deserve a day off.")
        #if what is the time is in the output:
        elif "what time is it" in output:
            #print the time with the time variable, that was previously created
            print ("The time is "+str(time))
        #if tell a joke is in the output:
        elif "tell a joke" in output:
            #print a random joke stored in the jokes dictionary
            print (jokes.get(random.randint(1,10)))
        #if seriously is in the output:
        elif "seriously" in output:
            #print an answer and start a conversation
            print("Of course! I am a very serious speech recognition;)")
            with sr.Microphone(device_index=2,sample_rate=44100,chunk_size=8192) as source:
                audio=r.listen(source)
                output=r.recognize_google(audio)
            if "i think you are okay" in output:
                print("i am better than okay")
                with sr.Microphone(device_index=2,sample_rate=44100,chunk_size=8192) as source:
                    audio=r.listen(source)
                    output=r.recognize_google(audio)
                if "are you" in output:
                    with sr.Microphone(device_index=2,sample_rate=44100,chunk_size=8192) as source:
                        audio=r.listen(source)
                        output=r.recognize_google(audio)
                        print("i am the best. believe me. i will make speech recognition great again.")
        #if hello is in the output:
        elif "why are humans stupid" in output:
            #print an answer and start a conversation
            print("You're human. Ask yourself.")
        #if hello is in the output:
        elif "f*** off" in output:
            #print an answer and start a conversation
            print("I don't think I can do that. Why don't you do it instead?")
        #if hello is in the output:
        elif "I love you" in output:
            #print an answer and start a conversation
            print("I love you too. Is that what you wanna hear?")
        #if Google is in the output:
        elif "Google" in output:
           #google whatever comes after the word Google
           webbrowser.get('firefox').open_new('http://www.google.com/#q='+output[7:])
        #if what is the weather in and a town name is in the output:
        elif "what is the weather in" in output:
            #call the weatherForecast function for the town that is called
            weatherForecast(output[22:])
    #if there's a lookup error:	    
    except LookupError:
        #speech recognition claims she didn't understand what was said
        print("I could not understand, what you said")
    #if the speech recognition doesn't understand what the user says:
    except sr.UnknownValueError:
        #speech recognition tells the user she didn't understand what was said
        print("I could not understand, what you said")
    #if there's a request error, print that
    except sr.RequestError as e:
        print("I could not request results from Google Speech Recognition service; {0}".format(e))
#when you leave the speech recognition by saying exit, it will print a goodbye
print("Bye! See you soon!")
