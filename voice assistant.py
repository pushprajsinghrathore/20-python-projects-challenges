# pyttsx3 text  to speech  convter
import pyjokes
import pyttsx3
import speech_recognition as sr
import webbrowser # using for web searching
import datetime

def sptext(): # funcation define  sptext
    recognizer=sr.Recognizer() # speech recoganize varaible cretate
    with sr.Microphone() as source: # this line code to take  perfrom microphone process
        print("Listening.....") # ready to listen
        recognizer.adjust_for_ambient_noise(source) # unknow noise remove  from source
        audio= recognizer.listen(source)
        try:
            print("recoganizing;;;")
            data=recognizer.recognize_google(audio)
            print(data)
        except sr.unknowValueError:
            print("not understand")
def speechtx(x):
    engine=pyttsx3.init() # crate engine name varaible init() class
    voices=engine.getProperty('voices')
    engine.setProperty('voice',voices[1].id)# 1 denotes femal voice
    rate = engine.getProperty('rate')
    engine.setProperty('rate',120)
    engine.say(x)
    engine.runAndWait()
speechtx("hello welcome to AI how can i help you for your better yur life")

if __name__ =='__main__':
    if sptext().lower()=="hey jarvis":
        data=sptext().lower()

        if "your name" in data1:
            name=" my name is jarvis"
            speechtx(name)
        elif "old are you" in detal:
            age=" i am two year old"
            speechtx(age)

        elif "now time " in data1:
            time =datetime.datetime.now().strftime("%I%M%p")
            speechtx(time)
        elif " youtube" in data1:
            webbrowser.open("https://www.youtube.com/")
        elif "joke" in data1:
            joke_1=pyjokes.get_joke((language='en',category="netural"))
            speechtx(joke_1)
        elif "exit" in data1:
            break






