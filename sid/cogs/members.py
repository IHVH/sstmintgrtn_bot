import discord
import json
import logging
from pathlib import Path
from discord import Color
from discord.ext import commands


cfx_path = Path.cwd() / 'sid' / 'json' / 'cfx.json'
cfx = json.load(open(cfx_path, encoding='utf-8'))

colour_path = Path.cwd() / 'sid' / 'json' / 'colours.json'
colour = json.load(open(colour_path, encoding='utf-8'))

class Members_Cog(commands.Cog):
    def __init__(self, Bot):
        self.Bot = Bot

    @commands.Cog.listener()
    async def on_ready(self):
        print(f'{self.__cog_name__} is up')
        logging.info(f'{self.__cog_name__} is up')

    @commands.Cog.listener()
    async def on_member_joined(self, member: discord.Member):
        channel = self.Bot.get_channel(cfx['info_channel'])

        embed = discord.Embed(title=f'{member.display_name} - Прибыл на сервер', description="\uFEFF", colour=Color.from_str(colour['red']))
        embed.add_field(name="Member name", value=member.mention, inline=True)
        embed.add_field(name="Joined at", value=member.joined_at.strftime("%A, %B %d %Y @ %H:%M:%S %p"), inline=False)
        embed.add_field(name="Created at", value=member.created_at.strftime("%A, %B %d %Y @ %H:%M:%S %p"), inline=False)

        await channel.send(embed=embed)

    @commands.Cog.listener()
    async def on_member_remove(self, member: discord.Member):
        channel = self.Bot.get_channel(cfx['info_channel'])

        embed = discord.Embed(title=f'{member.display_name} - Покинул сервер', description="\uFEFF", colour=Color.from_str(colour['red']))
        embed.add_field(name="Member name", value=member.mention, inline=True)
        embed.add_field(name="Joined at", value=member.joined_at.strftime("%A, %B %d %Y @ %H:%M:%S %p"), inline=False)
        embed.add_field(name="Created at", value=member.created_at.strftime("%A, %B %d %Y @ %H:%M:%S %p"), inline=False)

        await channel.send(embed=embed)

    @commands.command()
    async def user(self, ctx, member: discord.Member):
        '''
        Позволяет посмотреть информацию о пользователе
        формат - user <тег пользователя/ID пользователя>
        '''
        embed = discord.Embed(title=f'{member.display_name} - info', description="\uFEFF", colour=Color.from_str(colour['blue']))
        embed.add_field(name="Member name", value=member.mention, inline=False)
        embed.add_field(name="Member ID", value=member.id, inline=False)
        embed.add_field(name="Timeout", value=member.timed_out_until, inline=False)
        embed.add_field(name="Bot", value=member.bot, inline=False)
        embed.add_field(name="Status", value=member.status, inline=False)
        embed.add_field(name="Joined at", value=member.joined_at.strftime("%A, %B %d %Y @ %H:%M:%S %p"), inline=False)
        embed.add_field(name="Created at", value=member.created_at.strftime("%A, %B %d %Y @ %H:%M:%S %p"), inline=False)
        await ctx.send(embed=embed)

async def setup(Bot):
    await Bot.add_cog(Members_Cog(Bot))