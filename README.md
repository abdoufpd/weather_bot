# weather_bot
🌦️ Weather Checker Telegram Bot

A simple Telegram bot built with Python that provides real-time weather information for any city using the OpenWeatherMap API.

🚀 Features
🌍 Get current weather by city name
🌡️ Temperature (in Celsius)
💧 Humidity
🌅 Sunrise & 🌇 Sunset time
💬 Simple conversational responses
🤖 Works in both private chats and groups
🛠️ Tech Stack
Python 🐍
python-telegram-bot
OpenWeatherMap API
Requests library
📂 Project Structure
weather-telegram-bot/
│── bot.py
│── txt.txt
│── README.md
⚙️ Installation & Setup
1. Clone the repository
git clone https://github.com/your-username/weather-telegram-bot.git
cd weather-telegram-bot
2. Install dependencies
pip install python-telegram-bot requests
3. Get API Keys
Telegram Bot Token from BotFather
Weather API key from OpenWeatherMap
🔐 Important Security Note

⚠️ Your current code exposes:

Telegram bot token
API key

Fix this immediately by using environment variables:

import os

token = os.getenv("BOT_TOKEN")
apikey = os.getenv("WEATHER_API_KEY")

Then set them in your system:

export BOT_TOKEN="your_token_here"
export WEATHER_API_KEY="your_api_key_here"
▶️ Running the Bot
python bot.py

You should see:

starting...
polling...
💬 Bot Commands
Command	Description
/start	Start the bot
/help	Show help message

