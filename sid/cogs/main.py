import discord
import json
import logging
from pathlib import Path
from discord import Message, message
from discord.ext import commands
from discord.ui import Button, View

cfx_path = Path.cwd() / 'sid' / 'json' / 'cfx.json'
cfx = json.load(open(cfx_path, encoding='utf-8'))

class Main_Cog(commands.Cog):
    def __init__(self, Bot):
        self.Bot = Bot

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

    @commands.Cog.listener("on_message")
    async def on_message(self, message, *, arg:str):
        print("a")
        if not message.guild and message.author != self.Bot.user:
            channel = self.Bot.get_channel(cfx['sandbox_channel'])

            await channel.send(f'{message.author} написал в лс:')
            print(f'\nworking?')
        else:
                print(f'\nwhy?')

        await self.bot.process_commands(message)


    
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