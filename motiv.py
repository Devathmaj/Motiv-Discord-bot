import discord
from discord.ext import commands
from dotenv import load_dotenv
import os
from openai import OpenAI

load_dotenv()
discord_token = os.getenv("DISCORD_TOKEN")
openrouter_key = os.getenv("OPENROUTER_API_KEY")

# Core AI client setup using OpenRouter
ai = OpenAI(base_url="https://openrouter.ai/api/v1", api_key=openrouter_key)

bot = commands.Bot(
    command_prefix="!",
    intents=discord.Intents.default().all()  # Required for message reading
)

@bot.event
async def on_ready():
    print(f"{bot.user} online")

@bot.event
async def on_message(message):
    if message.author == bot.user:
        return

    try:
        # Mood detection stage
        mood = ai.chat.completions.create(
            model="deepseek/deepseek-chat-v3-0324:free",
            messages=[{
                "role": "system",
                "content": "Reply 'SAD' if message sounds depressed, otherwise 'NOT_SAD'"
            },{
                "role": "user", 
                "content": message.content
            }],
            temperature=0.3,
            max_tokens=10
        ).choices[0].message.content.strip()

        if mood == "SAD":
            # Generate and send comfort response
            response = ai.chat.completions.create(
                model="deepseek/deepseek-chat-v3-0324:free",
                messages=[{
                    "role": "system",
                    "content": f"Reply to <@{message.author.id}> with 1 uplifting sentence (include emoji)"
                },{
                    "role": "user",
                    "content": message.content
                }],
                temperature=0.7
            )
            await message.channel.send(response.choices[0].message.content.strip())

    except Exception as e:
        print(f"Error: {e}")
        await message.channel.send(f"<@{message.author.id}> You've got this! 💪")

    await bot.process_commands(message)

bot.run(discord_token)