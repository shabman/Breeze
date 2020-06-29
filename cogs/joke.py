import asyncio

@commands.command()
async def joke(ctx):

    await ctx.send("{}, check your DMs!".format(ctx.author.mention))

    def check(message):
        return message.author == ctx.author and isinstance(message.channel, discord.DMChannel) and ctx.author.bot == False

    await ctx.author.send("Wanna hear a funny joke? [yes / no]")

    try:

        msg1 = await self.client.wait_for('message', check=check, timeout=10)

        if msg1.content.lower() == 'yes':

            await ctx.author.send("Sike! There is no joke :wink:")
            asyncio.sleep(3)
            await msg1.delete()

        elif msg1.content.lower() == 'no':

            await ctx.author.send(":sob:")
            asyncio.sleep(3)
            await msg1.delete()

        else:

            await ctx.author.send("Invalid input")
            asyncio.sleep(3)
            await msg1.delete()

    except asyncio.TimeoutError:

        await ctx.author.send("Time is up buddy!")
        asyncio.sleep(3)
        await msg1.delete()
