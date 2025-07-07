# 🧠 Jarvis - Your Voice Assistant in Python

Jarvis is an intelligent, voice-activated virtual assistant built in Python. It can perform a variety of daily tasks like telling jokes, fetching news, calculating expressions, reporting weather, and answering random questions using AI (via Azure + GPT-4.1).

---

## 🚀 Features

- 🎤 Voice Activation with wake-word "Jarvis"
- 🌐 Open popular websites (Google, YouTube, Spotify, etc.)
- 🎵 Play music from a custom song library
- 🗞️ Fetch latest news headlines (NewsAPI)
- ☀️ Get live weather updates (OpenWeather API)
- 🧠 AI fallback using GPT-4.1 (Azure Inference)
- 📅 Tell current time and date
- 🧮 Solve simple math expressions
- 🤖 Fun jokes & interesting facts
- 👋 Greet people with name recognition
- 👤 Introduce its creator and features
- 📤 Easily extendable and customizable

---

## 🛠️ Installation

### 1. Clone the repository

```bash
git clone https://github.com/AyushmaanJoshi/Jarvis_asistant.git
cd Jarvis_asistant
```

### 2. Create a virtual environment (recommended)

```bash
python3 -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. (macOS only) Fix PyAudio if needed

```bash
brew install portaudio
pip install pyaudio
```

---

## 🔧 Configuration

### API Keys

Update the following keys in your main file (or load them from `.env`):

- `newsapi`: [Get from NewsAPI.org](https://newsapi.org/)
- `weather_api_key`: [Get from OpenWeatherMap](https://openweathermap.org/api)
- `Azure GPT-4.1 token and endpoint`: From Azure AI Studio

---

## ▶️ Usage

```bash
python main.py
```

- Say “**Jarvis**” to activate the assistant.
- Then ask any command, e.g.:
  - “What’s the weather in Delhi?”
  - “Tell me a joke.”
  - “Open YouTube.”
  - “Calculate 7 times 8.”
  - “Greet Aman.”

To exit: say “**exit**” or “**quit**”.

---

## 📁 Project Structure

```
Jarvis_asistant/
├── main.py
├── client.py
├── weather_module.py
├── musicLibrary.py
├── requirements.txt
├── README.md
└── static/
```

---

## 📌 Dependencies

- `SpeechRecognition`
- `pyttsx3`
- `pyaudio`
- `requests`
- `azure-ai-inference`
- `flask` (if integrating with web UI)

---

## 💡 Future Improvements

- Add web dashboard with Flask
- Support Hindi/Multilingual commands
- Add note-taking & reminders
- Email or WhatsApp integration

---

## 👨‍💻 Author

**Ayushmaan Joshi**  
Third-year B.Tech CSE student at LPU | Python + AI enthusiast

📫 Connect on [LinkedIn](https://www.linkedin.com/in/ayushmaan-joshi)

---

## ⚠️ Disclaimer

This project is for educational purposes only. Do not expose or upload your API keys publicly. Keep your secrets in a `.env` file or environment variables.

---
