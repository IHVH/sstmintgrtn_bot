import discord
import json
from pathlib import Path
from discord import Message, message
from discord.ext import commands
from discord.ui import Button, View

cfx_path = Path.cwd() / 'sid' / 'json' / 'cfx.json'
cfx = json.load(open(cfx_path, encoding='utf-8'))

class User(commands.Cog):
    def __init__(self, Bot):
        self.Bot = Bot

    @commands.Cog.listener()
    async def on_ready(self):
        print('main cog is up')

    @commands.command()
    async def tm(self, ctx, *, arg: str):
        await ctx.send(arg)

async def setup(Bot):
    await Bot.add_cog(User(Bot))