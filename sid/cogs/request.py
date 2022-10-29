import discord
import requests
import json
import logging
from pathlib import Path
from discord import Message, message
from discord.ext import commands
from discord.ui import Button, View

cfx_path = Path.cwd() / 'sid' / 'json' / 'cfx.json'
cfx = json.load(open(cfx_path, encoding='utf-8'))

class Request_Cog(commands.Cog):
    def __init__(self, Bot):
        self.Bot = Bot
    
    @commands.Cog.listener()
    async def on_ready(self):
        print(f'{self.__cog_name__} is up')
        logging.info(f'{self.__cog_name__} is up')

    @commands.command()
    async def req_test(self, ctx):
        req = requests.get('https://randomfox.ca/floof/')
        req = req.json()
        await ctx.send(req['image'])

async def setup(Bot):
    await Bot.add_cog(Request_Cog(Bot))