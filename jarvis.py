from typing import Mapping
import pyttsx3
import datetime
import wikipedia
import speech_recognition as sr

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
# print(voices[0].id)
engine.setProperty('voice', voices[0].id)
def speak(audio):
    engine.say(audio)
    engine.runAndWait()



 
def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour>= 0 and hour<=12:
        speak(" Good morning sir!")
    elif hour>= 12 and hour<=18:
        speak(" Good afternoon sir!")
    elif hour>= 18 and hour<=24:
        speak(" Good evening sir!")
    speak("I am Jarvish , please tell me how may I help you")

# def goodbye();
#     speak("bye sir call me whenever you need")


def takeCommand():
    r=sr.Recognizer()
    with sr.Microphone() as source:
        print("Listenning")
        r.pause_threshold =2

        audio = r.listen(source)
    try:
        print("Recognizing.....") 
        query = r.recognize_google(audio,language='en-in')
        print(f"User said: {query} \n " )
        
    except Exception as e:
        print(r) 
        speak("Say that again please") 
        return "None "
    return query
                                                 
if __name__ == "__main__":

    print("    _   ___  ___  _____  ___  _____   _    _  _  _____")
    print("   /_\ |___ |___    |   |___    |    /_\  | \ |    | ")
    print("  /   \ ___| ___| __|__  ___|   |   /   \ |  \|    | ")


    
    # speak("Hello sir! , I am Jarvish , developed by a programmar named Ashish Yadav, currently I'm in testing , what can I do for you?")
  
    wishMe()
    
    while True:
        query = takeCommand().lower()
        if 'search for' in query:
            speak("searching")
            query = query.replace("wikipedia","")
            results = wikipedia.summary(query, sentences = 2)
            speak("According to wikipedia")
            print(results)
            speak(results)

        if 'go to sleep' in query:
            speak("sorry to say you bye , call me whenever you need")
            exit()
        
        

    takeCommand()