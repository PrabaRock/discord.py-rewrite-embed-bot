import discord
import asyncio
from discord import *
from discord import Game
from discord.message import *
from discord.ext.commands import Bot
from discord.ext import commands

BOT_PREFIX = ("e.")

TOKEN = ""

client = Bot(command_prefix = BOT_PREFIX)

@client.command(name = "embed",
                brief = "Does embedding.",
                aliases = ["e"],
                description = "Embeds guilds for Dream's sake. Note 'embedDesc' is optional. Requires permission 'manage_messages' to be used.",
                pass_context = True)
@commands.has_permissions(manage_messages = True)
async def embed(ctx, sendToChannel: discord.TextChannel, embedTitle, embedLink, embedImage, embedDesc = None):
    embed = discord.Embed(color = 0x36393E)
    embed.set_image(url = embedImage)
    embed.add_field(name = "Guild Name", value = embedTitle, inline = True)
    embed.add_field(name = "Link", value = embedLink, inline = True)
    if desc != None:
        embed.add_field(name = "Description", value = embedDesc, inline = False)
    await client.get_channel(sendToChannel.id).send(embed = embed)

client.run(TOKEN)
