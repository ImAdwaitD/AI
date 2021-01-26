from urllib.parse import DefragResult
from urllib.request import DataHandler
import pyttsx3
import speech_recognition as sr
import datetime
import os
import cv2
from requests import get
import wikipedia
import webbrowser
from urllib.parse import quote
import pywhatkit as kit


engine = pyttsx3.init()
voices = engine.getProperty('voices')
# print(voices[1].id)
engine.setProperty('voices', voices[0].id)

def speak(audio):
    engine.say(audio)
    print(audio)
    engine.runAndWait()

def wish():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<=12:
        speak("good morning")
    elif hour>=12 and hour<=18:
        speak("good afternoon")
    else:
        speak("good evening")
    speak("Hello i am your a i. please tell me your command")

def takecommand():
    r= sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source, timeout=7, phrase_time_limit=5)

    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-in')
        print(f"You said {query}")

    except Exception as e:
        speak("Say that again")
        return "none"
    return query

if __name__=="__main__":
    wish()
     
    if 1:
        query = takecommand().lower()
        
        if "open notepad" in query:
            os.startfile(r'C:\WINDOWS\system32\notepad.exe')

        # elif "open cmd" or "open command prompt" in query:
        #     os.system('start cmd')
        
        elif "start camera" in query:
           cam = cv2.VideoCapture(0)
           while cam.isOpened():
                ret, frame1 = cam.read()
                if cv2.waitKey(10) == ord('q'):
                    break
                cv2.imshow('helloo', frame1)
        
        elif "ip address" in query:
            ip = get("https://api.ipify.org").text
            speak(f"your ip address is {ip}")

        elif "wikipedia" in query:
            speak("searching wikipedia..")
            query = query.replace("wikipedia", "")
            result = wikipedia.summary(query, sentences=2)
            speak(f"according to wikipedia, {result}")

        elif "open youtube" in query:
            webbrowser.open("www.youtube.com")

        elif "open stack overflow" in query:
            webbrowser.open("www.stackoverflow.com")

        elif "open google" in query:
            new = 2
            base_url = "http://www.google.com/?#q="
            speak("Please enter your search query: ")
            query = takecommand().lower()
            final_url = base_url + quote(str(query))
            webbrowser.open_new(final_url)

        elif "send whatsapp message" in query:
            speak("Please tell the number you want to send the message to...")
            number = takecommand().lower()
            str(number)
            speak("please tell the message you want to send..")
            msg = takecommand().lower()
            str(msg)
            now = datetime.datetime.now().hour.s
            now = int(datetime.datetime.strptime(now, "%H"))
            now_2 = int(datetime.datetime.now().minute + datetime.timedelta(minutes=2))
            kit.sendwhatmsg("+91"+number, msg, now, now_2)