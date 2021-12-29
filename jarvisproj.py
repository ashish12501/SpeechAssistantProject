import pyttsx3 #pip install pyttsx3
import speech_recognition as sr #pip install speechRecognition
import datetime
import wikipedia #pip install wikipedia
import webbrowser
import os
import smtplib
#import rendom #random module for choosing numbers randomly


engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
# print(voices[1].id)
engine.setProperty('voice', voices[1].id)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good Morning!")

    elif hour>=12 and hour<18:
        speak("Good Afternoon!")   

    else:
        speak("Good Evening!")  

    speak("I am Zira Sir. Please tell me how may I help you")       

def takeCommand():
    #It takes microphone input from the user and returns string output

    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognizing...")    
        query = r.recognize_google(audio, language='en-in')
        print(f"User said: {query}\n")

    except Exception as e:
        # print(e)    
        print("Say that again please...")  
        speak("Say that again please")
        return "None"
    return query

def sendEmail(to, content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login('ashishyadav63887@gmail.com', 'BumbleBee@79')
    server.sendmail('ashishyadav63887@gmail.com', to, content)
    server.close()

if __name__ == "__main__":

    print("************************************************************************************************************************")
    print("                 ____   ___   ___  ___  ___ _   _        _   ___  ___  _____  ___  _____   _    _  _  _____")
    print("                |____  |___| |__  |__  |    |___|       /_\ |___ |___    |   |___    |    /_\  | \ |    | ")
    print("                 ____| |     |___ |___ |___ |   |      /   \ ___| ___| __|__  ___|   |   /   \ |  \|    | ")
    print("                                                                     ")
    print("************************************************************************************************************************")

    wishMe()
    while True:
    # if 1:
        query = takeCommand().lower()

        # Logic for executing tasks based on query
        if 'search for' in query:
            speak('Searching Wikipedia...')
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=2)
            speak("According to Wikipedia")
            print(results)
            speak(results)

        elif 'open youtube' in query:
            webbrowser.open("youtube.com")

        elif 'open google' in query:
            webbrowser.open("google.com")

        elif 'open stackoverflow' in query:
            webbrowser.open("stackoverflow.com")   


        elif 'play music' in query:
            music_dir = 'D:\\MUSIC\\for proj'
            songs = os.listdir(music_dir)
            print(songs)    
            os.startfile(os.path.join(music_dir, songs[0]))

        elif 'play video' in query:
            video_dir = 'D:\\MUSIC\\for proj'
            videos = os.listdir(video_dir)
            #print(songs)    
            os.startfile(os.path.join(video_dir, videos[1]))


        elif 'the time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")    
            speak(f"Sir, the time is {strTime}")

        elif 'open code' in query:
            codePath = "C:\\Users\\ay079\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
            os.startfile(codePath)

        elif 'open zoom' in query:
            zoomPath = "C:\\Users\\ay079\\AppData\\Roaming\\Zoom\\bin\\Zoom.exe"
            os.startfile(zoomPath)
        
        elif 'go to sleep' in query:
            speak("sorry to say you bye sir , call me whenever you need")
            exit()

        elif 'exit' in query:
            speak("sorry to say you bye sir , call me whenever you need")
            exit()
        
        elif 'how are you' in query:
            speak("I'm fine. you're very kind to ask , what can I do for you ?")
        
        elif 'joke' in query:
            speak('Where are average things manufactured?     The satisfactory.')
            

        elif 'hello' in query:
            speak("I'm listening, tell me what can I do for you ?")

        elif 'stone paper' in query:
            speak('choose any one , stone , paper , scissor')
            user = takeCommand()
            if user == "stone":
                speak('i chose scissor, you won')
            elif user == "scissor":
                speak('i chose paper , you won')
            elif user == "paper":
                speak('i chose scissor , i won')

        
            
        elif 'send an email to aparna' in query:
            try:
                speak("What should I say?") 
                content = takeCommand()
                to = "2000560100026@bbdniit.ac.in"    
                sendEmail(to, content)
                speak("Email has been sent!")
            except Exception as e:
                print(e)
                speak("Sorry my sir. I am not able to send this email")    
            
            
        elif 'send an email to aman' in query:
            try:
                speak("What should I say?") 
                content = takeCommand()
                to = "2000560100017@bbdniit.ac.in"    
                sendEmail(to, content)
                speak("Email has been sent!")
            except Exception as e:
                print(e)
                speak("Sorry my sir. I am not able to send this email")    
        
   
            
        elif 'send an email to ashish' in query:
            try:
                speak("What should I say?") 
                content = takeCommand()
                to = "2000560100033@bbdniit.ac.in"    
                sendEmail(to, content)
                speak("Email has been sent!")
            except Exception as e:
                print(e)
                speak("Sorry my sir. I am not able to send this email")    
                