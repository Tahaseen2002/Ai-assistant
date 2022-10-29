import pyttsx3 #converts text to speech.used in python 2 and 3 versions
import datetime
import speech_recognition as sr # identifies voices
engine = pyttsx3.init('sapi5')#Speech api used to take voices of windows inbuilt voice
voices = engine.getProperty('voices')
#print(voices) 2 voices 1.David 2.Zira
engine.setProperty('voice',voices[1].id)


def speak(audio):
    engine.say(audio)
    engine.runAndWait();
def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12 :
        speak("Good Morning:)")
    elif hour>=12 and hour<18 :
        speak("Good Afternoon!")
    else:
        speak("Good Evening!")
        
    speak("I am Zari!! could you please tell me how may I help you  ?")
    
def takeCommand():
    #It takes Microphone input from user and return string output
    r = sr.Recognizer()#helps to recognise microphone voice
    with sr.Microphone() as source:
        print("Listening.....")
        r.pause_threshhold = 1 #seconds of non speakin audio before a phase is completed...When we are speaking if we stop for a second the phase should not complete because we stopped.
        audio = r.listen(source)
    try:
        print("Recognizing...")
        query = r.recognize_google(audio,Language='en-in')
        print(f"User Said: {query}\n")
        
    except Exception as e:
        print(e)
        print("Say that again please...")
        return "None"
    return query
        
    
            

     
if __name__ == "__main__":
    speak("Hi,Tahaseen!!!")
    wishMe()
    takeCommand()