import logging
from discord.ext import commands

class Owner_Cog(commands.Cog):
    def __init__(self, Bot):
        self.Bot = Bot

    @commands.Cog.listener()
    async def on_ready(self):
        print(f'{self.__cog_name__} is up')
        logging.info(f'{self.__cog_name__} is up')

    @commands.command(pass_context=True)
    @commands.is_owner()
    async def load(self, ctx, extension):
        try:
            self.Bot.load_extension(f"cogs.{extension}")
        except Exception as e:
            await ctx.send(f'**`ERROR:`** {type(e).__name__} - {e}')
        else:
            await ctx.send(f'{extension} loaded successfully')

    @commands.command(pass_context=True)
    @commands.is_owner()
    async def unload(self, ctx, extension):
        try:
             self.Bot.unload_extension(f"cogs.{extension}")
        except Exception as e:
            await ctx.send(f'**`ERROR:`** {type(e).__name__} - {e}')
        else:
            await ctx.send(f'{extension} loaded successfully')

    @commands.command(pass_context=True)
    @commands.is_owner()
    async def reload(self, ctx, extension):
        try:
            self.Bot.unload_extension(f"cogs.{extension}")
            self.Bot.load_extension(f"cogs.{extension}")
        except Exception as e:
            await ctx.send(f'**`ERROR:`** {type(e).__name__} - {e}')
        else:
            await ctx.send(f'{extension} loaded successfully')


async def setup(Bot):
    await Bot.add_cog(Owner_Cog(Bot))