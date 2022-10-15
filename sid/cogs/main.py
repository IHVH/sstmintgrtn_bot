import discord
import json
from pathlib import Path
from discord import Message, message
from discord.ext import commands
from discord.ui import Button, View

cwd = Path(__file__).parents[1]
cwd = str(cwd)
cfx = json.load(open(cwd+'\json\cfx.json', encoding='utf-8'))

class User(commands.cog):
    def __init__(self, Bot):
        self.Bot = Bot

    @commands.Cog.listener()
    async def on_ready(self, ctx):
        await ctx.send("ready")

    @commands.command()
    async def tm(ctx, *, arg: str):
        await ctx.send(arg)

async def setup(Bot):
    await Bot.add_cog(User(Bot))