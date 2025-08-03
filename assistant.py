import speech_recognition as sr
import pyttsx3 
import datetime
import webbrowser

engine = pyttsx3.init()
engine.setProperty('rate', 150)  # speaking speed

def speak(text):
    print("🤖 Assistant:", text)
    engine.say(text)
    engine.runAndWait()

def listen():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("🎙️ Listening...")
        audio = r.listen(source)
        try:
            command = r.recognize_google(audio)
            print("🗣️ You said:", command)
            return command.lower()
        except sr.UnknownValueError:
            speak("Sorry, I didn't catch that.")
        except sr.RequestError:
            speak("Sorry, network issue.")
        return ""

def main():
    speak("Hello! I am your voice assistant. What can I do for you?")

    while True:
        command = listen()

        if 'time' in command:
            time_now = datetime.datetime.now().strftime("%I:%M %p")
            speak(f"The current time is {time_now}")

        elif 'date' in command:
            date_today = datetime.date.today().strftime("%B %d, %Y")
            speak(f"Today's date is {date_today}")

        elif 'your name' in command:
            speak("I am JARVIS, your virtual assistant.")

        elif 'open google' in command:
            speak("Opening Google...")
            webbrowser.open("https://www.google.com")

        elif 'exit' in command or 'stop' in command:
            speak("Goodbye! Have a nice day.")
            break

        elif command != "":
            speak("Sorry, I didn't understand that.")

if __name__ == "__main__":
    main()
