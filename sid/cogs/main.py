import discord
import json
from discord import Message, message
from discord.ext import commands
from discord.ui import Button, View

class User(commands.cog):

    def __init__(self, Bot):
        self.Bot = Bot

    @commands.Cog.listener()
    async def on_ready(self, ctx):
        await ctx.send("ready")

    @commands.command()
    async def tm(ctx, *, arg: str):
        await ctx.send(arg, delete_after=3)

def setup(Bot):
    Bot.add_cog(User(Bot))