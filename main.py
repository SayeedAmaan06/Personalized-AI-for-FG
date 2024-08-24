#Personalized Assistant for Financial Guidance
import speech_recognition as sr
import pyttsx3
import datetime
import gemini

r = sr.Recognizer()
engine = pyttsx3.init()

intro = "Iam your Personal financial Assistant, how can i help you"

current_time = datetime.datetime.now().time()
if current_time.hour < 12:

    engine.say(f"Good morning!, {intro}")
    engine.runAndWait()

elif current_time.hour < 17:
    engine.say(f"Good afternoon!, {intro}")
    engine.runAndWait()

else:
    engine.say(f"Good evening!, {intro}")
    engine.runAndWait()

with sr.Microphone() as source:
    print("Listening...")

    while True:
        audio = r.listen(source, phrase_time_limit=5)
        try:
            text = r.recognize_google(audio, language="en-US")
            print("You said: " + text)
            output = gemini.finance(text) 
            engine.say(output)
            engine.runAndWait()
        except sr.UnknownValueError:
            engine.say("Sorry, I didn't catch that. Please try again.")
            print("Didn't catch that. Try again!")
        except sr.RequestError as e:
            print("Error: " + str(e))
            