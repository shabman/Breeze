import json
import os
from itertools import cycle
import discord
from discord.ext import commands, tasks
import random
from discord.ext.commands.cooldowns import BucketType
from discord.utils import get
from discord.ext import commands
import time
import aiohttp
from discord import Webhook, AsyncWebhookAdapter
import sys, traceback
import asyncio

# Token


token = "NzA5Nzc1MTc5MzAzMjIzMzg3.XvWgIQ.6dNRafY_3XzEJjia6IwAZACMKrg"
# removes help command



# Get Prefix


async def get_prefix(bot, message):
    with open('prefixes.json', 'r') as f:
        prefixes = json.load(f)

        prefix = prefixes[str(message.guild.id)]
    return commands.when_mentioned_or(prefix)(client, message)


# Define Bot


client = commands.Bot(command_prefix=get_prefix)


# Status Cycle


status = cycle(
    ["Breeze Development", "-invite", "Join Support Server for Help!", "discord.py", "-suggest (Suggestion)"])

# On Ready


client = commands.Bot(command_prefix=get_prefix, owner_id=[693661517824131172, 171539705043615744, 655795127079534605, 514858928983506959])
client.ready = False
client.remove_command('help')


@client.event
async def on_ready():
    if not client.ready:
        with open("prefixes.json", "r") as f:
            client.prefixes = json.load(f)
        print("Breeze is now online! ")
        await client.change_presence(activity=discord.Game("-help"))
        change_stats.start()
        print("Status Loop Has Started!")
        print(f"Breeze is in {len(client.guilds)} servers!")
        client.ready = True


# Guild Join/Guild Leave


@client.event
async def on_guild_join(guild):
    print(f"""Someone invited Breeze to their server!
Server Name - {guild.name}
Breeze is now in {len(client.guilds)} servers!""")
    with open('prefixes.json', 'r') as f:
        prefixes = json.load(f)

        prefixes[str(guild.id)] = "-"

        with open("prefixes.json", "w") as f:
            json.dump(prefixes, f, indent=4)


@client.event
async def on_guild_remove(guild):
    print(f"""Someone removed Breeze from their server
Server Name - {guild.name}
Breeze is now in {len(client.guilds)} servers :(""")

    with open('prefixes.json', 'r') as f:
        prefixes = json.load(f)

        prefixes.pop(guild.id)

        with open("prefixes.json", "w") as f:
            json.dump(prefixes, f, indent=4)


extentions = ["jishaku", "cogs.Admin", "cogs.Emojis", "cogs.Errors", "cogs.Fun", "cogs.Help", "cogs.Miscellaneous"]


if __name__ == "__main__":
    loop = asyncio.get_event_loop()
    for ext in extentions:
        try:
            client.load_extension(ext)
        except Exception as exct:
            print(f"{exct} could not load {ext}")


# Game Loop


@tasks.loop(seconds=25)
async def change_stats():
    await client.change_presence(activity=discord.Game(next(status)))


client.run(token)