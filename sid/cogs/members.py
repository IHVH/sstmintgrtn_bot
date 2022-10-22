import discord
import json
import logging
from pathlib import Path
from discord import Message, message
from discord.ext import commands
from discord.ui import Button, View


cfx_path = Path.cwd() / 'sid' / 'json' / 'cfx.json'
cfx = json.load(open(cfx_path, encoding='utf-8'))

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
        await channel.send(f'{member.display_name} Вошел в {member.joined_at}')

    @commands.Cog.listener()
    async def on_member_remove(self, member: discord.Member):
        channel = self.Bot.get_channel(cfx['info_channel'])
        await channel.send(f'{member.display_name} Вышел в {member.removed_at}')

async def setup(Bot):
    await Bot.add_cog(MembersCog(Bot))