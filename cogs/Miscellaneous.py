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


class Misc_Commands(commands.Cog):
    def __init__(self, client):
        self.client = client


    @commands.command(aliases=["feedback", "suggestion"])
    async def suggest(self, ctx, *, content): 
        await ctx.message.delete()
        async with aiohttp.ClientSession() as session:
            webhook = Webhook.from_url('The Webhook URL', adapter=AsyncWebhookAdapter(session))
            await webhook.send(f"Suggestion - {content}", username="Suggestion")


    @commands.command(aliases=["reportbug", "sendbug", "bugreport"])
    async def bug(self, ctx, *, content): 
        await ctx.message.delete()
        async with aiohttp.ClientSession() as session:
            webhook = Webhook.from_url('The Webhook URL', adapter=AsyncWebhookAdapter(session))
            await webhook.send(f"Bug - {content}", username="Bug Found!")



    @commands.command(aliases=["enterqueue", "queueenter"])
    async def queue(self, ctx, *, text):
        embed = discord.Embed(
            title="User Entered The Queue",
            colour=discord.Colour.blue(),

        )

        embed.set_author(name=f"{ctx.author}")
        embed.add_field(name="Server", value=f"{ctx.guild}", inline=False)
        embed.add_field(name="User", value=f"{ctx.author}", inline=False)
        embed.add_field(name="Queue", value=f"{ctx.author} entered the queue!", inline=False)
        embed.add_field(name="Queue Username", value=f"{text}", inline=False)

        await ctx.send(embed=embed)


    @commands.command(aliases=["invitebot"])
    async def invite(self, ctx):
        embed = discord.Embed(

            title="Invite Breeze"
        )
        embed.add_field(name="Invite me to your server!",
                        value="[Invite Link](https://discord.com/oauth2/authorize?client_id=709775179303223387&permissions=8&scope=bot)")
        await ctx.send(embed=embed)


    @commands.command()
    async def ping(self, ctx):
        await ctx.send(f'Pong! {round(self.client.latency * 1000)}ms')
        print(f"Someone requested the ping! The ping was {round(self.client.latency * 1000)}ms! ")


    @commands.command(aliases=["supportserver", "support_server", "help_server", "helpserver"])
    async def support(self, ctx):
        embed = discord.Embed(

            title="Join our support server!"
        )
        embed.add_field(name="Support Server", value="[Invite Link](https://discord.gg/YNw3bfj)")
        await ctx.send(embed=embed)


    @commands.command(aliases=["dono", "donation", "paypal", "venmo", "cashapp"])
    async def donate(self, ctx):
        embed = discord.Embed(

        )
        embed.add_field(name="Donate", value="[Donation Link](https:Ko-fi.com/breezebotdevs)")
        await ctx.send(embed=embed)


def setup(client):
    client.add_cog(Misc_Commands(client))
