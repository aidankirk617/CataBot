import os
import random
import discord
import asyncio
import datetime
import sys
import time
import info

from dotenv import load_dotenv
from discord.ext import commands
from discord.utils import get


load_dotenv()
TOKEN = info.TOK
GUILD = os.getenv('DISCORD_GUILD')

bot = commands.Bot(command_prefix='&')
client = discord.Client()

dictionary = wl.build_dictionary()


# Log on message for the bot
@bot.event
async def on_ready():
    for guild in bot.guilds:
        if guild.name == GUILD:
            break

    print(
        f'{bot.user} is connected to the following guild:\n'
        f'{guild.name}(id: {guild.id})'
    )

    members = '\n - '.join([member.name for member in guild.members])


# Writes errors to file
@bot.event
async def on_error(event, *args, **kwargs):
    with open('err.log', 'a') as f:
        if event == 'on_message':
            f.write(f'Unhandled message: {args[0]}\n')
        else:
            raise


# info command
@bot.command(name='info')
async def info(ctx):
    info_message = 'Hi kid. My name\'s Bill. Bill Cipher. I help out around here\nMy prefix is `&` and I can do things like spam quotes and make fun of you.\nMaybe one day I\'ll be useful. But not today!'
    await ctx.send(info_message)


# Quote command
@bot.command(name='quote', help='Responds with a random Gravity Falls quote')
async def quote(ctx):

    gravity_falls_quotes = [
        'Reality is an illusion, the universe is a hologram, buy gold, bye!',
        'Hey kid, wanna make a *deal?*',
        'Time is dead and meaning has no meaning.',
        'Existence is upside down and i reign supreme.',
        'It\'s funny how dumb you are',
        'Here, have a head that\'s always screaming',
        'Did you miss me? Admit it, you missed me',
        'I\'m watching you nerds'
    ]

    response = random.choice(gravity_falls_quotes)
    await ctx.send(response)


# Rolls dice
@bot.command()
async def roll(ctx, num_dice: int, num_sides: int):
    dice = [
        str(random.choice(range(1, num_sides + 1)))
        for _ in range(num_dice)
    ]
    total = 0
    for die in dice:
        sum += int(die)
    await ctx.send(str(dice) + " with a total of " + str(total))


# ping command
@bot.command()
async def ping(ctx):
    '''
    Issues a ping and returns the latency
    '''

    latency = bot.latency
    await ctx.send("Pong! " + str(latency))


# Respond to messages
@bot.event
async def on_message(message):
    if (message.author.bot):
        returctxn
    await bot.process_commands(message)
    msg = message.content.lower().replace(" ", "")
    username = message.author.name.lower().replace(" ", "")
    if '!stop!' in msg:
        await bot.logout()
    if 'brown' in msg:
        await message.channel.send('Brown is closed on weekends')
    if 'bill' in msg or 'cipher' in msg:
        emoji = '<:bill_cipher_pointing:621113711473590274>'
        await message.add_reaction(emoji)
    if 'dannys theme' in msg or "danny's theme" in msg:
        await message.channel.send('https://soundcloud.com/mynameisdonut/dannys-theme-but-im-leaving-it-unmixed-and-unfinished-because-danny-is-trash')
    if 'summon' in msg:
        emoji = '<:bill_cipher_pointing:621113711473590274>'
        await message.channel.send(emoji)
    if 'conceptually' in msg:
        emoji = '<:conceptually:688540260417667078>'
        await message.channel.send(emoji)

# join the voice channel


@bot.command()
async def join(ctx, *, channel: discord.VoiceChannel):
    if ctx.voice_client is not None:
        return await ctx.voice_client.move_to(channel)
    await channel.connect()

# leave the voice channel


@bot.command()
async def leave(ctx):
    server = ctx.message.server
    voice_client = bot.voice_client_in(server)
    await voice_client.disconnect()


# Send random word
@bot.command()
async def rand(ctx):
    word = random.choice(dictionary)
    await ctx.send(word + "!")


bot.loop.create_task(time_check())

bot.run(TOKEN)
