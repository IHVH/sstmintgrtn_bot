import discord
import asyncio
import os
import json
import logging
from discord.ext import commands
from pathlib import Path

cogs_path = Path.cwd() / 'sid' / 'cogs'
cfx_path = Path.cwd() / 'sid' / 'json' / 'cfx.json'
print(cfx_path)
cfx = json.load(open(cfx_path, encoding='utf-8'))

token = os.environ["DBOTTOKEN"]
intents = discord.Intents.all()
intents.message_content = True
activity = discord.Activity(name='голоса в своей голове', type=discord.ActivityType.listening)
Bot = commands.Bot(command_prefix=cfx['prefix'], activity=activity, intents=intents, owner_id=cfx['owner'])

logging.basicConfig(filename=f'{Path.cwd()}/sid/main.log', filemode='w', encoding='utf-8', level=logging.INFO)
logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')

@Bot.command(pass_context=True)
@commands.is_owner()
async def load(ctx, extension):
    await Bot.load_extension(f"cogs.{extension}")

@Bot.command(pass_context=True)
@commands.is_owner()
async def unload(ctx, extension):
    await Bot.unload_extension(f"cogs.{extension}")

@Bot.command(pass_context=True)
@commands.is_owner()
async def reload(ctx, extension):
    await Bot.unload_extension(f"cogs.{extension}")
    await Bot.load_extension(f"cogs.{extension}")

async def auto_load_extensions():
    for filename in os.listdir(cogs_path):
        if filename.endswith(".py"):
            await Bot.load_extension(f"cogs.{filename[:-3]}")

async def main():
    async with Bot:
        logging.info("Bot is up")
        print("Bot is up")
        await auto_load_extensions()
        await Bot.start(token)

asyncio.run(main())