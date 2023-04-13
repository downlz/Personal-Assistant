import speech_recognition as sr
import pyttsx3
import datetime
import webbrowser
import os

# Initialize speech recognition and text-to-speech engines
r = sr.Recognizer()
engine = pyttsx3.init()

# Function to speak the given text
def speak(text):
    engine.say(text)
    engine.runAndWait()

# Function to recognize speech and return the text
def get_text():
    with sr.Microphone() as source:
        r.adjust_for_ambient_noise(source, duration=1)
        print("Listening...")
        audio = r.listen(source)
        try:
            text = r.recognize_google(audio)
            print(f"You said: {text}")
            return text
        except sr.UnknownValueError:
            speak("Sorry, I didn't understand that.")
        except sr.RequestError:
            speak("Sorry, there was an error processing your request.")

# Function to set a reminder
def set_reminder():
    speak("What should I remind you about?")
    reminder_text = get_text()
    speak("When should I remind you? Please provide the time in HH:MM format.")
    reminder_time = get_text()
    try:
        datetime.datetime.strptime(reminder_time, '%H:%M')
        speak(f"Okay, I will remind you to {reminder_text} at {reminder_time}.")
        os.system(f'echo "{reminder_text}" | at {reminder_time}')
    except ValueError:
        speak("Sorry, the time format is incorrect. Please provide the time in HH:MM format.")

# Function to create a to-do list
def create_todo_list():
    speak("Please tell me the tasks you want to add to the to-do list, one by one. Say 'done' when you're finished.")
    tasks = []
    while True:
        task = get_text().lower()
        if task == "done":
            break
        tasks.append(task)
    speak("Here's your to-do list.")
    for i, task in enumerate(tasks):
        speak(f"Task {i+1}: {task}")

# Function to search the web
def search_web():
    speak("What do you want to search for?")
    query = get_text()
    url = f"https://www.google.com/search?q={query}"
    webbrowser.open(url)
    speak(f"Here's what I found for {query} on Google.")

# Main loop
speak("Hi, I'm your voice assistant. How can I help you?")
while True:
    text = get_text().lower()
    if "set reminder" in text:
        set_reminder()
    elif "create to-do list" in text:
        create_todo_list()
    elif "search web" in text:
        search_web()
    elif "exit" in text or "bye" in text:
        speak("Goodbye!")
        break

