import discord
from discord.ext import commands

from rpsbLib import *

bot = commands.Bot(command_prefix='$')

@bot.event
async def on_ready():
    print('Logged in as')
    print(bot.user.name)
    print(bot.user.id)
    print('------')

@bot.command()
async def throw(ctx):
    await ctx.send(botThrowing(False))

@bot.command()
async def throwWithBomb(ctx):
    await ctx.send(botThrowing(True))

@bot.command()
async def ithrow(ctx, playerThrow):
    botThrow = botThrowing(False)
    result = playGame(playerThrow.lower(), botThrow)
    resp = "I throw " + botThrow + ". You " + result
    await ctx.send(resp)

@bot.command()
async def ithrowiVBomb(ctx, playerThrow):
    botThrow = botThrowing(True)
    result = playGame(playerThrow.lower(), botThrow)
    resp = "I throw " + botThrow + ". You " + result
    await ctx.send(resp)

bot.remove_command('help')

@bot.command()
async def help(ctx):
    embed = discord.Embed(title="nice bot", description="A Very Nice bot. List of commands are:", color=0xeee657)

    embed.add_field(name="$throw", value="Gives a random normal throw.", inline=False)
    embed.add_field(name="$throwWithBomb", value="Gives a random bomb-enabled throw.", inline=False)
    embed.add_field(name="$ithrow SIGN", value="Throws normally vs **SIGN** and gives result.", inline=False)
    embed.add_field(name="$ithrowVBomb", value="Throws bomb-enabled vs **SIGN** and gives result.", inline=False)
    embed.add_field(name="$help", value="Gives this message", inline=False)

    await ctx.send(embed=embed)

bot.run('key goes here')
