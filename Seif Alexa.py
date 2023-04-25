from gtts import gTTS
import os
import playsound
import speech_recognition as sr
import datetime
import random
import requests
from bs4 import BeautifulSoup
import pywhatkit
import wikipedia
from googletrans import Translator, constants


LANG="en"
wikipedia.set_lang(LANG)
tranlator= Translator()
preReponses =["ok.","hi"]
headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36"}
def speak(text):
    tts=gTTS(text=text,lang=LANG)
    tts.save("hello.mp3")
    playsound.playsound("hello.mp3",True)
    os.remove("hello.mp3")

listener = sr.Recognizer()
def get_time():
    return datetime.datetime.now().strftime("%H:%M:%S")

def get_date():
    return datetime.datetime.now().strftime("%A %d/%m/%Y")



def listen():
    try:
        with sr.Microphone() as source:
            voice=listener.listen(source)
            command=listener.recognize_google(voice, language=LANG)
            if "alexa" in command:
                print(command)
                return command
            else:
                return " "    
      
    except:
        speak("i cannot understand your majesty")



def run():
    v=True
    while v:
        command=listen()
        if not command is None:
            i =random.randint(0,1)
            intro =preReponses[i]
            if "end" in command:
                v=False
            elif "clock" in command :
                speak(intro +". the clock now is ." + get_time())
            elif "date" in command :
                speak(intro +".  the date now is ." + get_date())
            elif "how are you" in command :
                speak(". i am good ....thanks god ." )
            elif "address" in command :
                speak(".  i live in cairo ." )
            elif "news" in command :
                URL = "https://www.bbc.com/arabic"
                page= requests.get(URL, headers=headers)
                soup = BeautifulSoup(page.content, "html.parser")
                l = [a.text for a in soup.select("div main ")]
                for a in l:
                    print(a)
                    speak(a)
            elif " i have a question" in command:
                question = command.replace("i have a question " , " ")
                question = question.replace("seif", "")
                URL = "https://www.google.co.ma/search?hl="+LANG+"&q="+question
                page = requests.get(URL, headers=headers)
                soup = BeautifulSoup(page.content, 'html.parser')
                result=""
                try:
                    result=soup.find(class_="HwtpBd gsrt PZPZlf kTOYnf").get_text()
                    speak(result)
                except:
                    pass 

            elif "song" in command or "music " in command or "Surah " in command or " Sorah"in command:
                command = command.replace("seif", "")
                speak(intro + "here you go" +command)
                pywhatkit.playonyt(command)

            elif " who is  " in command:
                command = command.replace("   who is ", " ")
                command = command.replace(" seif", " ")
                info= wikipedia.summary(command,1)
                speak(info)

                

    speak("good bye my creator    ")    

run()        


