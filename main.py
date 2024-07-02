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

@client.command(pass_context=True)
async def join(ctx):
    if (ctx.author.voice):
        channel = ctx.author.voice.channel
        await channel.connect()
    else:
        await ctx.send('You are not in a voice channel!')

@client.command(pass_context=True)
async def leave(ctx):
   if (ctx.voice_client):
       await ctx.guild.voice_client.disconnect()
    else:
        await ctx.send('I am not in a voice channel!')

client.run(BOT_TOKEN)
