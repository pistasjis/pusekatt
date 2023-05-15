import voltage
import os
from voltage.ext import commands

client = commands.CommandsClient("pus ")

@client.command()
async def ping(ctx):
    """Says hi"""
    await ctx.send("Hi!")

@client.command()
async def cat(ctx):
    """Posts a cat"""
    embed = voltage.SendableEmbed(
            title=ctx.author.name + "'s very own cat",  # The title of the embed
            colour="#7dd",  # The colour of the "strip" at the side of the embed
            icon_url=ctx.author.display_avatar.url,  # The icon beside the title of the embed. "message.author.display_avatar.url" gets the user's avatar.
            media="https://cataas.com/cat",  # The media for the embed. Here, we have an image.
        )
    # Reply to a message.
    await ctx.reply(content="Here is a cat for you!", embed=embed)

@client.command()
async def gif(ctx):
    """Posts a cat gif"""
    embed = voltage.SendableEmbed(
            title=ctx.author.name + "'s very own cat gif",  # The title of the embed
            colour="#7dd",  # The colour of the "strip" at the side of the embed
            icon_url=ctx.author.display_avatar.url,  # The icon beside the title of the embed. "message.author.display_avatar.url" gets the user's avatar.
            media="https://cataas.com/cat/gif",  # The media for the embed. Here, we have an image.
        )
    # Reply to a message.
    await ctx.reply(content="Here is a cat gif for you!", embed=embed)

@client.command(name="say", description="Posts a cat saying your message")
async def say(ctx, *, message):
    """Posts a cat saying your message"""
    embed = voltage.SendableEmbed(
            title=ctx.author.name + "'s very own cat",  # The title of the embed
            colour="#7dd",  # The colour of the "strip" at the side of the embed
            icon_url=ctx.author.display_avatar.url,  # The icon beside the title of the embed. "message.author.display_avatar.url" gets the user's avatar.
            media="https://cataas.com/cat/says/" + message,  # The media for the embed. Here, we have an image.
        )
    # Reply to a message.
    await ctx.reply(content="Here is a custom cat for you!", embed=embed)

try:
    token = os.environ["PUSEKATT_TOKEN"]
except KeyError:
    print("Missing PUSEKATT_TOKEN environment variable.")

client.run(token)