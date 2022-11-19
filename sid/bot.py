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
intents.members = True
activity = discord.Activity(name='голоса в своей голове', type=discord.ActivityType.listening)
Bot = commands.Bot(command_prefix=cfx['prefix'], activity=activity, intents=intents, owner_id=cfx['owner'])

logging.basicConfig(filename=f'{Path.cwd()}/sid/main.log', filemode='w', encoding='utf-8', level=logging.INFO)
logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')

async def auto_load_extensions():
    for filename in os.listdir(cogs_path):
        if filename.endswith(".py"):
            await Bot.load_extension(f"cogs.{filename[:-3]}")

async def main():
    async with Bot:
        await auto_load_extensions()
        await Bot.start(token)

        logging.info(f'Logged in as: {Bot.user.name} - {Bot.user.id}, Version: {discord.__version__}\n')
        print(f'\n\nLogged in as: {Bot.user.name} - {Bot.user.id}\nVersion: {discord.__version__}\n')

asyncio.run(main())