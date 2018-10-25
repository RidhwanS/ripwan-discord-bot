import discord
from discord.ext.commands import Bot
import asyncio
import time
import wikipedia
import random
import requests
import json

client = Bot(command_prefix='!')

eightBalls = {0: 'It is certain',
           1: 'Reply hazy try again',
           2: "Don't count on it",
           3: 'It is decidedly so',
           4: 'Ask again later',
           5: 'My reply is no',
           6: 'Without a doubt',
           7: 'Better not tell you now',
           8: 'My sources say no',
           9: 'Yes definitely',
           10: 'Cannot predict now',
           11: 'Outlook not so good',
           12: 'You may rely on it',
           13: 'Concentrate and ask again',
           14: 'Very doubtful'
}

eightBallsColours = {0: 0x00FF00,
           1: 0xFFFF00,
           2: 0xFF0000,
           3: 0x00FF00,
           4: 0xFFFF00,
           5: 0xFF0000,
           6: 0x00FF00,
           7: 0xFFFF00,
           8: 0xFF0000,
           9: 0x00FF00,
           10: 0xFFFF00,
           11: 0xFF0000,
           12: 0x00FF00,
           13: 0xFFFF00,
           14: 0xFF0000
}

@client.command(pass_context=True)
async def wiki(ctx,*args):
	search = wikipedia.search(' '.join(args))
	try:
		result = wikipedia.page(search[0])
	except wikipedia.exceptions.DisambiguationError as e:
		await client.say("The stuff you tried to search for had like a billion results. And wikipedia library doesnt like that or something. So RIP")
		return
	em = discord.Embed(title='Wikipedia: ' + result.title, description=(result.summary[:500] + '..') if len(result.summary) >= 500 else result.summary, color=0x2db5ef, url=result.url)
	await client.say(embed=em)

@client.command()
async def camp():
	file_object = open("Files/campInfo.txt", "r")
	em = discord.Embed(title='Campaign Info', description=file_object.read(), color=0x2db5ef)
	await client.say(embed=em)

@client.command(pass_context=True)
async def gitgud(ctx):
	number = random.randint(1, 6)
	imageURL = "Images/gitgud-"+str(number)+".png"
	#with open(imageURL, 'rb') as f:
	await client.send_file(ctx.message.channel,imageURL)

@client.command(name='8ball',pass_context=True)
async def eight_ball(ctx,*args):
	em = discord.Embed(title='8Ball: ' + ' '.join(args), description=random.choice(eightBalls), color=random.choice(eightBallsColours))
	await client.say(embed=em)

@client.command()
async def poll(*args):
	poll_parameters = list(args)
	question = poll_parameters.count('Q:')
	number_of_answers = poll_parameters.count('A:')
	if question == 0 or question > 1 or number_of_answers == 0:
		await client.say('The Format is, !poll Q: A Question A: Foo A: Bar. Only one Q: and at least one A:')
		return
	question_index = poll_parameters.index('Q:')
	if question_index != 0:
		await client.say('The Format is, !poll Q: A Question A: Foo A: Bar. The Q: has to be first')
		return
	first_answer_index = poll_parameters.index('A:')
	question_string = ' '.join(poll_parameters[1:first_answer_index])
	what_remains = poll_parameters[first_answer_index:]
	answers_list = [i for i in ' '.join(what_remains).split('A: ')]
	answers_list = answers_list[1:]
	data = {"title": question_string, "options": answers_list}
	poll = requests.post("https://www.strawpoll.me/api/v2/polls", json=data, headers={"Content-Type": "application/json"})
	await client.say("https://www.strawpoll.me/" + str(json.loads(poll.text)['id']))
	
client.run("<token>") #Insert your bots token here