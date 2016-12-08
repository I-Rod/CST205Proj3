import speech_recognition as sr
import pyaudio
import os
import datetime
import random
import pyowm
import webbrowser
r=sr.Recognizer()
output=""
time=datetime.datetime.now()
weatherphrase="what is the weather in"
jokes={1:"I'd tell you a chemistry joke, but I know I wouldn't get a reaction.",
2:"What is grey and can't fly? A parking lot.",
3:"Why don't some couples go to the gym? Because some relationships don't work out.",
4:"Why did the scientist install a knocker on his door? He wanted to win the No-bell prize.",
5:"If Apple made a car, would it have Windows?"}
def weatherForecast(city):
    owm=pyowm.OWM('5aade8c8e40d66b4d1b0897a9a485d52')
    observation=owm.weather_at_place(city)
    w=observation.get_weather()
    temperature=w.get_temperature('fahrenheit') 
    w.get_detailed_status()
    w.get_sunrise_time('iso')
    w.get_sunset_time('iso')
    print("Temperature: "+str(temperature['temp']))
    print("Current weather: "+str(w.get_detailed_status()))
    print("Sunrise: "+str(w.get_sunrise_time('iso')))
    print("Sunset: "+str(w.get_sunset_time('iso')))
while output!="exit":
    print
    with sr.Microphone(device_index=2,sample_rate=44100,chunk_size=8192) as source:
        print("Say something!")
        audio=r.listen(source)
        print("Processing...")

    try:
        print("You said "+r.recognize_google(audio))
        output=r.recognize_google(audio)
        if "hello" in output:
            print("Hello! Hope you're doing well today!")
        elif "what time is it" in output:
            print ("The time is "+str(time))
        elif "tell a joke" in output:
            print (jokes.get(random.randint(1,5)))
        elif "seriously" in output:
            print("Of course! I am a very serious speech recognition;)")
        elif "Google" in output:
           webbrowser.get('firefox').open_new('http://www.google.com/#q='+output[7:])
        elif "what is the weather in" in output:
            weatherForecast(output[22:])	    
    except LookupError:
        print("I could not understand, what you said 1")
    except sr.UnknownValueError:
        print("I could not understand, what you said")
    except sr.RequestError as e:
        print("Could not I wanna try smtn request results from Google Speech Recognition service; {0}".format(e))
print("Bye! See you soon!")
