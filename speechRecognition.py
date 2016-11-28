import speech_recognition as sr
import pyaudio
import os
r=sr.Recognizer()
output=""
while output!="exit":
    print
    with sr.Microphone(device_index=2,sample_rate=44100,chunk_size=8192) as source:
        print("Say something!")
        audio=r.listen(source)
        print("Processing...")

    try:
        #print("Say something7!")
        print("You said "+r.recognize_google(audio))
        output=r.recognize_google(audio)
        if output=="hello":
            print("Hello! How are you today?")
        #print("Say something3!")
    except LookupError:
        print("I could not understand, what you said")
        #print("Say something4!")
    except sr.UnknownValueError:
        print("I could not understand, what you said")
        #print("Say something5!")
    except sr.RequestError as e:
        print("Could not I wanna try smtn request results from Google Speech Recognition service; {0}".format(e))
        #print("Say something6!")
"""import speech_recognition as sr
import pyaudio
r=sr.Recognizer()
with sr.Microphone(device_index=1) as source:
    audio=r.listen(source(

try:
    print(r.recognize_google(audio))
except sr.UnknownValueError:
    print("I could not understand, what you said")
except sr.RequestError as e:
    print("Could not request results from Google Speech Recognition service; {0}".format(e))"""
#    print("You said "+r.recognize_google(audio,key="GOOGLE_SPEECH_RECOGNITION_API_KEY"))

