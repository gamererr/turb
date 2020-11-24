#!/usr/bin/env python3

import random
import asyncio
import discord
import requests
from discord import Member, Embed

with open("tokenfile", "r") as tokenfile:
	token=tokenfile.read()

intents = discord.Intents.all()
client = discord.Client(intents=intents)

async def attachments_to_files(attached,spoiler=False):
	filelist = []
	for i in attached:
		file = await i.to_file()
		filelist.insert(len(filelist),file)
	return filelist

@client.event
async def on_ready():
	print("hello world!")

randomness_sent = True
messages = 0

@client.event
async def on_message(message):
    
    global randomness_sent
    global messages

    temp = message.author.name.upper()
    randomphrase = ["shmoo balook", "your mom", "fartnite", '*holds out frog*\n"Quieres?"', "monke", "big chungus", temp]
    
    if randomness_sent:
        messages = random.randrange(5, 10)
        randomness_sent = False

    messages -= 1

    if messages == 0:
        await message.channel.send(randomphrase[random.randrange(len(randomphrase))])
        randomness_sent = True

client.run(token)