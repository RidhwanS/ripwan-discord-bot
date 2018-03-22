import discord
from discord.ext.commands import Bot
from discord.ext import commands
import asyncio
import time
import wikipedia

Client = discord.Client()
client = commands.Bot(command_prefix = "!")

@client.event
async def on_ready():
    print("Bot is online and connected to Discord")

@client.event
async def on_message(message):
    if message.content.lower().startswith('!wiki'):
        args = message.content.replace('!wiki', '', 1)
        if len(args) == 0:
            await client.send_message(message.channel, "No Message Was Next To Command")
        else:
            search = wikipedia.search(args)
            result = wikipedia.page(search[0])
            em = discord.Embed(title='Wikipedia: ' + result.title, description=result.summary[:500] + '..', color=0x2db5ef, url=result.url)
            await client.send_message(message.channel, embed=em)

client.run("<TOKEN>") #Insert your bots token here