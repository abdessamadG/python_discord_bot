import discord
import os
from dotenv import load_dotenv
from discord.ext import commands
from openai import OpenAI

load_dotenv()

OPENAI_API_KEY = os.getenv('OPENAI_API_KEY')

openai_client = OpenAI(api_key=OPENAI_API_KEY)

intents = discord.Intents.default()
intents.message_content = True

client = commands.Bot(command_prefix="!", intents=intents)

@client.event
async def on_ready():
    print(f'You are logged in as {client.user}')

@client.command()
async def hello(ctx):
    await ctx.send(f"{ctx.author.mention}, hope you're having a wonderful day! 🌟")
    
@client.command()
async def ask(ctx, *, question):
    await ctx.send(f"Generating answer for {ctx.author.mention}...")

    try:
        # Call OpenAI API using new 1.x Python client syntax
        response = openai_client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[
                # System prompt
                {"role": "system", "content": "You are a helpful assistant."},
                # User prompt
                {"role": "user", "content": question}
            ],
            max_tokens=1000
        )
        # extracts the generated answer text that the bot will send back to Discord
        answer = response.choices[0].message.content
        # Send the AI's answer back to the Discord channel
        await ctx.send(f"{answer}")

    except Exception as e:
        # Print detailed error in bot console
        print("OpenAI API Error:", e)
        # Inform the user something went wrong
        await ctx.send("Failed to get a response from OpenAI. \nCheck terminal for more info about what caused that error")

client.run(os.getenv('TOKEN'))