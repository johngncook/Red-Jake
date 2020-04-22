import pyttsx3
import datetime
import speech_recognition as sr
import wikipedia


engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
#print(voices[1].id)
engine.setProperty('voice', voices[0].id)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def wish_Me():
    hour = int(datetime.datetime.now().hour)
    if hour >= 0 and hour < 12:
        speak ("Good Morning!")
    elif hour >= 12 and hour <18:
        speak("Good Afternoon")
    else:
        speak ("Good Evening!")

    speak (" I am Jarvis Sir. How may I help you today?")


# Takes micrphone input and returns string output
def takecommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognizing....")
        query = r.recognize_google(audio)
        print(f"User said: {query}\n")

    except Exception as e:
        #print(e)
        print("Say that again please...")
        return "None"

    return query


if __name__ == "__main__":
    wish_Me()
    while True:
        query = takecommand().lower()
        if 'wikipedia' in query:
            speak('Searching Wikipedia')
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=2)
            speak("According to Wikipedia")
            print(results)
            speak(results)

        else:
            speak('That is good to hear sir.')
            speak('If you need assistance, please let me know!')


    # Logic for executing tasks based on query


