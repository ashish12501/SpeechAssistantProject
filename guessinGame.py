



from typing import Mapping
import pyttsx3

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
print(voices[0].id)
engine.setProperty('voice', voices[0].id)
def speak(audio):
    engine.say(audio)
    engine.runAndWait()





word = "Vector Academy"
guess = ""
guess_count = 0
count_limit = 3
status = False
    
while guess_count<count_limit and status == False:
    speak("Enter your guess")
    guess = input("Enter your guess : ")
    
    guess_count +=1
    if guess == word:
        speak("You won!")
        print ("You won!")
        status = True
    elif guess_count< count_limit and status==False:
        speak("Try again...")
        print("Try again...")

if status== False:
    speak("You lost...!")
    print("You lost...!")
