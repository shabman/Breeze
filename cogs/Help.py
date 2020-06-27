import json
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


class Help_Command(commands.Cog):
    def __init__(self, client):
        self.client = client

    # Removes the help Command


    #self.client.remove_command("help")


    # Creates A New Help Command


    @commands.command(aliases=["command", "commands", "help!"])
    async def help(self, ctx):
        embed = discord.Embed(title=f'All Commands (Default prefix is "-")')

        embed.add_field(name="__**Fun**__", value="""
    whois (Mention User)
    pfp (Mention User)
    confess (channel) (confession)
    sticks (Mention User)
    rick (Mention User)
    meme
    trey
    bubblewrap
    coinflip
    dad
    ice
    """, inline=False)
        embed.add_field(name="__**Miscellaneous**__", value="""
    queue (Your Username)
    suggest (Suggestion)
    invite
    owner
    ping
    support
    updates
    donate
    """, inline=False)
        embed.add_field(name="__**Emojis**__", value="""
    thumbsup
    thumbsdown
    clown
    shrug
    oof
    wut
    eyes""", inline=False)
        embed.add_field(name="__**Administrator**__ ", value="""
    kick (Mention User) (Reason)
    ban (Mention User) (Reason)
    unban (Username And Four Numbers On The End)
    move (Mention User) (Voice Channel ID)
    dm (Mention User) (Message)
    say (Channel) (Message)
    prefix (New Prefix)
    role (Role) (User)
    purge (Amount)
    """, inline=False)
        embed.add_field(name="__**Need More Help? Join Our Help Server!**__", value="[Invite Link](https://discord.gg/YNw3bfj)")
    
        await ctx.send(embed=embed)


def setup(client):
    client.add_cog(Help_Command(client))