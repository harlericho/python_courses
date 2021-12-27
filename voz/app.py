import pyttsx3
# Text a Voice
engine = pyttsx3.init()
# voice = 'spansih-latin-am'
voice = 'mbrola-es1'
engine.setProperty('voice', voice)
rate = engine.getProperty('rate')
engine.setProperty('rate', rate-50)
string = 'Hello my friend, how are you?'
engine.say(string)
engine.runAndWait()
