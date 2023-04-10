import speech_recognition  as sr
import pyaudio
import webbrowser
import pyttsx3
import urllib

x=True
url="https://www.google.com/search?q="
engine = pyttsx3.init()
chrome_path = r"C:\Program Files (x86)\Google\Chrome\Application\chrome.exe"
  
# First registers the new browser
webbrowser.register('chrome', None, 
                    webbrowser.BackgroundBrowser(chrome_path))

#engine.say("Hai")
#engine.runAndWait()
#print("sr version is " + sr.__version__)
r=sr.Recognizer()
def takeCommand():
    
    with sr.Microphone() as mp:
        engine.say("Hai welcome to voice search...please tell me secret code to proceed.")
        engine.runAndWait()
        r.pause_threshold = 1
        #r.energy_threshold=300
        code=r.listen(mp)
        if 'gayatri' or 'mohan' in code:
            engine.say("Please ask me how can i help you")
            engine.runAndWait()
            print("Listening...")
            r.pause_threshold = 2
            
            audio=r.listen(mp)
        
    try:


        print("Recognizing...")   
        query = r.recognize_google(audio)
        query = query.lower()
        print(query)
        engine.say(f"you requested for {query} ...here you go..")
        engine.runAndWait()
        #url+query
        print(f"User said: {query}\n")
        webbrowser.get('chrome').open(url+query)
            
    
    except Exception as e:
        
        print(e)   
        print("Unable to Recognize your voice.") 
        return "None"
        
    return query
takeCommand()
            

           
  

    