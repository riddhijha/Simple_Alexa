import speech_recognition as sr
import pyttsx3
import pywhatkit
import datetime
import wikipedia

listener =  sr.Recognizer()
engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice' , voices[1].id)

def talk(text):
    #engine.say("I am listening")
    engine.say(text)
    engine.runAndWait()

def listen_Me():  
    try:
        with sr.Microphone() as source:
            print('Listening...')
            voice = listener.listen(source)
            command = listener.recognize_google(voice)
            command =command.lower()
            if 'alexa'  in command:
                command = command.replace('alexa', '')
                # engine.say(command)
                # engine.runAndWait()
                print(command)
    except:
        pass
    return command


def play_Alexa():
    command = listen_Me()
    #print(command)
    if 'play' in command:
        song = command.replace('play', '')
        talk('Playing ' + song)
        pywhatkit.playonyt(song)
    elif 'time' in command:
        time = datetime.datetime.now().strftime('%I:%M:%S %p')
        print(time)
        talk('Current time is ' + time) 
    elif 'search' in command:
        word = command.replace('search' ,'')
        info = wikipedia.summary(word,1)
        print(info)
        talk(info)
play_Alexa()