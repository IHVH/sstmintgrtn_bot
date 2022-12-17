import discord
import json
import logging
from pathlib import Path
from discord.ext import commands
from discord import Webhook
import aiohttp

cfx_path = Path.cwd() / 'sid' / 'json' / 'cfx.json'
cfx = json.load(open(cfx_path, encoding='utf-8'))

class Main_Cog(commands.Cog):
    def __init__(self, Bot):
        self.Bot = Bot

    @commands.command()
    async def foo(self, ctx):
        async with aiohttp.ClientSession() as session:
            webhook = Webhook.from_url(cfx['WHT'], session=session)
            await webhook.send('Hello World', username='Foo')

    @commands.Cog.listener()
    async def on_ready(self):
        print(f'{self.__cog_name__} is up')
        logging.info(f'{self.__cog_name__} is up')

    @commands.command()
    async def tm(self, ctx, *, arg: str):
        await ctx.send(arg)

    @commands.command()
    async def dm(self, member: discord.Member, * ,arg):
        await member.send(arg)

    ###TODO -- не работает
    @commands.Cog.listener("on_message")
    async def ReactOnMessage(self, ctx, *, arg:str):
        if ctx.guild == None:
            channel = self.Bot.get_channel(cfx['sandbox_channel'])
            await channel.send(f'{ctx.author} написал в лс:')

        await self.Bot.process_commands(ctx)


    
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
    await Bot.add_cog(Main_Cog(Bot))