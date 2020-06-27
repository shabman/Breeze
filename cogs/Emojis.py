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


class Emoji_Commands(commands.Cog):
    def __init__(self, client):
        self.client = client


    @commands.command()
    async def clown(self, ctx):
        await ctx.message.delete()
        await ctx.send(":clown:")


    @commands.command()
    async def shrug(self, ctx):
        await ctx.message.delete()
        await ctx.send(":man_shrugging:")


    @commands.command()
    async def thumbsup(self, ctx):
        await ctx.message.delete()
        await ctx.send(":thumbsup:")


    @commands.command()
    async def thumbsdown(self, ctx):
        await ctx.message.delete()
        await ctx.send(":thumbsdown:")


    @commands.command()
    async def oof(self, ctx):
        await ctx.message.delete()
        await ctx.send("<:oof:607682498050260998>")


    @commands.command()
    async def wut(self, ctx):
        await ctx.message.delete()
        await ctx.send("<:waitWhat:622740549673418782>")


    @commands.command()
    async def eyes(self, ctx):
        await ctx.message.delete()
        await ctx.send("<:zoomeyes:390046883281633290>")


def setup(client):
    client.add_cog(Emoji_Commands(client))