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


class Admin_Commands(commands.Cog):
    def __init__(self, client):
        self.client = client


    @commands.command()
    @commands.has_permissions(ban_members=True)
    @commands.bot_has_permissions(ban_members=True)
    async def ban(self, ctx, member: discord.Member, *, reason=None):
        await member.ban(reason=f"Breeze Bot Ban - Responsible User : {ctx.author.name} | Reason : {reason}")
        await ctx.send(f'Banned {member.mention}')


    @commands.command(aliases=["removeban"])
    @commands.has_permissions(ban_members=True)
    @commands.bot_has_permissions(ban_members=True)
    async def unban(self, ctx, *, member):
        banned_users = await ctx.guild.bans()
        member_name, member_discriminator = member.split("#")
        for ban_entry in banned_users:
            user = ban_entry.user

        if (user.name, user.discriminator) == (member_name, member_discriminator):
            await ctx.guild.unban(user)
            await ctx.send(f'Unbanned {user.name}#{user.discriminator}')


    @commands.command()
    @commands.has_permissions(kick_members=True)
    @commands.bot_has_permissions(kick_members=True)
    async def kick(self, ctx, member: discord.Member, *, reason=None):
        await member.kick(f"Breeze Bot Kick - Responsible User : {ctx.author.name} | Reason : {reason}")
        await ctx.send(f'{member.mention} was kicked! ')


    @commands.command(aliases=["changeprefix", "prefixchange", "newprefix", "new_prefix"])
    @commands.has_permissions(administrator=True)
    @commands.bot_has_permissions(administrator=True)
    async def prefix(self, ctx, new_prefix):
        with open("prefixes.json", 'r') as f:
            prefixes = json.load(f)
        prefixes[str(ctx.guild.id)] = new_prefix

        with open("prefixes.json", "w") as f:
            json.dump(prefixes, f, indent=4)

        await ctx.send(f"Prefix changed to {new_prefix}")


    @commands.command(aliases=["send"])
    @commands.has_permissions(manage_messages=True)
    @commands.bot_has_permissions(manage_messages=True)
    async def say(self, ctx, channel: discord.TextChannel = None, *, content: str):
        channel = channel if channel else ctx.channel
        await ctx.message.delete()
        await channel.send(content)


    @commands.command(aliases=["clear"])
    @commands.has_permissions(manage_messages=True)
    @commands.bot_has_permissions(manage_messages=True)
    async def purge(self, ctx, *, amount=5):
        await ctx.message.delete()
        await ctx.channel.purge(limit=amount)


    @commands.command(aliases=["addrole", "removerole"])
    @commands.has_permissions(manage_roles=True)
    @commands.bot_has_permissions(manage_roles=True)
    async def role(self, ctx, role: discord.Role, user: discord.Member):
        if role in user.roles:
            await user.remove_roles(role)
        else:
            await user.add_roles(role)


    @commands.command(aliases=["moveto", "move_to", "movechannel", "move_channel"])
    @commands.has_permissions(administrator=True)
    @commands.bot_has_permissions(administrator=True)
    async def move(self, ctx, member: discord.Member, channel: discord.VoiceChannel):
        await ctx.message.delete()
        await member.move_to(channel, reason=None)


    @commands.command(aliases=["pm"])
    @commands.has_permissions(administrator=True)
    @commands.bot_has_permissions(administrator=True)
    async def dm(self, ctx, member: discord.Member, *, text):
        await ctx.message.delete()
        await member.send(f"Message from {ctx.author}: {text}")


def setup(client):
    client.add_cog(Admin_Commands(client))
