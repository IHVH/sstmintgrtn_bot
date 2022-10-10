import discord
import os
from discord import Message, message
from discord.ext import commands
from discord.ui import Button, View

prefix = os.environ["PREFIX"]
token = os.environ["DBOTTOKEN"]
intents = discord.Intents.all()
intents.message_content = True
#у изменения активности есть варианты - streaming, playing, listening, watching, competing
# + есть варианты unknown и custom - первый говорит сам за себя, а как работает второй я пока не понял
activity = discord.Activity(name='голоса в своей голове', type=discord.ActivityType.listening)
Bot = commands.Bot(command_prefix=prefix, activity=activity, intents=intents)

# Проверка базового функционала сообщений
# P.S. я так и не понял почему он копирует все переданное после команды сообщение только если в аргументах функции есть *, arg после контекста
# P.S.S - по поводу контекта - https://discordpy.readthedocs.io/en/latest/ext/commands/api.html#discord.ext.commands.Context
@Bot.command()
async def tm(ctx, *, arg: str):
    await ctx.send(arg)

#TODO - базовый функционал эмодзи + callback на нажатия 
# -- Все еще не работает
@Bot.command()
async def et(ctx):
    await ctx.send("tst_msg")
    emoji = '🤔'
    await ctx.message.add_reaction(emoji)

#TODO - сообщения в личку
@Bot.command()
async def dm(ctx):
    user = Bot.get_user(ctx.author.id)
    await user.send(f'no way!\ndm is working!')

# Проверка базового функционала кнопок через UI дискорда
@Bot.command()
async def test(ctx):
        # callback функционал - в данном виде редактирует сообщение делая его "пустым"
        # сделать его полностью пустым сделав " " нельзя, дискорд будет ругатся, но при желании можно удалить все сообщение
        async def button_callback(interaction):
            await interaction.response.edit_message(content="_", view=None)

        button = Button(label="BTN_TST", style=discord.ButtonStyle.danger, custom_id='button1')
        view = View()
        view.add_item(button)

        await ctx.send(view=view)

        button.callback = button_callback

Bot.run(token)