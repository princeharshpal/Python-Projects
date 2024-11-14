# # Ai Assistant - Alexa
# import speech_recognition as sr
# import pyttsx3
# import pywhatkit
# import datetime
# import wikipedia
# import pyjokes


# # engine_en = pyttsx3.init()  if want to add any other languages
# # engine_hi = pyttsx3.init()


# listener = sr.Recognizer()
# engine = pyttsx3.init()
# voices = engine.getProperty('voices')


# def talk(text):
#     engine.say(text)
#     engine.runAndWait()

# def take_command():
#     try:
#         with sr.Microphone() as source:
#             print('Listening...')
#             voice = listener.listen(source)
#             command = listener.recognize_google(voice)
#             command = command.lower()

#             if 'alexa' in command:
#                 command = command.replace('alexa', '')
#                 print(command)
#     except:
#         pass
#     return command

# def run_alexa():
#     command = take_command()
#     if 'play' in command:
#         song = command.replace('play', '')
#         talk('playing' + song)
#         pywhatkit.playonyt(song)
#     elif 'time' in command:
#         time = datetime.datetime.now().strftime('%I:%M %p')
#         talk('current time is ' + time)
#         print(time)
#     elif 'who is ' in command:
#         search = command.replace('who is', '')
#         info = wikipedia.summary(search,5)
#         print(info)
#         talk(info)
#     elif 'tell me about' in command:
#         search = command.replace('who is', '')
#         info = wikipedia.summary(search,5)
#         print(info)
#         talk(info)
#     elif 'what is' in command:
#         search = command.replace('what is', '')
#         info = wikipedia.summary(search,5)
#         print(info)
#         talk(info)
#     elif 'date' in command:
#         talk('sorry, i have headache')
#     elif 'are you single' in command:
#         talk('sorry, i am in a relationship')
#     elif 'joke' in command:
#         talk(pyjokes.get_joke())
#         print(pyjokes.get_joke())
#     else:
#         talk("I can't understand, can you repeat what you was saying ")

# while True:
#     run_alexa()

# Importing necessary libraries
import speech_recognition as sr  # For speech recognition
import pyttsx3  # For text-to-speech conversion
import pywhatkit  # For playing YouTube videos
import datetime  # For getting the current time
import wikipedia  # For searching information on Wikipedia
import pyjokes  # For telling jokes

# Initialize speech recognition and text-to-speech engine
listener = sr.Recognizer()  # Create a recognizer object to listen to audio
engine = pyttsx3.init()  # Initialize the text-to-speech engine
voices = engine.getProperty('voices')  # Get available voices (male/female)

# Function to make the assistant speak the provided text
import pyttsx3
import time

def talk(text):
    try:
        engine.say(text)
        engine.runAndWait()  # Wait for speech to finish
    except KeyboardInterrupt:
        print("Speech interrupted. Exiting...")
        exit(0)
#  Wait for the speech to complete

# Function to listen to and recognize the command given by the user
def take_command():
    command = ""  # Initialize command to an empty string
    try:
        with sr.Microphone() as source:
            print('Listening...')  # This will indicate that the app is listening
            voice = listener.listen(source)
            print('Recognizing...')  # Feedback to indicate recognition is happening
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



# Function to process and execute the recognized command
def run_alexa():
    command = take_command()  # Get the command from the user
    if 'play' in command:  # If the command contains 'play', play a song on YouTube
        song = command.replace('play', '')  # Extract the song name from the command
        talk('Playing ' + song)  # Notify the user that the song is being played
        pywhatkit.playonyt(song)  # Use pywhatkit to play the song on YouTube
    elif 'time' in command:  # If the command contains 'time', tell the current time
        time = datetime.datetime.now().strftime('%I:%M %p')  # Get the current time in 12-hour format
        talk('The current time is ' + time)  # Announce the current time
        print(time)  # Print the time for debugging
    elif 'who is' in command:  # If the command contains 'who is', search Wikipedia for the person
        search = command.replace('who is', '')  # Extract the person's name
        info = wikipedia.summary(search, 5)  # Get a brief summary from Wikipedia
        print(info)  # Print the summary for debugging
        talk(info)  # Read out the Wikipedia summary
    elif 'tell me about' in command:  # If the command contains 'tell me about', search Wikipedia for the topic
        search = command.replace('tell me about', '')  # Extract the topic name
        info = wikipedia.summary(search, 5)  # Get a brief summary from Wikipedia
        print(info)  # Print the summary for debugging
        talk(info)  # Read out the Wikipedia summary
    elif 'what is' in command:  # If the command contains 'what is', search Wikipedia for the topic
        search = command.replace('what is', '')  # Extract the topic name
        info = wikipedia.summary(search, 5)  # Get a brief summary from Wikipedia
        print(info)  # Print the summary for debugging
        talk(info)  # Read out the Wikipedia summary
    elif 'date' in command:  # If the command contains 'date', tell the assistant is having a headache
        talk('Sorry, I have a headache')  # Respond with a humorous message
    elif 'are you single' in command:  # If the command contains 'are you single', respond humorously
        talk('Sorry, I am in a relationship')  # Respond with a humorous message
    elif 'joke' in command:  # If the command contains 'joke', tell a random joke
        talk(pyjokes.get_joke())  # Use pyjokes to get a joke and speak it
        print(pyjokes.get_joke())  # Print the joke for debugging
    else:  # If the command is not recognized, ask the user to repeat
        talk("I can't understand, can you repeat what you were saying?")  # Ask the user to repeat

# Continuous loop to keep the assistant listening and responding
while True:
    run_alexa()  # Continuously run the Alexa assistant
