import discord
from discord.ext import commands
from discord import FFmpegPCMAudio
import os
from dotenv import load_dotenv

# load env varibales
load_dotenv()
BOT_TOKEN = os.getenv('BOT_TOKEN')
AUDIO_FILE = os.getenv('AUDIO_FILE')
CHANNEL_NAME = os.getenv('CHANNEL_NAME')

# set intents
intents = discord.Intents.default()
intents.message_content = True
intents.voice_states = True

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
        voice = await channel.connect()
        source = FFmpegPCMAudio(AUDIO_FILE)
        player = voice.play(source)
    else:
        await ctx.send('You are not in a voice channel!')

@client.command(pass_context=True)
async def leave(ctx):
    if (ctx.voice_client):
        await ctx.guild.voice_client.disconnect()
    else:
        await ctx.send('I am not in a voice channel!')

@client.event
async def on_voice_state_update(member, before, after):
    bot_channel = discord.utils.get(member.guild.voice_channels, name=CHANNEL_NAME)

    # Handle user joining the general voice channel
    if after.channel is not None and after.channel == bot_channel:
        if client.user not in after.channel.members:
            voice = await after.channel.connect()
            source = FFmpegPCMAudio(AUDIO_FILE)
            voice.play(source)
    
    # Handle user leaving the general voice channel
    if before.channel is not None and before.channel == bot_channel:
        if len(before.channel.members) == 1 and before.channel.members[0] == client.user:
            await before.channel.guild.voice_client.disconnect()

client.run(BOT_TOKEN)
