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


class Command_Events(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.Cog.listener()
    async def on_command_not_found(self, ctx, error):
        embed = discord.Embed(
            title=f"No command found! Type -help for a list of all the availble commands commands!",
            description=None,
            colour=discord.Colour.red()
        )

        if isinstance(error, commands.BadArgument):
            await ctx.send(embed=embed)


    @commands.Cog.listener()
    async def on_missing_arg(self, ctx, error):
        embed = discord.Embed(
            title=f"I didnt understand the way you said that! Make sure you are useing the correct arguments! You can see the correct arguments by doing -help!",
            description=None,
            colour=discord.Colour.red()
        )

        if isinstance(error, commands.MissingRequiredArgument):
            await ctx.send(embed=embed)


    @commands.Cog.listener()
    async def cooldown(self, ctx, error):
        cooldown_left = round(error.retry_after / 60)
        await ctx.message.delete()
        if isinstance(error, commands.errors.CommandOnCooldown):
            await ctx.send(f"You are on cooldown! You can use this command in {cooldown_left} minutes!")



def setup(client):
    client.add_cog(Command_Events(client))