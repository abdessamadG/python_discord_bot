import discord
import os
from dotenv import load_dotenv
from discord.ext import commands

load_dotenv()

intents = discord.Intents.default()
intents.message_content = True

client = commands.Bot(command_prefix="!", intents=intents)

@client.event
async def on_ready():
    print(f'You are logged in as {client.user}')

@client.command()
async def hello(ctx):
    await ctx.send(f"Hello {ctx.author.mention}! 👋")

client.run(os.getenv('Token'))