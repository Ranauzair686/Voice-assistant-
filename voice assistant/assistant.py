import speech_recognition as sr
import pyttsx3

# Initialize speech recognition
recognizer = sr.Recognizer()

# Initialize text-to-speech
engine = pyttsx3.init()

def recognize_speech():
    with sr.Microphone() as source:
        print("Listening...")
        recognizer.adjust_for_ambient_noise(source)
        audio = recognizer.listen(source)

    try:
        print("Recognizing...")
        query = recognizer.recognize_google(audio)
        print(f"User said: {query}")
        return query.lower()
    except sr.UnknownValueError:
        print("Sorry, I didn't get that. Please try again.")
        return ""
    except sr.RequestError:
        print("Sorry, could not request results. Please check your internet connection.")
        return ""

def speak(text):
    engine.say(text)
    engine.runAndWait()

def main():
    speak("Hello! I am your personal assistant. How can I help you today?")

    while True:
        query = recognize_speech()

        if "hello" in query:
            speak("Hello! How can I assist you?")
        elif "what is your name" in query:
            speak("I am a voice-controlled personal assistant.")
        elif "exit" in query:
            speak("Goodbye!")
            break
        else:
            speak("Sorry, I couldn't understand your request.")

if __name__ == "__main__":
    main()
