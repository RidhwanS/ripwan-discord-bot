import discord
from discord.ext.commands import Bot
from discord.ext import commands
import asyncio
import time
import wikipedia
import random

Client = discord.Client()
client = commands.Bot(command_prefix="!")

eightBalls = {0: 'It is certain',
           1: 'As I see it, yes',
           2: 'Reply hazy try again',
           3: "Don't count on it",
           4: 'It is decidedly so',
           5: 'Most likely',
           6: 'Ask again later',
           7: 'My reply is no',
           8: 'Without a doubt',
           9: 'Outlook good',
           10: 'Better not tell you now',
           11: 'My sources say no',
           12: 'Yes definitely',
           13: 'Yes',
           14: 'Cannot predict now',
           15: 'Outlook not so good',
           16: 'You may rely on it',
           17: 'Signs point to yes',
           18: 'Concentrate and ask again',
           19: 'Very doubtful'
}

eightBallsColours = {0: 0x00FF00,
           1: 0x00FF00,
           2: 0xFFFF00,
           3: 0xFF0000,
           4: 0x00FF00,
           5: 0x00FF00,
           6: 0xFFFF00,
           7: 0xFF0000,
           8: 0x00FF00,
           9: 0x00FF00,
           10: 0xFFFF00,
           11: 0xFF0000,
           12: 0x00FF00,
           13: 0x00FF00,
           14: 0xFFFF00,
           15: 0xFF0000,
           16: 0x00FF00,
           17: 0x00FF00,
           18: 0xFFFF00,
           19: 0xFF0000
}

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
            try:
                result = wikipedia.page(search[0])
            except wikipedia.exceptions.DisambiguationError as e:
                await client.send_message(message.channel, "The stuff you tried to search for had like a billion results. And wikipedia library doesnt like that or something. So RIP")
            em = discord.Embed(title='Wikipedia: ' + result.title, description=(result.summary[:500] + '..') if len(result.summary) >= 500 else result.summary, color=0x2db5ef, url=result.url)
            await client.send_message(message.channel, embed=em)
    if message.content.lower().startswith('!camp'):
        file_object = open("Files/campInfo.txt", "r")
        em = discord.Embed(title='Campaign Info', description=file_object.read(), color=0x2db5ef)
        await client.send_message(message.channel, embed=em)
    if message.content.lower().startswith('!gitgud'):
        number = random.randint(1, 6)
        imageURL = "Images/gitgud-"+str(number)+".png"
        with open(imageURL, 'rb') as f:
            await client.send_file(message.channel, f, content="GIT GUD")
    if message.content.lower().startswith('!8ball'):
        args = message.content[6:]
        number = random.randint(0, 19)
        em = discord.Embed(title='8Ball:' + args, description=eightBalls[number], color=eightBallsColours[number])        await client.send_message(message.channel, embed=em)
    if message.content.lower().startswith('!help'):
        file_object = open("README.md", "r")
        em = discord.Embed(title='Help', description=file_object.read(), color=0x2db5ef)
        await client.send_message(message.channel, embed=em)

client.run("<token>") #Insert your bots token here