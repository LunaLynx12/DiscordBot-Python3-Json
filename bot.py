import discord
from discord.ext import commands
import random
import asyncio
import os

bot =commands.Bot(command_prefix="$")

@bot.event
async def on_ready():
    print('Logged in as {0} ({0.id})'.format(bot.user))
    print('------')

@bot.command()
async def nick(ctx, member: discord.Member, *, name: str):
    await member.edit(nick=name)

for cog in os.listdir("./cogs"):
    if cog.endswith(".py"):
        try:
            cog = f"cogs.{cog.replace('.py', '')}"
            bot.load_extension(cog)
        except Exception as e:
            print(f"{cog} can not be loaded:")
            raise e

bot.run('my_token')
