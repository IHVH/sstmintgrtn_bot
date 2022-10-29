import discord
import json
import logging
from pathlib import Path
from discord import Message, message
from discord.ext import commands
from discord.ui import Button, View

cfx_path = Path.cwd() / 'sid' / 'json' / 'cfx.json'
cfx = json.load(open(cfx_path, encoding='utf-8'))

class Owner_Cog(commands.Cog):
    def __init__(self, Bot):
        self.Bot = Bot

    @commands.Cog.listener()
    async def on_ready(self):
        print('owner cog is up')
        logging.info('owner cog is up')

    @commands.command(pass_context=True)
    @commands.is_owner()
    async def load(self, ctx, extension):
        try:
            self.Bot.load_extension(f"cogs.{extension}")
        except Exception as e:
            await ctx.send(f'**`ERROR:`** {type(e).__name__} - {e}')
        else:
            await ctx.send('**`SUCCESS`**')

    @commands.command(pass_context=True)
    @commands.is_owner()
    async def unload(self, ctx, extension):
        try:
             self.Bot.unload_extension(f"cogs.{extension}")
        except Exception as e:
            await ctx.send(f'**`ERROR:`** {type(e).__name__} - {e}')
        else:
            await ctx.send('**`SUCCESS`**')

    @commands.command(pass_context=True)
    @commands.is_owner()
    async def reload(self, ctx, extension):
        try:
            self.Bot.unload_extension(f"cogs.{extension}")
            self.Bot.load_extension(f"cogs.{extension}")
        except Exception as e:
            await ctx.send(f'**`ERROR:`** {type(e).__name__} - {e}')
        else:
            await ctx.send('**`SUCCESS`**')


async def setup(Bot):
    await Bot.add_cog(Owner_Cog(Bot))