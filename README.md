# CST205Proj3

Github Repo = https://github.com/I-Rod/CST205Proj3

Firstly, to properly use our project you must have pyaudio 0.2.9, pyttsx, pyowm (Weather app) and its API key, and speech_recognition installed. 
Our project is essentially a Siri clone with some conversational features including text and speech. It responds with weather, time, various
jokes, and can google upon command. It listens for a voice input, and depending on input, it either prints something or does something. The 
only mmajor problem was successfully using pyttsx. Unfortunately, there were some problems with packages within pyttsx, namely init.py and 
engine.py that could not be resolved. This prevents the voice feature from working as a response. This has no effect on speech recognition.
A minor snag was also the differences in pyaudio 0.2.8 and 0.2.9. Ubuntu was unable to recognize 0.2.9 without the use of a virtual 
environment, so please take that into consideration when installing. 

Future work: First and foremost we would need to solve the issues with pyttsx so that the app could respond with speech. Once we finish this
we could continue working on different features, like a calculator, opening programs, sending emails, playing music, and also creating 
alarms for other days. Pyttsx was definitely the hurdle for us in terms of creating a properly immersive and responsive  program, one in which the user
could feel involved with instead of just using and controlling it. This would have probably taken an additional few weeks.
