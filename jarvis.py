
''' 

Back-up Code

'''
'''


# import speech_recognition as sr
# import webbrowser
# import pyttsx3
# import musicLibrary
# import requests
# from client import ask_ai_fallback  # ⬅️ AI fallback now delegated to client.py

# # Initialize engines
# recognizer = sr.Recognizer()
# engine = pyttsx3.init()

# # API Key for NewsAPI
# newsapi = "f0faf33211054f06a0c38cf0bb61a624"

# def speak(text):
#     engine.say(text)
#     engine.runAndWait()

# def process_Command(c):
#     c = c.lower()

#     # Predefined websites
#     websites = {
#         "google": "https://google.com",
#         "youtube": "https://youtube.com",
#         "linkedin": "https://linkedin.com",
#         "facebook": "https://facebook.com",
#         "spotify": "https://spotify.com",
#         "twitter": "https://twitter.com",
#         "instagram": "https://instagram.com",
#         "reddit": "https://reddit.com",
#         "amazon": "https://amazon.com",
#         "gmail": "https://mail.google.com"
#     }

#     for key, url in websites.items():
#         if f"open {key}" in c:
#             webbrowser.open(url)
#             speak(f"Opening {key}")
#             return

#     # Music command
#     if c.startswith("play"):
#         parts = c.split(" ", 1)
#         if len(parts) > 1:
#             song = parts[1].strip()
#             link = musicLibrary.music.get(song)
#             if link:
#                 webbrowser.open(link)
#                 speak(f"Playing {song}")
#             else:
#                 speak("Sorry, I couldn't find that song.")
#         else:
#             speak("Please specify a song name.")
#         return

#     # News command
#     if "news" in c:
#         try:
#             r = requests.get(f"https://newsapi.org/v2/top-headlines?country=us&apiKey={newsapi}")
#             if r.status_code == 200:
#                 data = r.json()
#                 headlines = [article['title'] for article in data.get('articles', [])][:5]
#                 speak("Here are the top headlines.")
#                 for h in headlines:
#                     speak(h)
#             else:
#                 speak("Unable to fetch news at the moment.")
#         except:
#             speak("News service is currently unavailable.")
#         return

#     # AI Fallback using Azure GPT-4.1
#     speak("Let me check that for you.")
#     reply = ask_ai_fallback(c)
#     print("AI:", reply)
#     speak(reply)

# if __name__ == "__main__":
#     speak("Initializing Jarvis...")

#     while True:
#         try:
#             with sr.Microphone() as source:
#                 print("Listening for wake word...")
#                 recognizer.adjust_for_ambient_noise(source)
#                 audio = recognizer.listen(source, timeout=2)
#                 wake = recognizer.recognize_google(audio)

#             if wake.lower() == "jarvis":
#                 speak("Yes?")
#                 print("Activated.")

#                 with sr.Microphone() as source:
#                     audio = recognizer.listen(source)
#                     command = recognizer.recognize_google(audio)
#                     print("Command:", command)
#                     process_Command(command)

#         except sr.WaitTimeoutError:
#             pass
#         except Exception as e:
#             print("ERROR:", e)





# if __name__ == "__main__":
#     speak("Initializing Jarvis....")  # Announce initialization

#     while True:
#         # Create a new recognizer instance for each loop iteration
#         r = sr.Recognizer()

#         print("Recognizing")
#         try:
#             # Listen for the wake word using the microphone
#             with sr.Microphone() as source:
#                 print("Listening....")
#                 audio = r.listen(source, timeout=2)  # Listen for up to 2 seconds

#             # Convert the audio to text
#             word = r.recognize_google(audio)
#             if word.lower() == "jarvis":
#                 speak("Yaa")  # Respond to the wake word

#                 # Listen for the next command after activation
#                 with sr.Microphone() as source:
#                     print("Jarvis is now Activated Kindly speak")
#                     speak("Jarvis is now Activated Kindly speak")
#                     audio = r.listen(source)
#                     command = r.recognize_google(audio)
#                     process_Command(command)  # Process the user's command

#         except Exception as e:
#             print("ERROR")  # Print error message if something goes wrong
