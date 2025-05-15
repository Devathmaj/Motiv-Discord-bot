# Motiv-Discord-bot
Created in late 2023 | Updated May 2024

A supportive Discord bot that detects sad or down messages and responds with uplifting, AI-generated encouragement.

---

## Features ✨

- 🧠 **AI-Powered Mood Detection**  
  Uses DeepSeek (or OpenAI) to intelligently detect sadness in messages.

- 💬 **Personalized Comfort**  
  Generates unique, motivational responses based on the user's message.

- @ **User Mentions**  
  Always pings the user directly to offer personalized support.

- 🤖 **No Commands Needed**  
  The bot listens and responds automatically in all channels.

---

## Setup ⚙️

### Requirements

- Python 3.9 or higher
- Discord bot token (from Discord Developer Portal)
- OpenRouter API key (free tier available) or OpenAI API key

### Installation

```bash
pip install discord.py python-dotenv openai
```
Configuration
Create a .env file in your project directory with the following content:

ini
Copy
Edit
DISCORD_TOKEN=your_discord_bot_token_here
OPENROUTER_API_KEY=your_openrouter_api_key_here
# or if using OpenAI:
OPENAI_API_KEY=your_openai_api_key_here
Running the Bot
bash
Copy
Edit
python bot.py
How It Works 🔍
The bot listens to all messages sent in the Discord server.

Each message is sent to an AI service (DeepSeek or OpenAI) to detect the user's mood based on message context.

If the AI detects sadness, depression, or feeling down:

The bot generates a custom comforting message.

It mentions the user directly with the motivational response.

If the user’s message does not indicate sadness, the bot remains silent.

Example 💬
User: "I'm having a really tough day..."

Bot: "<@123456789> Remember, even the darkest nights end with sunrise ☀️. You're not alone!"

Troubleshooting 🛠️
Issue	Solution
400 Bad Request	Double-check your OpenRouter/OpenAI API key is valid and has correct permissions.
Missing Privileged Intents	Enable "Message Content Intent" and other privileged intents in the Discord Developer Portal.
Empty or No Bot Response	Verify your AI API key and quota; check internet connection and API service status.
Bot Not Responding	Confirm your bot has permission to read messages and send messages in your Discord server.
API Rate Limit (Error 429)	You may be exceeding your monthly quota; consider upgrading your API plan or reducing requests.

Notes 📌
This bot is intended for supportive purposes only and is not a substitute for professional mental health care.

Always monitor and moderate your server environment when using AI-powered bots.

Feel free to contribute or open issues if you find bugs or want to suggest improvements!
