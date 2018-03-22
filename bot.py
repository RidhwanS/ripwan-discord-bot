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
            em = discord.Embed(title='Wikipedia: ' + result.title, description=(result.summary[:500] + '..') if len(result.summary) >= 500 else result.summary, color=0x2db5ef, url=result.url)
            await client.send_message(message.channel, embed=em)
    if message.content.lower().startswith('!camp'):
        file_object = open("campInfo.txt", "r")
        em = discord.Embed(title='Campaign Info', description=file_object.read(), color=0x2db5ef)
        await client.send_message(message.channel, embed=em)


client.run("<TOKEN>") #Insert your bots token here