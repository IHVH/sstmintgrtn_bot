import discord
import json
import logging
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
        logging.info('main cog is up')

    @commands.command()
    async def tm(self, ctx, *, arg: str):
        await ctx.send(arg)

    @commands.command()
    async def dm(self, ctx):
        user = self.Bot.get_user(ctx.author.id)
        await user.send(f'no way!\ndm is working!')

    
    # -- Тестирование Embed'а
    @commands.command()
    async def stats(self, ctx):
        dpyVersion  = discord.__version__
        serverCount = len(self.Bot.guilds)
        memberCount = len(set(self.Bot.get_all_members()))

        embed = discord.Embed(title=f'{self.Bot.user.name} Stats', description="\uFEFF", colour=ctx.author.colour)
        embed.add_field(name="API version", value=dpyVersion, inline=True)
        embed.add_field(name="Total guilds", value=serverCount, inline=True)
        embed.add_field(name="Total users", value=memberCount, inline=True)
        await ctx.send(embed=embed)

async def setup(Bot):
    await Bot.add_cog(User(Bot))