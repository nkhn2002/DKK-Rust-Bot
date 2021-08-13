import time, asyncio

from discord.ext import commands
from discord.ext.commands import Cog
from cogs.enemy import EnemyModule

from core.bot_settings import ENEMY_LOOP_CHANNEL

class EnemyLoop(Cog):
    def __init__(self, bot) -> None:
        self.bot = bot

    @Cog.listener()
    async def on_ready(self):
        asyncio.get_event_loop().create_task(EnemyLoop.run_loop(self))
        print("Starting enemy checker loop")

    async def run_loop(self):
        while True:
            channel = self.bot.get_channel(ENEMY_LOOP_CHANNEL)
            await channel.send(embed=EnemyModule.check_enemy_activity(EnemyModule.get_enemy_list()))
            await asyncio.sleep(300)

def setup(bot):
    bot.add_cog(EnemyLoop(bot))