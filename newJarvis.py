import pyttsx3
import datetime
engine = pyttsx3.init('sapi5')

hour = datetime.datetime.now()
# min = datetime.datetime.now()


engine.runAndWait()


def introduction():
    print("Introduction")
    engine.say("Hello sir! , I am Jarvish , developed by a programmar named Ashish Yadav, currently I'm in testing , what can I do for you?")
    engine.runAndWait()

def enquiry():
    print("enquiring")
    engine.say("sir. current user set to Ashish , should I change the user ")
    engine.say("         ")

def time():
    print("time zone")
    min = int(datetime.datetime.now().min)
    engine.say("sir the time is " )
    engine.say(hour)
    engine.say(min)

    engine.runAndWait()



# enquiry()
# introduction()
if __name__== "__main__":
    print("hello")