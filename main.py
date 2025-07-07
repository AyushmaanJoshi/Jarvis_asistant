import speech_recognition as sr  # For converting speech to text
import webbrowser                # To open web pages in the default browser
import pyttsx3                   # For offline text-to-speech functionality
import musicLibrary              # Custom module: should contain a dictionary of songs and their URLs
import requests                  # For making HTTP requests (e.g., fetching news, jokes, facts)
import sys                       # For reliable program exit
from weather_module import get_weather  # Weather function in a separate file
import datetime                  # For time and date
import re                        # For calculator expression parsing and greeting feature
import random                    # For randomizing greeting responses
# Import the AI fallback function from client.py
from client import ask_ai_fallback  # <-- NEW FEATURE: For answering random questions

# -------------------- BASIC SETUP --------------------

# Owner information
OWNER_NAME = "Aaayushmaan"
OWNER_DESC = (
    "Aayushmaan is a passionate Python developer and technology enthusiast "
    "who created me to help with daily tasks, answer questions, and make life easier."
)

# Initialize the speech recognizer and text-to-speech engine
recognizer = sr.Recognizer()
engine = pyttsx3.init()
engine.setProperty('rate', 190)  # Set speaking speed (lower = slower)

# Your API keys
newsapi = "f0faf33211054f06a0c38cf0bb61a624"
weather_api_key = "dad1b1dcdc25e976c53ced00e8faedec"

# -------------------- HELPER FUNCTIONS --------------------

def speak(text):
    """
    Convert the given text to speech and play it aloud.
    """
    engine.say(text)
    engine.runAndWait()

def tell_joke():
    """
    Fetches a random joke from the Official Joke API.
    """
    try:
        response = requests.get("https://official-joke-api.appspot.com/random_joke")
        joke = response.json()
        return f"{joke['setup']} ... {joke['punchline']}"
    except Exception:
        return "Sorry, I couldn't fetch a joke right now."

def fun_fact():
    """
    Fetches a random fun fact from the Useless Facts API.
    """
    try:
        response = requests.get("https://uselessfacts.jsph.pl/random.json?language=en")
        fact = response.json()
        return fact["text"]
    except Exception:
        return "Sorry, I couldn't fetch a fun fact right now."

def calculate_expression(expression):
    """
    Evaluates a simple math expression from a string.
    """
    try:
        # Replace words with symbols for basic operations
        expr = expression.replace("plus", "+").replace("minus", "-") \
                         .replace("times", "*").replace("multiplied by", "*") \
                         .replace("divided by", "/").replace("over", "/")
        # Remove any non-math characters for safety
        expr = re.sub(r'[^0-9\.\+\-\*\/\(\) ]', '', expr)
        result = eval(expr)
        return f"The result is {result}."
    except Exception:
        return "Sorry, I couldn't calculate that."

def get_time_based_greeting():
    """
    Returns a greeting based on the current time of day.
    """
    hour = datetime.datetime.now().hour
    if 5 <= hour < 12:
        return "Good morning"
    elif 12 <= hour < 18:
        return "Good afternoon"
    elif 18 <= hour < 22:
        return "Good evening"
    else:
        return "Hello"

# -------------------- MAIN COMMAND PROCESSOR --------------------

def process_Command(c):
    """
    Process the user's command and perform the corresponding action.
    Supports opening popular websites, playing music, fetching news, weather, time, date, jokes, fun facts, calculator, greeting, owner info, and listing features.
    """
    c = c.lower()  # Convert command to lowercase for easier matching

    # 1. Greeting Feature: Jarvis greets anyone you ask
    greet_match = re.search(r"(greet|say hello to|say hi to|wish)\s+([a-zA-Z]+)", c)
    if greet_match:
        name = greet_match.group(2).capitalize()
        greetings = [
            f"{get_time_based_greeting()}, {name}!",
            f"Hi {name}, hope you're having a fantastic day!",
            f"Hello {name}! Wishing you all the best.",
            f"Hey {name}, nice to meet you!",
            f"{name}, I hope you have a wonderful day ahead!",
            f"Sending good vibes your way, {name}!"
        ]
        greeting = random.choice(greetings)
        print(greeting)
        speak(greeting)
        return

    # 2. Owner/creator info with multiple trigger phrases
    if any(phrase in c for phrase in [
        "who is your owner",
        "who made you",
        "who created you",
        "who programmed you",
        "who built you",
        "who developed you",
        "who is your creator"
    ]):
        response = f"My owner is {OWNER_NAME}. {OWNER_DESC}"
        print(response)
        speak(response)
        return

    # 3. "What can you do?" Feature: Jarvis lists its abilities
    if any(phrase in c for phrase in [
        "what can you do",
        "what are your features",
        "what commands do you support",
        "what can you perform",
        "how can you help me"
    ]):
        features = (
            "I can perform the following tasks by voice command:\n"
            "- Open popular websites like Google, YouTube, Facebook, and more.\n"
            "- Play songs from your music library.\n"
            "- Fetch and read out the latest news headlines.\n"
            "- Provide current weather updates for any city.\n"
            "- Tell you the current time and date.\n"
            "- Tell jokes and share fun facts.\n"
            "- Solve simple math expressions and calculations.\n"
            "- Greet anyone you ask me to.\n"
            "- Tell you about my creator.\n"
            "- Deactivate or exit on your command.\n"
            "Just ask me using natural language!"
        )
        print(features)
        speak(features)
        return

    # 4. Open popular websites based on keywords in the command
    if "open google" in c:
        webbrowser.open("https://google.com")
    elif "open youtube" in c:
        webbrowser.open("https://youtube.com")
    elif "open linkedin" in c:
        webbrowser.open("https://linkedin.com")
    elif "open facebook" in c:
        webbrowser.open("https://facebook.com")
    elif "open spotify" in c:
        webbrowser.open("https://spotify.com")
    elif "open twitter" in c:
        webbrowser.open("https://twitter.com")
    elif "open instagram" in c:
        webbrowser.open("https://instagram.com")
    elif "open reddit" in c:
        webbrowser.open("https://reddit.com")
    elif "open amazon" in c:
        webbrowser.open("https://amazon.com")
    elif "open gmail" in c:
        webbrowser.open("https://mail.google.com")
    
    # 5. Play a song if the command starts with "play"
    elif c.startswith("play"):
        parts = c.split(" ")
        if len(parts) > 1:
            song = parts[1]
            link = musicLibrary.music.get(song)
            if link:
                webbrowser.open(link)
            else:
                speak("Sorry, I couldn't find that song.")
        else:
            speak("Please specify the song name after 'play'.")

    # 6. Fetch and return news headlines if "news" is mentioned in the command
    elif "news" in c:
        r = requests.get(f"https://newsapi.org/v2/top-headlines?country=us&apiKey={newsapi}")
        if r.status_code == 200:
            data = r.json()
            headlines = [article['title'] for article in data.get('articles', [])]
            speak("Here are the latest headlines.")
            for headline in headlines[:5]:
                print(headline)
                speak(headline)
            return headlines
        else:
            print(f"Failed to fetch news: {r.status_code}")
            speak("Sorry, I couldn't fetch the news right now.")
            return []

    # 7. Weather updates
    elif "weather" in c:
        words = c.split()
        if "in" in words:
            city = words[words.index("in") + 1]
            weather_report = get_weather(city, weather_api_key)
            speak(weather_report)
        else:
            speak("Please specify a city, for example: 'weather in London'.")

    # 8. Time reporting
    elif "time" in c:
        now = datetime.datetime.now()
        current_time = now.strftime("%I:%M %p")
        speak(f"The current time is {current_time}.")

    # 9. Date reporting
    elif "date" in c:
        today = datetime.date.today()
        speak(f"Today's date is {today.strftime('%B %d, %Y')}.")

    # 10. Jokes
    elif "joke" in c:
        joke = tell_joke()
        speak(joke)

    # 11. Fun facts
    elif "fun fact" in c or "fact" in c:
        fact = fun_fact()
        speak(fact)

    # 12. Calculator for math expressions
    elif "calculate" in c or "what is" in c or "solve" in c:
        expr = c
        for trigger in ["calculate", "what is", "solve"]:
            if trigger in expr:
                expr = expr.split(trigger, 1)[1]
                break
        result = calculate_expression(expr)
        speak(result)

    # 13. If command is not understood
    # AI fallback for unrecognized commands (NEW FEATURE)
    else:
        # If the command is not recognized, ask the AI model for an answer
        response = ask_ai_fallback(c)
        print(response)
        speak(response)

# -------------------- MAIN LOOP --------------------

if __name__ == "__main__":
    speak("Initializing Jarvis...")  # Jarvis announces that it is starting
    recognizer = sr.Recognizer()

    while True:  # Outer loop: Always listening for the wake word
        try:
            with sr.Microphone() as source:
                print("Waiting for wake word ('Jarvis')...")
                audio = recognizer.listen(source, timeout=3)
            word = recognizer.recognize_google(audio)
            print(f"Wake word heard: {word}")
            if word.strip().lower() == "jarvis":
                speak("Yes, how can I help you?")
                print("Activated. Listening for commands. Say 'stop' to deactivate or 'exit'/'quit' to close.")
                speak("Activated. Listening for commands. Say 'stop' to deactivate or 'exit'/'quit' to close.")
                 
                while True:  # Inner loop: Listening for commands
                    with sr.Microphone() as source:
                        print("Listening for command...")
                        audio = recognizer.listen(source)
                    command = recognizer.recognize_google(audio)
                    command = command.strip().lower()
                    print(f"You said: {command}")

                    if command == "stop":
                        speak("Deactivating. Say 'Jarvis' to activate me again.")
                        print("Deactivated. Waiting for wake word again.")
                        break  # Go back to waiting for 'Jarvis'
                    elif command in ["exit", "quit"]:
                        speak("Goodbye!")
                        print("Exiting assistant.")
                        sys.exit()  # Use sys.exit() for reliable shutdown
                    else:
                        process_Command(command)
        except Exception as e:
            print("ERROR:", e)
