# DKK Rust Bot
# Developed by: scoot
import discord
import os

from discord.ext import commands

from cogs.enemy import EnemyModule
from core.bot_settings import TOKEN, PREFIX

class Bot:
    def __init__(self, token, prefix):
        self.token = token
        self.bot = commands.Bot(command_prefix=prefix, indents=discord.Intents.all(), case_sensitive=False)

        self.bot._token = token
        self.bot.remove_command('help')

    def load_cogs(self):
        for root, _, items in os.walk('cogs'):
            for item in items:
                if not item.endswith('.py') or item.startswith('__') or item.startswith('-'):
                    continue

                cog = os.path.join(root, item).replace(os.sep, '.')[:-3]

                try:
                    self.bot.load_extension(cog)

                    print(f'\x1b[92m\'{cog}\'\x1b[0m')
                except Exception as e:
                    print(f'\x1b[91m\'{cog}\' \x1b[0m: \x1b[90m{e}')

    def run(self):
        self.load_cogs()
        self.bot.run(self.token)

if __name__ == '__main__':
    bot = Bot(TOKEN, PREFIX)
    bot.run()