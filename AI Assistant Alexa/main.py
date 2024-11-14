import speech_recognition as sr  
import pyttsx3 
import pywhatkit  
import datetime 
import wikipedia  
import pyjokes  

listener = sr.Recognizer()  
engine = pyttsx3.init()  
voices = engine.getProperty('voices')  

import pyttsx3
import time

def talk(text):
    try:
        engine.say(text)
        engine.runAndWait()  
    except KeyboardInterrupt:
        print("Speech interrupted. Exiting...")
        exit(0)

def take_command():
    command = ""  
    try:
        with sr.Microphone() as source:
            print('Listening...')
            voice = listener.listen(source)
            print('Recognizing...')
            command = listener.recognize_google(voice)
            command = command.lower()

            if 'alexa' in command:
                command = command.replace('alexa', '')
                print(f"Command received: {command}")
    except sr.UnknownValueError:
        print("Google Speech Recognition could not understand the audio.")
    except sr.RequestError as e:
        print(f"Could not request results from Google Speech Recognition service; {e}")
    except Exception as e:
        print(f"Error: {e}")
    
    return command

def run_alexa():
    command = take_command()  
    if 'play' in command:
        song = command.replace('play', '')  
        talk('Playing ' + song)  
        pywhatkit.playonyt(song)  
    elif 'time' in command:
        time = datetime.datetime.now().strftime('%I:%M %p')  
        talk('The current time is ' + time)  
        print(time)  
    elif 'who is' in command:
        search = command.replace('who is', '')  
        info = wikipedia.summary(search, 5)  
        print(info)  
        talk(info)  
    elif 'tell me about' in command:
        search = command.replace('tell me about', '')  
        info = wikipedia.summary(search, 5)  
        print(info)  
        talk(info)  
    elif 'what is' in command:
        search = command.replace('what is', '')  
        info = wikipedia.summary(search, 5)  
        print(info)  
        talk(info)  
    elif 'date' in command:
        talk('Sorry, I have a headache')  
    elif 'are you single' in command:
        talk('Sorry, I am in a relationship')  
    elif 'joke' in command:
        talk(pyjokes.get_joke())  
        print(pyjokes.get_joke())  
    else:
        talk("I can't understand, can you repeat what you were saying?")  

while True:
    run_alexa()  
