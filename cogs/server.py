import datetime
from modules.config import ConfigModule

from discord.ext import commands
from discord.ext.commands import Cog

from core.embed import default_embed

EMBED = default_embed()

class Server(Cog):
    def __init__(self, bot) -> None:
        self.bot = bot

    @commands.command(name="server")
    async def execute(self, ctx, *args):
        if args[0] == "set":
            if len(args) < 1:
                EMBED.title = "Error"
                EMBED.description = "You have to add an ID while setting the server id!"
                await ctx.send(embed=EMBED)

            try:
                server_id = int(args[1])

            except:
                EMBED.title = "Error"
                EMBED.description = "Server ID can only be numbers!"
                await ctx.send(embed=EMBED)

            ConfigModule.set_server_id(server_id)
            EMBED.title = "Success"
            EMBED.description = "Successfully set server id"
            
            await ctx.send(embed=EMBED)

        


def setup(bot):
    bot.add_cog(Server(bot))