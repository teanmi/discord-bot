import discord
from discord.ext import commands
import os
from dotenv import load_dotenv

# load env varibales
load_dotenv()
BOT_TOKEN = os.getenv('BOT_TOKEN')

# set intents
intents = discord.Intents.default()
intents.message_content = True
client = commands.Bot(command_prefix = '!!', intents=intents)

# startup
@client.event
async def on_ready():
    print('Bot is ready.')
    print('--------------------------------')

# commands
@client.command()
async def hello(ctx):
    await ctx.send('Hello!')

client.run(BOT_TOKEN)
