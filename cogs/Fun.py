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


class Fun_Commands(commands.Cog):
    def __init__(self, client):
        self.client = client


    @commands.command(aliases=["aboutuser", "about_user", "userinfo", "user_info", "whoisme"])
    async def whois(self, ctx, member: discord.Member = None):
        if member == None:
            member = ctx.author
        elif member !=None:
            embed = discord.Embed(

                colour=member.colour,
                timestamp=ctx.message.created_at

            )

            roles = [role for role in member.roles]

            embed.set_author(name=f"User Info - {member}")
            embed.set_thumbnail(url=member.avatar_url)
            embed.set_footer(text=f"Requested By {ctx.author}", icon_url=ctx.author.avatar_url)

            embed.add_field(name="User Name", value=member.name, inline=False)
            embed.add_field(name="ID", value=member.id, inline=False)
            embed.add_field(name="Account Created", value=member.created_at.strftime("%a, %#d %B %Y, %I:%M %p UTC"), inline=False)
            embed.add_field(name="Member Joined", value=member.joined_at.strftime("%a, %#d %B %Y, %I:%M %p UTC"), inline=False)
            embed.add_field(name=f"Roles ({len(roles)})", value=" ".join([r.mention for r in member.roles if r != ctx.guild.default_role]), inline=False)
            embed.add_field(name="Top Role", value=member.top_role.mention, inline=False)
            embed.add_field(name="Bot?", value=member.bot, inline=False)

        await ctx.send(embed=embed)


    @commands.command(aliases=["avatar", "useravatar", "userpfp", "profilepicture", "profile_picture"])
    async def pfp(self, ctx, member: discord.Member = None):
        member = ctx.author if not member else member
        embed = discord.Embed(
            title=f"{member}'s Profile Picture",
            colour=member.colour
        )
        embed.set_image(url=member.avatar_url)
        await ctx.send(embed=embed)

    @commands.command(aliases=["confession", "makeconfession", "addconfession"])
    @commands.cooldown(1, 300, BucketType.member)
    async def confess(self, ctx, channel: discord.TextChannel, *, content: str):
        await ctx.message.delete()
        embed = discord.Embed(
            title="Someone made a confession!"
        )
        embed.add_field(name="Confession", value=content)
        await channel.send(embed=embed)


    @commands.command(aliases=["stix", "keys"])
    async def sticks(self, ctx, *, text):
        if ctx.guild.id != 491772737233092629: return
        await ctx.message.delete()
        await ctx.send(f"{text} get on the sticks")


    @commands.command(aliases=["rick", "roll" "getrick", "getricked", "rickastley", "astley"])
    async def rickroll(self, ctx, member: discord.Member):
        member = ctx.author if not member else member
        if member.id == 693661517824131172:
            await ctx.send("You cant rick roll the master rick roller you peasant!")
        else:
            await ctx.send(f"You just got rick rolled {member.mention}!",
                        file=discord.File(r"C:\Users\asher\OneDrive\Pictures\Camera Roll\Get Ricked.mp4"))


    @commands.command(aliases=["memes", "memer", "dankmeme", "dankmemer"])
    async def meme(self, ctx):
        await ctx.send(file=discord.File(
            r"C:\Users\asher\OneDrive\Pictures\Camera Roll\Meme.mp4"))


    @commands.command(aliases=["basketballgame", "trey", "basket", "mynameistrey"])
    async def basketball(self, ctx):
        await ctx.send(file=discord.File(r"C:\Users\asher\OneDrive\Pictures\Camera Roll\Basketball Game.mp44"))


    @commands.command(aliases=["Ice"])
    async def ice(self, ctx):
        await ctx.send(f"You have been iced by {ctx.author}", file=discord.File(r"C:\Users\asher\OneDrive\Pictures\Camera Roll\Ice Ice Baby.png"))


    @commands.command(aliases=["pop", "wrapper", "popper", "wrapperpop", "wrapperpopper", "bw", "bubble", "wrap"])
    async def bubblewrap(self, ctx):
        poppers = "||pop||" * 168
        await ctx.send(f"""{ctx.author} I see you like bubble wrap...
    > {poppers}""")


    @commands.command(aliases=["cf", "cointoss", "coin_toss", "coin", "coin_flip", "headsortails", "random_coin", "randomcoin"])
    async def coinflip(self, ctx):
        sides = ["**HEADS**", "**TAILS**"]
        randomcoin = random.choice(sides)
        await ctx.send(f"The coin landed on {randomcoin}!")


    @commands.command(aliases=["finddad", "wheredad", "milk", "dadlocator"])
    async def dad(self, ctx):
        await ctx.send("Have you tried looking in the gas station? He's probably in the dairy section.")


def setup(client):
    client.add_cog(Fun_Commands(client))