#assistant english
from gtts import gTTS
import os
from pydub import AudioSegment
from pydub.playback import play
import datetime
from time import sleep
import speech_recognition as sr
import wikipedia
import webbrowser
from io import BytesIO

#default query


#function for assistant speak
def speak(audio):
    mp3_fp = BytesIO()
    speak_obj = gTTS(text=audio,lang='en',slow=False)
    speak_obj.write_to_fp(mp3_fp)
    mp3_fp.seek(0)
    
    #Using pydub to play sound directly from bytes.
    speech = AudioSegment.from_file(mp3_fp,format="mp3")
    play(speech)
    
def wishMe():
    hour =int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good Morning!")
    elif hour>=12 and hour<18:
        speak("Good Afternoon!")
    else:
        speak("Good Evening!")
        
    speak("I am Kannya. How may i help you?")

def takeCommand():
    #query = 'quit'
    rec = sr.Recognizer()
    
    ################################################
    #printing list of microphones
    #for mic in sr.Microphone.list_microphone_names():
    #    print(mic,n)
    #    n=n+1
    #################################################
    
    with sr.Microphone(device_index=2) as source:
        print("Listening...")
        rec.pause_threshold=1
        audio = rec.listen(source)
        
    try:
        print("Recognizing....")
        query = rec.recognize_google(audio, language="en-in")
        print(f"User said :: {query}\n")
        
    except Exception as e:
        print(e)
    print(query)
    return query
    
if __name__=="__main__":
    wishMe()
    
    while True:
        query = takeCommand().lower()
        
        #logic for executing tasks
        if 'wikipedia' in query:
            speak('searching wikipedia....')
            query = query.replace("wikipedia","")
            results = wikipedia.summary(query,sentences=3)
            speak("According to wikipedia, ")
            print(results)
            speak(results)
            
        elif 'open youtube' in query:
            webbrowser.open("youtube.com")
            
        elif 'open google' in query:
            webbrowser.open("google.com")
            
        elif 'play music' in query:
            music_dir = "F:\songs"
            songs = os.listdir(music_dir)
            print(songs)
            os.startfile(os.path.join(music_dir,songs[0]))
            
        elif 'current time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"Sir, the time is {strTime}")
            
        elif 'quit' in query:
            break