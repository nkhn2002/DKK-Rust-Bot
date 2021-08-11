from discord.ext import commands
from discord.ext.commands import Cog

class BotReady(Cog):
    def __init__(self, bot) -> None:
        self.bot = bot

    @Cog.listener()
    async def on_ready(self):
        print("\nRust Bot is online!")

def setup(bot):
    bot.add_cog(BotReady(bot))