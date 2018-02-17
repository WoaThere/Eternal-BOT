# Eternal BOT by Woa There

# Import
import random
import discord
from discord.ext import commands
from discord.ext.commands import Bot
import asyncio

#
bot = commands.Bot(command_prefix='/')

@bot.event
async def on_ready():
  print(bot.user.name + " BOT Online with ID " + bot.user.id)

# Roll command
@bot.command(pass_context=True)
async def roll(ctx):
  roll = random.randint(1, 20)
  if roll == 1 :
    await bot.say("You rolled " + str(roll) + ". Critical failure!")
  elif roll == 20:
    await bot.say("You rolled " + str(roll) + ". Critical success!")
  else :
    await bot.say("You rolled " + str(roll) + ".")

# Ping Command
@bot.command(pass_context=True)
async def ping(ctx):
  await bot.say(":ping_pong: Pong!")

# Bot Info Command
@bot.command(pass_context=True)
async def botinfo(ctx):
  embed = discord.Embed(title="{} BOT Infomation".format(bot.user.name), description="I am a bot.", color=0x5e0fdd)
  await bot.say(embed=embed)

# Quote Command
@bot.command(pass_context=True)
async def quote(ctx, quote = None, speaker = None, year = None):
  
  if quote == None or speaker == None or year == None :
    
    embed = discord.Embed(title="Error!".format(bot.user.name), description="Missuse of the command. To use the command, type '/quote\"Quote\" Author Year'", color=0x5e0fdd)
    msg = await bot.say(embed=embed)
    await asyncio.sleep(3)
    await bot.delete_message(ctx.message)
    await bot.delete_message(msg)
    
  else :
    
    embed = discord.Embed(title="\"{}\"".format(quote), description="—{0}, {1}".format(speaker, year), color=0x5e0fdd)
    msg = await bot.say(embed=embed)
    await bot.delete_message(ctx.message) 
    await bot.add_reaction(msg, '\N{THUMBS UP SIGN}')
    await bot.add_reaction(msg, '\N{THUMBS DOWN SIGN}')
    cache_msg = discord.utils.get(bot.messages, id=msg.id)
    
    resolved = False
    timer = 60
    while not resolved and timer >= 0 :

      await asyncio.sleep(1)
      timer -= 1
      if len(cache_msg.reactions) >= 5 :
        resolved = True
    await bot.say("{0} {1}".format(cache_msg.reactions.count('\N{THUMBS UP SIGN}'), cache_msg.reactions.count('\N{THUMBS DOWN SIGN}')))
    if cache_msg.reactions.count('\N{THUMBS UP SIGN}') > cache_msg.reactions.count('\N{THUMBS DOWN SIGN}') :
      # Remove Reactions
      await asyncio.sleep(1)
    else :
      await bot.delete_message(msg)
bot.run("MzI3NzE3Mzk4NjEyMjc5Mjk5.DVRL3g.g7m6n0_Y80YEwmOXctkyVYBZbb0")
