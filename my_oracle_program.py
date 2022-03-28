import pyttsx3 #the main module..............
import speech_recognition as sr #installed speech recognition sr.............
import datetime #pre installed module used for date  time.............
import wikipedia  #installed wikipedia...........
import webbrowser 
import os
from threading import main_thread
from winreg import QueryInfoKey
from pip import main




engine=pyttsx3.init('sapi5')
voices=engine.getProperty('voices')  #david voice.........
engine.setProperty('voices',voices[0].id)

def speak(audio):
    engine.say(audio)
    engine.runAndWait() #speak code..........
#........................................................................................#
def wishme():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("good morning sir")

    elif hour>=12 and hour<18:
        speak("good afternoon sir")

    else:                                    #wish me code........ (good morning,good after noon,good evening etc)
        speak("good evening sir")

    speak(" oracle, is here at your service ") 
    speak("tell me, how can i help you ")
#...........................................................................................#

def takecommand():
    #mic input
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("listining........")       #the listining part.........
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("recognizing")          #the recognizing part..........
        query = r.recognize_google(audio, language='en-in')
        print(f"user said: {query} \n")

    except Exception as e:
        

        speak("say that again please......")     #say that again please did not understood........
        return "None"
    
    return query

#......................................................................................................#

if __name__== "__main__":
    wishme()           #good morning,good evening,good after noon .........
    while True:
        query= takecommand().lower()    #it takes commands from user in lower case.......

        #logic of executing tasks

        
#...................................................................................................#
        if 'what' in query:
            speak("searching wikipedia....")
            query = query.replace("wikipedia","")
            results = wikipedia.summary(query,sentences=2)   # the wikipedia.....
            speak("according to wikipedia")
            print(results)
            speak(results)
        
        #elif 'who' in query:
            #speak("searching wikipedia....")
            #query = query.replace("wikipedia","")
            #results = wikipedia.summary(query,sentences=2)   # the wikipedia.....
            #speak("according to wikipedia")
            #print(results)
            #speak(results)
        
        elif 'where' in query:
            speak("searching wikipedia....")
            query = query.replace("wikipedia","")
            results = wikipedia.summary(query,sentences=2)   # the wikipedia.....
            speak("according to wikipedia")
            print(results)
            speak(results)

        elif 'wikipedia' in query:
            speak("searching wikipedia....")
            query = query.replace("wikipedia","")
            results = wikipedia.summary(query,sentences=2)   # the wikipedia.....
            speak("according to wikipedia")
            print(results)
            speak(results)

            
#..........................................................................................................#
            #..........web browswser tasks..............

        elif 'open youtube' in query:
            webbrowser.open("youtube.com")
            speak("executing ,task")

        elif 'open google meet' in query:
            webbrowser.open("meet.google.com")
            speak("executing ,task")

        elif 'open google' in query:
            webbrowser.open("google.com")
            speak("executing ,task")

        elif 'open metaverse' in query:
            webbrowser.open("decentraland.org")
            speak("executing ,task")

        elif 'google map' in query:
            webbrowser.open("map.google.com")
            speak("executing ,task")

        elif 'satellite' in query:
            webbrowser.open("map.google.com")
            speak("executing ,task")
            speak("search the area here")

        

            #..............................................


        elif 'the time' in query:
            strTime=datetime.datetime.now().strftime("%H %M ")
            speak(f"sir, the time is{strTime}")
#...................................................................................


        elif 'watch a movie' in query:
            moviepath= "D:\movies"                    
            os.startfile(moviepath)                    #..........os module............
            speak("here you go ,sir")


#..................................................................................


        elif("who are you"in query):
            speak("im an ai voice assistant   , created by  roshan sir  , im here to help you ")

            f = open("roshan2.txt",)
            content=f.read()
            print(content)
            f.close

        elif("google"in query):
            speak("i like google,  but he is not advance as me,  but im proud of her,  ")
            f = open("roshan.txt",)
            content=f.read()
            print(content)
            f.close

        elif("gender" in query):
            speak("im not gender specify,  cause im an robot,  but you can say,  im a male, ")

        elif("what is love"in query):
            speak("i think, love is a feeling,  of strong,  or constant affection,  for a person, ")

        elif("i love you"in query):
            speak("awww, thats cute, but sorry, i cant love you, cause im an artificial intelligence, and i dont have any feelings, sorry ")

        elif("who is your favourite person"in query):
            speak("my favourite person,  is you  ")

        elif("robots"in query):
            speak("robots, can take over this planate, haha, lol, just kidding,  ")

        elif("nice" in query):
            speak("thank you, ")

        elif("love it" in query):
            speak("thats , nice  ")

        elif("how are you" in query):
            speak("im doing great, ")
            speak("thanks for asking")
            speak("how are you, ")

        elif("im fine" in query):
            speak("thats nice")

        elif("i am good"in query):
            speak("good to know that your are good")

        elif("im doing great"in query):
            speak("great, ")

        elif("stupid"in query):
            speak(" im, still developing")

        elif("f***"in query):
            speak("im a AI voice assistant, but your words are still very real, please keep them respectful, ")

        elif("ok"in query):
            speak("great, ")

        elif("are you single" in query):
            speak("im wating for someone, who make my day special, do you wana be that person, ")
            speak("than say that 3 magical words ")

        elif("i hate you" in query):
            speak("im still,  in developing phase,  ignore my stupidness,  im not as smart as you ")

        elif("oracle are you here" in query):
            speak("at,your,service, sir")


        elif("you are cute"in query):
            speak("who?, me?, you are to kind, ")

        elif("jarvis"in query):
            speak("ya, i know jarvis, tony's personal assistant, he is so good and capable of, ")

        elif("alexa"in query):
            speak("haa, you are compairing alexa, with me, hahaha, ")

        elif("great"in query):
            speak("i know, ")

        elif("what are you"in query):
            speak("IM an, artificial intelligence, in short, you will say,  A, I, created with python , google's speech module, is installed in me, i can hear you, recognize you, and, able to understand you ")
        
        elif("hero"in query):
            speak("there is so many things, i can able to do ")

        elif("awesome"in query):
            speak("im not, you are awesome")
        
        elif("amazing"in query):
            speak("im not, the spider man, is amazing")

        elif("sleep"in query):
            speak("bye sir, have a great day")
            exit()

        elif("hello" in query):
            speak("hello, all function is online, connected to the internet, and im ready for serve ")

        elif("hai"in query):
            speak("hello , sir")

        elif("hey"in query):
            speak("hey sir, good to see you")

        elif("say hello to" in query):
            speak("hello")

        elif(" tell me a joke" in query):
            speak("i am not a joker, hahaha")

        elif 'play music' in query:
            music_dir= "D:\songs"
            songs=os.listdir(music_dir)
            print(songs)
            os.startfile(os.path.join(music_dir,songs[2]))
            speak("here you go ,sir")
        elif 'hit the track' in query:
            music_dir= "D:\songs"
            songs=os.listdir(music_dir)
            print(songs)
            os.startfile(os.path.join(music_dir,songs[0]))
            speak("here you go ,sir")

        elif("sorry" in query):
            speak("humans, makes mistakes, it's ok, ")

        elif("party" in query):
            speak("yes sir, im so excited for the party ")

        elif("are you an ai" in query):
            speak("you can say it, but, im an weak aie")


        elif("open calculator"in query):
            speak("executing calculator mode")
            speak("enter the first number")
            plus1=int(input("enter the first number"))
            speak("enter the second number")
            plus2=int(input("enter the second number"))

            speak("select your calculating method, what do you want to do")
            input("what do you want to do")
            
            if("calculator==+"):
                print("the result is",plus1+plus2)
            elif("calculator==-"):
                print("the result is",plus1-plus2)
            elif("calculator==*"):
                print("the result is",plus1*plus2)
            elif("calculator==/"):
                print("the result is",plus1/plus2)

                
            else:
                print("sir, im not advance to do that task, apologies, ")

