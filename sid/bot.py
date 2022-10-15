import discord
import os
import json
from discord.ext import commands
from pathlib import Path

cwd = Path(__file__).parents[0]
cwd = str(cwd)
cfx = json.load(open(cwd+'\json\cfx.json', encoding='utf-8'))

token = os.environ["DBOTTOKEN"]
intents = discord.Intents.all()
intents.message_content = True
activity = discord.Activity(name='голоса в своей голове', type=discord.ActivityType.listening)
Bot = commands.Bot(command_prefix=cfx['prefix'], activity=activity, intents=intents, owner_id=cfx['owner'])

@Bot.command(pass_context=True)
#@commands.is_owner()
async def load(ctx, extension):
    Bot.load_extension(f"cogs.{extension}")

@Bot.command(pass_context=True)
#@commands.is_owner()
async def unload(ctx, extension):
    Bot.unload_extension(f"cogs.{extension}")

@Bot.command(pass_context=True)
#@commands.is_owner()
async def reload(ctx, extension):
    Bot.unload_extension(f"cogs.{extension}")
    Bot.load_extension(f"cogs.{extension}")

#TODO - этим образом оно не работает, пока подгрузка cog'ов разве что руками
'''
for filename in os.listdir(cwd+"\cogs"):
    if filename.endwith(".py"):
        Bot.load_extension(f"cogs.{filename[:-3]}")
'''

Bot.run(token)