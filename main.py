import speech_recognition as sr
import os
import webbrowser
import pyttsx3 

def takeCommand():
    # Mic se command lene ke liye
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-in')
        print(f"User said: {query}\n")
    except Exception as e:
        print("Say that again please...")
        return "None"
    return query.lower()

if __name__ == "__main__":
    while True:
        query = takeCommand()

        # Commands yahan add karein
        if 'open notepad' in query:
            os.system("notepad.exe")
            
        elif 'open google' in query:
            webbrowser.open("google.com")
            
        elif 'open youtube' in query:
            webbrowser.open("youtube.com")

        elif 'exit' in query:
            print("Goodbye!")
            break