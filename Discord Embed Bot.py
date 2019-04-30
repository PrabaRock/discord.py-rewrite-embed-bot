import discord
import asyncio
from discord import *
from discord.message import *
from discord.ext.commands import Bot
from discord.ext.commands import ConversionError #remembered what I was going to use it for: find the error raised if not enough inputs are inputted for embed command, prevent txt file (substitute for db file) from being written in so it doesn't store faulty data and break everything
from discord.ext import commands

BOT_PREFIX = ("e.")
TOKEN = ""
client = Bot(command_prefix = BOT_PREFIX)

path = ''

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
    
    if embedDesc != None:
        embed.add_field(name = "Description", value = embedDesc, inline = False)

    if len(open(path, 'r').read()) == 0:
        print(open(path, 'r').read())
        print("1")
        embedFile = open(path, 'r+')
        embedFile.write(str(sendToChannel.id))
        embedFile.write(embedTitle)
        embedFile.write(embedLink)
        embedFile.write(embedImage)
    else:
        print("2")
        embedFile = open(path, 'a')
        embedFile.write("\n")
        embedFile.write(str(sendToChannel.id))
        embedFile.write(embedTitle)
        embedFile.write(embedLink)
        embedFile.write(embedImage)

    if embedDesc != None:
        embedFile.write(embedDesc)
    embedFile.close()
    
    await client.get_channel(sendToChannel.id).send(embed = embed)

@client.command(hidden = True,
                pass_context = True) #pass needed so I can use ctx
async def cleardb(ctx):
    if ctx.message.author.id == "156179325421486081" or "150417106549211136": #dream or me
        embedFile = open(path, 'w')
        embedFile.write("")
        channel = ctx.channel
        await channel.send("Done.")

@client.command(hidden = True,
                pass_context = True)
async def dblen(ctx):
    channel = ctx.channel
    await channel.send(len(open(path, 'r').read()))

client.run(TOKEN)
