import discord
import asyncio
#import aiohttp
from discord import *
from discord import Game
from discord.message import *
from discord.ext.commands import Bot
from discord.ext import commands

BOT_PREFIX = ("gae.")

TOKEN = ""

client = Bot(command_prefix = BOT_PREFIX)

@client.command(pass_context = True)
@commands.has_permissions(manage_messages = True)
async def embed(ctx, chan: discord.TextChannel, titl, link, image, desc = None):
    embed = discord.Embed(color = 0x36393E)
    embed.set_image(url = image)
    embed.add_field(name = "Guild Name", value = titl, inline = True)
    embed.add_field(name = "Link", value = link, inline = True)
    if desc != None:
        embed.add_field(name = "Description", value = desc, inline = False)
    await client.get_channel(chan.id).send(embed = embed)

@client.command(pass_context = True)
async def search(query):
    return

client.run(TOKEN)
