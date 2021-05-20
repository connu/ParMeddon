import random
from discord.ext import commands
import scar
import os


client = commands.Bot(command_prefix="!")


@client.event
async def on_ready():

    print("bot is ready")


@client.command()
async def daily(ctx):
    io = scar.url_list
    pro = random.choice(io)
    await ctx.send(pro)

@client.command()
async def dailyaar(ctx):
    io_r = scar.url_rare
    pro_r = random.choice(io_r)
    await ctx.send(pro_r)

@client.command()
async def cursed(ctx):
    io_c = scar.url_c
    pro_c = random.choice(io_c)
    await ctx.send(pro_c)
  

client.run(os.environ.get('KEY'))


