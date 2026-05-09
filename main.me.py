import speech_recognition as sr
import webbrowser
import pyttsx3
import musiclibrary
import requests

recognizer = sr.Recognizer()
engine = pyttsx3.init()

def speak(text):
    engine.say(text)
    engine.runAndWait()

def processcommand(c):
    if "open google" in c.lower():
        webbrowser.open("https://google.com")
    elif "open youtube" in c.lower():
        webbrowser.open("https://youtube.com")
    elif "open facebook" in c.lower():
        webbrowser.open("https://facebook.com")
    elif "open linkedin" in c.lower():
        webbrowser.open("https://linkedin.com")
    elif "open instagram" in c.lower():
        webbrowser.open("https://instagram.com")                
    elif "open github" in c.lower():
        webbrowser.open("https://github.com")
    elif c.lower().startswith("play"):
        songs = c.lower().split(" ")[1]   # 🔧 yahan sirf ye fix kiya
        link = musiclibrary.music[songs]
        webbrowser.open(link)

def get_news():
    api_key = "YAHAN_APNI_NEWSAPI_KEY_DALO"
    url = f"https://newsapi.org/v2/top-headlines?country=pk&apiKey={api_key}"

    try:
        response = requests.get(url)
        data = response.json()

        articles = data.get("articles", [])

        if not articles:
            speak("Sorry, koi news nahi mili.")
            return

        speak("Yeh rahi aaj ki taaza khabrein")

        for i, article in enumerate(articles[:5]):
            title = article.get("title")
            print(f"{i+1}. {title}")
            speak(title)

    except Exception as e:
        print("News error:", e)
        speak("Sorry, is waqt news nahi laa sakti.")

if __name__ == "__main__":
    speak("initializing jarvis...")
    
    while True:
        # Mic se command lene ke liye
        # wake up when jarvis call..
        r = sr.Recognizer()
       
        print("recognizing...")
        try:
            with sr.Microphone() as source:
                print("Listening...")
                audio = r.listen(source, timeout=3, phrase_time_limit=2)
            
            command = r.recognize_google(audio)
            if (command.lower()=="jarvis"):
                speak("ya")
                #listen for comamnd
                with sr.Microphone() as source:
                 print("jarvis active")
                 audio = r.listen(source)
                 command=r.recognize_google(audio)

                 processcommand(command)
        except Exception as e:
            print("error:", e)