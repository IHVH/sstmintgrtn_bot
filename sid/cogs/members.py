import discord
import json
import logging
from pathlib import Path
from discord import Message, message, Color
from discord.ext import commands
from discord.ui import Button, View


cfx_path = Path.cwd() / 'sid' / 'json' / 'cfx.json'
cfx = json.load(open(cfx_path, encoding='utf-8'))

colour_path = Path.cwd() / 'sid' / 'json' / 'colours.json'
colour = json.load(open(colour_path, encoding='utf-8'))

class MembersCog(commands.Cog):
    def __init__(self, Bot):
        self.Bot = Bot

    @commands.Cog.listener()
    async def on_ready(self):
        print('members cog is up')
        logging.info('members cog is up')

    @commands.Cog.listener()
    async def on_member_joined(self, member: discord.Member):
        channel = self.Bot.get_channel(cfx['info_channel'])

        embed = discord.Embed(title=f'{member.display_name} - Прибыл на сервер', description="\uFEFF", colour=Color.from_str(colour['red']))
        embed.add_field(name="Member name", value=member.mention, inline=True)
        embed.add_field(name="Joined at", value=member.joined_at, inline=True)

        await channel.send(embed=embed)

    @commands.Cog.listener()
    async def on_member_remove(self, member: discord.Member):
        channel = self.Bot.get_channel(cfx['info_channel'])

        embed = discord.Embed(title=f'{member.display_name} - Покинул сервер', description="\uFEFF", colour=Color.from_str(colour['red']))
        embed.add_field(name="Member name", value=member.mention, inline=True)
        embed.add_field(name="Joined at", value=member.joined_at, inline=True)

        await channel.send(embed=embed)

    @commands.command()
    async def test(self, ctx, member: discord.Member):
        
        embed = discord.Embed(title=f'{member.display_name} - info', description="\uFEFF", colour=Color.from_str(colour['green']))
        embed.add_field(name="Member name", value=member.mention, inline=True)
        embed.add_field(name="Joined at", value=member.joined_at, inline=True)
        await ctx.send(embed=embed)

async def setup(Bot):
    await Bot.add_cog(MembersCog(Bot))