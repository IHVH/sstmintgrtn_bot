import requests
import logging
import libgravatar
from discord.ext import commands

class Request_Cog(commands.Cog):
    def __init__(self, Bot):
        self.Bot = Bot
    
    @commands.Cog.listener()
    async def on_ready(self):
        print(f'{self.__cog_name__} is up')
        logging.info(f'{self.__cog_name__} is up')

    @commands.command()
    async def req_test(self, ctx):
        req = requests.get('https://randomfox.ca/floof/')
        req = req.json()
        await ctx.send(req['image'])

    @commands.command()
    async def grav(self, ctx, arg):
        email = libgravatar.Gravatar(arg)
        await ctx.send(email.get_image())
        await ctx.send(email.get_image(default='identicon', force_default=True))
        await ctx.send(email.get_image(default='monsterid', force_default=True))
        await ctx.send(email.get_image(default='wavatar', force_default=True))
        await ctx.send(email.get_image(default='robohash', force_default=True))
        await ctx.send(email.get_image(default='retro', force_default=True))

async def setup(Bot):
    await Bot.add_cog(Request_Cog(Bot))