# -*- coding: utf-8 -*-
# Author : Infinity Coderz
# https://www.youtube.com/channel/UC42MlfMpzlSuznz0X1kM2gw and subscribe me!

import pyttsx3
import speech_recognition as sr
import datetime
import os
import random
import requests
from requests import get
import wikipedia
import webbrowser
import sys
import cv2
from bs4 import BeautifulSoup
import time
import pyautogui
import geocoder
import operator
import pyjokes
import numpy as np
import PyPDF2
from pytube import Search
from qr_generator import qr_gen
from image_generator import img_gen

# Initialize the pyttsx3 engine
engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
print(voices[0].id)
engine.setProperty('voice', voices[0].id)
engine.setProperty('rate', 200)

def speak(audio):
    engine.say(audio)
    print(audio)
    engine.runAndWait()

def takecommand():
    # Initialize recognizer
    r = sr.Recognizer()
    
    try:
        with sr.Microphone() as source:
            print("listening...")
            r.pause_threshold = 1
            # Attempt to capture audio
            audio = r.listen(source, timeout=7, phrase_time_limit=7)
    except Exception as e:
        print("Error capturing audio:", e)
        print("Sorry, I couldn't hear you. Please try again.")
        return "none"  # Early return if audio is not captured

    try:
        print("Recognizing...")
        # Attempt to recognize the audio using Google Speech Recognition
        query = r.recognize_google(audio, language='en-in')
        print(f"user said: {query}")
    except sr.UnknownValueError:
        # Google Speech Recognition could not understand the audio
        print("Sorry, I didn't catch that.")
        return "none"
    except sr.RequestError as e:
        # Could not request results from Google Speech Recognition service
        print("Sorry, my speech service is down.")
        print(f"Google Speech Recognition error: {e}")
        return "none"
    except Exception as e:
        # Catch any other exceptions
        print(f"An error occurred: {str(e)}")
        return "none"
    
    return query


# to wish

def news():
    main_url = "http://newsapi.org/v2/top-headlines?sources=techcrunch&apiKey=a73b0e9fb9f442ecaf1bb286ed4b05ca"

    main_page = requests.get(main_url).json()
    articles = main_page["articles"]
    head = []
    day = ["first","second","third","fourth","fifth","sixth","seventh","eighth","ninth","tenth"]
    for ar in articles:
        head.append(ar["title"])
    for i in range (len(day)):
        speak(f"Today's {day[i]} news is: {head[i]}")

def wish():

    hour = int(datetime.datetime.now().hour)
    strTime = datetime.datetime.now().strftime("%I:%M:%S %p")
    if hour >= 0 and hour < 12:
        speak(f"good morning sir, its {strTime}")
    elif hour >= 12 and hour < 18:
        speak(f"good afternoon sir, its {strTime}")
    else:
        speak(f"good evening sir, its {strTime}")
    if 1:
        speak("Allow me to introduce myself. I am jarvis. the virtual artificial intelligence. I'am here to assist you with a variety of tasks . as best I can 24 hours a day. 7 days a week . importing all preferences from hub interface . system is about fully operational, please tell me how can i help you...")

def wish_me():
    strime = datetime.datetime.now().strftime("%d/%m/%Y")
    if strime == 15/8/2024:
        speak("Happy Independence day sir")
    elif strime == 26/1/2025:
        speak("Happy republic day sir")
    elif strime == 14/10/2024:
        speak("Happy birthday sir")
    elif strime == 1/1/2025:
        speak("Happy New Year sir!")

def search_youtube(search):
    YouTube = "https://www.youtube.com"
    webbrowser.open(YouTube)
    time.sleep(4)
    pyautogui.click(910, 138)
    time.sleep(1)
    pyautogui.write(search)
    pyautogui.press('enter')

def call_what(call_person):
    try:
        speak("Which type of call do you want to perform Video call, or Voice call")
        user_input = takecommand().lower()
        if "voice" in user_input:
            pyautogui.press('Win')
            time.sleep(0.5)
            pyautogui.write('Whatsapp')
            pyautogui.press('enter')
            time.sleep(1)
            pyautogui.write(call_person)
            time.sleep(1)
            pyautogui.click(338, 220)
            time.sleep(0.5)
            pyautogui.click(1820, 85)
            time.sleep(2)
            pyautogui.click(1889, 15)
        elif "video" in user_input:
            pyautogui.press('Win')
            time.sleep(0.5)
            pyautogui.write('Whatsapp')
            pyautogui.press('enter')
            time.sleep(2)
            pyautogui.write(call_person)
            time.sleep(1)
            pyautogui.click(338, 220)
            time.sleep(0.5)
            pyautogui.click(1761, 91)
            time.sleep(2)
            pyautogui.click(1889, 15)
    except Exception as w:
        speak(w)

def play_music_on_spotify(song_name):
    webbrowser.open("https://open.spotify.com/")
    time.sleep(6)
    pyautogui.hotkey("ctrl","shift","l")
    time.sleep(1)
    pyautogui.write(song_name)
    time.sleep(3)
    pyautogui.leftClick(805,515)

def message_what(message_person_name):
    try:
        speak("What should I say...")
        message_to_send = takecommand().lower()
        pyautogui.press('Win')
        time.sleep(0.5)
        pyautogui.write('Whatsapp')
        pyautogui.press('enter')
        time.sleep(2)
        pyautogui.write(message_person_name)
        time.sleep(1)
        pyautogui.click(338, 220)
        time.sleep(2)
        pyautogui.write(message_to_send)
        time.sleep(3)
        pyautogui.press('enter')
        time.sleep(2)
        pyautogui.click(1889, 15)
    except Exception as g:
        speak(g)

def read_pdf():
    try:
        book = open('python.pdf','rb')
        pdfReader = PyPDF2.PdfFileReader(book)
        pages = pdfReader.numPages
        speak(f"Total numbers of pages in this book is {pages}")
        speak("Sir, please enter the page number I have to read")
        pg = int(input("Please enter the page number : "))
        page = pdfReader.getPage(pg)
        text = page.extract_text()
        speak(text)
    except Exception as f:
        speak(f)

def alarm(query):
    timehere = open("Alarmtext.txt","a")
    timehere.write(query)
    timehere.close()
    os.startfile("alarm.py")

if __name__ == "__main__":
    wish()
    wish_me()
    while True:
        query = takecommand()

        # building logics to perform tasks

        if "open notepad" in query:
            speak("Opening notepad...")
            npath = "C:\\Windows\\System32\\notepad.exe"
            os.startfile(npath)

        elif "close notepad" in query:
            speak("Closing notepad...")
            os.system("taskkill /f /im notepad.exe")

        elif "call" in query:
            try:
                query = query.replace('call', '')
                query = query.replace('jarvis', '')
                call_what(call_person=query)
            except Exception as d:
               speak(d)

        elif "message" in query:
            try:
                query = query.replace('Jarvis send message to', '')
                query = query.replace('send message to', '')
                query = query.replace('Send message to', '')
                query = query.replace('papa ji', 'Papa JI')
                query = query.replace('jarvis', '')
                query = query.replace('Jarvis', '')
                query = query.replace('jarvis send a message to', '')
                query = query.replace('message to', '')
                query = query.replace('Message to', '')
                message_what(message_person_name=query)
            except Exception as f:
                speak(f)

        elif "off Wi-Fi" in query:
            pyautogui.hotkey('Win', 'A')
            pyautogui.press('space')

        elif "open" in query:
            query = query.replace('open', '')
            query = query.replace('Jarvis', '')
            query = query.replace('jarvis', '')
            query = query.replace('Open', '')
            pyautogui.press('Win')
            pyautogui.write(query)

        elif "on Wi-Fi" in query:
            pyautogui.hotkey('Win', 'A')
            pyautogui.press('space')

        elif "spotify" in query:
            try:
                query = query.replace('Spotify', '')
                query = query.replace('music', '')
                query = query.replace('play', '')
                query = query.replace('on', '')
                play_music_on_spotify(song_name=query)
            except Exception as f:
                speak(f)

        elif "who are you" in query:
            speak("Allow me to introduce myself. I am jarvis. the virtual artificial intelligence. I'am here to assist you with a variety of tasks . as best I can 24 hours a day. 7 days a week . importing all preferences from hub interface .system is about fully operational, please tell me how can i help you...")

        elif "open VS code" in query:
            apath = "C:\\Users\\PRATIBHA SINGH\\AppData\\Local\\Programs\\Microsoft VS Code\\code.exe"
            os.startfile(apath)
        elif "open file" in query:
            fvkj = "C:\\Windows\\explorer.exe"
            os.startfile(fvkj)
        elif "open microsoft edge" in query:
            epath = "C:\\Program Files (x86)\\Microsoft\\Edge\\Application\\msedge.exe"
            os.startfile(epath)
        elif "close microsoft edge" in query:
            speak("Closing microsoft edge...")
            os.system("taskkill /f /im msedge.exe")
        elif "open command prompt" in query:
            zpath = "C:\\Windows\\System32\\cmd.exe"
            os.startfile(zpath)

        elif "tell me" in query:
            try:
                query = query.replace("can you tell me", "")
                query = query.replace("tell me", "")
                query = query.replace("jarvis", "")
                results = wikipedia.summary(query, sentences=3)
                speak(results)
            except Exception as t:
                speak(t)

        elif "close vs code" in query:
            speak("closing visual studio code...")
            os.system("taskkill /f /im code.exe")

        elif "Thank you" in query:
            speak("welcome sir, please tell me how may I help you")

        elif "search YouTube" in query:
            try:
                query = query.replace('search', '')
                query = query.replace('jarvis', '')
                query = query.replace('Youtube', '')
                query = query.replace('youtube', '')
                query = query.replace('YouTube', '')
                search_youtube(query)
            except Exception as x:
                speak(x)

        elif "music" in query or "gana" in query:
            try:
                music_dir = "D:\Songs"
                songs = os.listdir(music_dir)
                rd = random.choice(songs)
                os.startfile(os.path.join(music_dir, rd))
                speak("As your wish sir")
            except Exception as d:
                speak(d)

        elif "close command prompt" in query:
            speak("Closing command prompt...")
            os.system("taskkill /f /im cmd.exe")

        elif "shut down" in query:
            zpath = "C:\\Windows\\System32\\cmd.exe"
            os.startfile(zpath)
            time.sleep(2)
            pyautogui.write("shutdown /s")
            pyautogui.press('enter')
            time.sleep(0.5)
            os.system("taskkill /f /im cmd.exe")

        elif "restart" in query:
            zpath = "C:\\Windows\\System32\\cmd.exe"
            os.startfile(zpath)
            time.sleep(2)
            pyautogui.write("shutdown /r")
            pyautogui.press('enter')
            time.sleep(0.5)
            os.system("taskkill /f /im cmd.exe")

        elif "ip address" in query:
            ip = get('https://api.ipify.org').text
            speak(f"your IP address is {ip}")

        elif "install python package" in query:
            speak("Sir, which package you want to install")
            sckfasjekcv = takecommand().lower()
            hrtpath = "C:\\Windows\\System32\\cmd.exe"
            os.startfile(hrtpath)
            time.sleep(1)
            pyautogui.write(f"pip install {sckfasjekcv}")
            pyautogui.press('enter')
            time.sleep(3)
            os.system("taskkill /f /im cmd.exe")

        elif "WSL" in query:
            zpath = "C:\\Windows\\System32\\cmd.exe"
            os.startfile(zpath)
            time.sleep(1)
            pyautogui.write("wsl")

        elif "ipl score" in query:
                    try:
                        from plyer import notification

                        url = "https://www.cricbuzz.com/"
                        page = requests.get(url)
                        soup = BeautifulSoup(page.text,"html.parser")
                        team1 = soup.find_all(class_ = "cb-ovr-flo cb-hmscg-tm-nm")[0].get_text()
                        team2 = soup.find_all(class_ = "cb-ovr-flo cb-hmscg-tm-nm")[1].get_text()
                        team1_score = soup.find_all(class_ = "cb-ovr-flo")[8].get_text()
                        team2_score = soup.find_all(class_ = "cb-ovr-flo")[10].get_text()

                        a = print(f"{team1} : {team1_score}")
                        b = print(f"{team2} : {team2_score}")

                        notification.notify(
                            title = "IPL SCORE :- ",
                            message = f"{team1} : {team1_score}\n {team2} : {team2_score}",
                            timeout = 15
                        )
                    except Exception as g:
                        speak(g)

        elif "QR code" in query:
            takecommand().lower()
            while True:
                qr_gen()

        elif "AI image" in query or "AI images" in query:
            try:
                img_gen()
            
            except Exception as h:
                speak(h)

        elif "alarm" in query:
            print("input time example:- 10 and 10 and 10")
            speak("Set the time")
            a = input("Please tell the time :- ")
            alarm(a)
            speak("Done,sir")

        elif "open camera" in query:
            speak("Opening webcam python...")
            cap = cv2.VideoCapture(0)
            while True:
                ret, img = cap.read()
                cv2.imshow('webcam',img)
                k = cv2.waitKey(50)
                if k==27:
                    break
            cap.release()
            cv2.destroyAllWindows()

        elif "wikipedia" in query:
            speak("searching to wikipedia...")
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=2)
            speak("according to wikipedia")
            speak(results)

        elif "write" in query:
            try:
                query = query.replace("write", "")
                pyautogui.write(query)

            except Exception as g:
                speak(g)

        elif "open youtube" in query:
            webbrowser.open("www.youtube.com")

        elif "hello jarvis" in query:
            speak("Hello sir, how can I help you ?")

        elif "play youtube shorts" in query:
            try:
                urls = [
                "https://www.youtube.com/shorts/"
                ]
                random_url = random.choice(urls)
                webbrowser.open(random_url)
                if "next" in query:
                    pyautogui.press('down')
            except Exception as e:
                speak(e)

        elif "open python package manager" in query:
            webbrowser.open("pypi.org")
        
        elif "pause" in query:
            pyautogui.press("k")
        elif "play" in query:
            pyautogui.press("k")
        elif "mute" in query:
            pyautogui.press("m")
        elif "full screen" in query:
            pyautogui.press("f")

        elif "read pdf" in query:
            read_pdf()

        elif "remember that" in query:
            query = query.replace("remember that","")
            query = query.replace("jarvis","")
            speak(f"You told me to remember that {query}")
            remember = open("Brain/remember.txt", "+a")
            remember.write(query)
            remember.close()

        elif "what do you remember" in query:
            remember = open("Brain/remember.txt","r")
            speak("You told me to remember that" + remember.read())

        elif "open mobile camera" in query:
            try:
                import urllib.request
                URL = "http://192.168.31.99:8080/shot.jpg"
                while True:
                    img_arr = np.array(bytearray(urllib.request.urlopen(URL).read()),dtype=np.uint8)
                    img = cv2.imdecode(img_arr,-1)
                    cv2.imshow('IPWebcam',img)
                    q = cv2.waitKey(1)
                    if q == ord("q"):
                       break

                    cv2.destroyAllWindows()
            except Exception as e:
                speak(e)

        elif "open pw"in query:
            webbrowser.open("https://www.pw.live/study/batches/study")

        elif "open my GitHub repository" in query:
            webbrowser.open("https://github.com/Infinity-coderz/")

        elif "next" in query:
            pyautogui.press('right')

        elif "open virtual machine" in query:
            gpa = "C:\\Program Files\\Oracle\\VirtualBox\\VirtualBox.exe"
            os.startfile(gpa)

        elif "open github" in query:
            webbrowser.open("github.com")

        elif "open python" in query:
            webbrowser.open("www.python.org")

        elif "tell me a joke" in query:
            my_jokes = pyjokes.get_joke(language="en", category="neutral")
            speak(my_jokes)
            
        elif "open app developer" in query:
            speak("Opening android studio...")
            andpath = "C:\\Program Files\\Android\\Android Studio\\bin\\studio64.exe"
            os.startfile(andpath)

        elif "battery" in query:
            import psutil
            battery = psutil.sensors_battery()
            percantage = battery.percent
            speak(f"Sir, our system has {percantage} percent battery")

        elif "search google" in query:
            try:
                query = query.replace("search", "")
                mpath = "C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe"
                os.startfile(mpath)
                time.sleep(1)
                pyautogui.write(query)
                pyautogui.press('enter')
            except ExceptionGroup as f:
                speak(f)

        elif "activate searching" in query:
            from pywikihow import search_wikihow
            speak("Searcing made is activated...")
            while True:
                speak("Please tell me what do you want to search")
                how = takecommand().lower()
                try:
                    if "exit" in how or "close" in how:
                        speak("Ok sir, searching mode is diactivated")
                        break
                    else:
                        max_results = 1
                        how_to = search_wikihow(how, max_results)
                        assert len(how_to) == 1
                        how_to[0].print()
                        speak(how_to[0].summary)
                except Exception as e:
                    speak("Sorry sir, I am not able to search this")

        elif "calculate" in query:
            try:
                r = sr.Recognizer()
                with sr.Microphone() as source:
                    speak("Sir, what do you want to calculate, for example: 3 plus 9")
                    print("Listening...")
                    r.adjust_for_ambient_noise(source)
                    audio = r.listen(source)
                my_string = r.recognize_google(audio)
                print(my_string)
                def get_operator_fn(op):
                    return {
                        '+' : operator.add,
                        '-' : operator.sub,
                        'x' : operator.mul,
                        'divided' : operator.__truediv__,
                    }[op]
                def eval_binary_expr(op1, oper, op2):
                    op1,op2 = int(op1), int(op2)
                    return get_operator_fn(oper)(op1, op2)
                speak("Result is :")
                speak(eval_binary_expr(*(my_string.split())))
            except Exception as s:
                speak(s)

        elif "open chat GPT" in query:
            webbrowser.open("https://chatgpt.com/")

        elif "close app developer" in query:
            speak("Closing android studio...")
            os.system("taskkill /f /im studio64.exe")

        elif "open facebook" in query:
            webbrowser.open("www.facebook.com")

        elif "activate friday" in query:
            fropateh = "C:\\Users\\PRATIBHA SINGH\\Documents\\friday.py"
            os.startfile(fropateh)
            sys.exit()

        elif "open stack overflow" in query:
            webbrowser.open("https://stackoverflow.com/")

        elif "open kali" in query:
            webbrowser.open("www.kali.org")

        elif "open google" in query:
            webbrowser.open("www.google.com")

        elif "open my website" in query:
            webbrowser.open("D:\webdev\HyDrex\index.html")

        elif "what's my location" in query:
            location = geocoder.ip('me')
            speak(f"Our location is {location.city},{location.state},{location.country}")
            print(f"Latitude : {location.latlng[0]}")
            print(f"Longitude : {location.latlng[1]}")
        elif "open calculator" in query:
            pyautogui.press('f12')

        elif "internet speed" in query:
            import speedtest
            st = speedtest.Speedtest()
            dl = st.download()
            up = st.upload()
            speak(f"Sir, we have {dl} bit per second downloading speed {up} bit per second uploading speed")

        elif "search google" in query:
            speak("sir, what should i search on google")
            cm = takecommand().lower()
            webbrowser.open(cm)

        elif "open chrome" in query:
            speak("Opening chrome browser...")
            mpath = "C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe"
            os.startfile(mpath)

        elif "close chrome" in query:
            speak("Closing chrome...")
            os.system("taskkill /f /im chrome.exe")
        
        elif "open hacker console" in query:
            speak("Opening metasploit framework...")
            slpatth = "C:\\metasploit\\console.bat"
            os.startfile(slpatth)

        elif "close hacker console" in query:
            speak("Cloasing metasploit framework...")
            os.system("taskkill /f /im console.bat")

        elif "the time" in query:
            strTime = datetime.datetime.now().strftime("%I:%M:%S %p")
            speak(f"Time is : {strTime}")
            if strTime >= "7:15:00 AM":
                speak("Hurry up! sir you have to reach to stop at 7:30 A.M")
            elif strTime == "11:00:00 PM":
                speak("GO to sleep sir")
            
        elif "what is date today" in query:
            strime = datetime.datetime.now().strftime("%d/%m/%Y")
            speak(f"The day is : {strime}")
            if strime == 15/8/2024:
                speak("Happy indepentence day sir")
            elif strime == 26/1/2025:
                speak("Happy republic day sir")
            elif strime == 14/10/2025:
                speak("Happy birthday day sir")

        elif "temperature" in query:
            try:
                search = "Temprature in delhi"
                url = f"https://www.google.com/search?q={search}"
                r = requests.get(url)
                data = BeautifulSoup(r.text,"html.parser")
                temp = data.find("div",class_="BNeawe")
                speak(f"current {search} is {temp}")
            except Exception as y:
                speak(y)

        elif "on bakelite" in query:
            speak("Turning on bakelites...")
            pyautogui.hotkey('fn', 'space')

        elif "open map" in query:
            maps = "C:\\Users\\PRATIBHA SINGH\\AppData\\Roaming\\Microsoft\\Windows\\Start Menu\\Programs\\Chrome Apps\\Google Earth.lnk"
            os.startfile(maps)

        elif "off bakelite" in query:
            speak("Turning off bakelites...")
            pyautogui.hotkey('fn', 'space')

        elif "open designer" in query:
            speak("Opening QT designer...")
            opath = "C:\\Program Files (x86)\\Qt Designer\\designer.exe"
            os.startfile(opath)

        elif "select all" in query:
            pyautogui.hotkey('Ctrl', 'A')

        elif "copy text" in query:
            pyautogui.hotkey('Ctrl', 'C')

        elif "paste here" in query:
            pyautogui.hotkey('Ctrl', 'V')

        elif "back" in query:
            pyautogui.press('backspace')
        elif "find" in query:
            pyautogui.hotkey('Clrl', 'F')
        elif "back all" in query:
            pyautogui.hotkey('Ctrl', 'backspace')
        elif "volume up" in query:
            pyautogui.press('volumeup')
        elif "volume down" in query:
            pyautogui.press('volumedown')
        elif "execute" in query:
            pyautogui.hotkey('Ctrl', 'right')
        elif "cut" in query:
            pyautogui.hotkey('Ctrl', 'X')
        elif "open play store" in query:
            aslpath = "C:\\Program Files\\Google\\Play Games\\Bootstrapper.exe"
            os.startfile(aslpath)
        elif "close play store" in query:
            speak("Closing Google play games beta...")
            os.system("taskkill /f /im Bootstrapper.exe")
        elif "save it" in query:
            pyautogui.hotkey('Ctrl', 'S')

        elif "switch the window" in query:
            pyautogui.keyDown('alt')
            pyautogui.press('tab')
            time.sleep(1)
            pyautogui.keyUp('alt')

        elif "tell me today's news" in query:
            speak("Please wait sir, fetching the latest news")
            news()

        elif "deactivate Jarvis" in query:
            speak("Ok mister stark, you can call me any time")
            speak("Deactivating jarvis...")
            sys.exit()

        elif "you can sleep now" in query:
            speak("Ok mister stark, you can call me any time")
            speak("Deactivating jarvis...")
            sys.exit()




