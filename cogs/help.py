import datetime

from discord.ext import commands
from discord.ext.commands import Cog

from core.embed import default_embed

EMBED = default_embed()

class Help(Cog):
    def __init__(self, bot) -> None:
        self.bot = bot

    @commands.command(name="help")
    async def execute(self, ctx, *args):
        EMBED.title = "Available Commands"
        EMBED.description = "_jesper lugter :D_"
        EMBED.add_field(name="Enemy", # Enemy commands
                        value=".enemy list - shows list of current enemies\n.enemy add <name> - add enemy to list\n.enemy del <name> - remove enemy from list",
                        inline=False)
        EMBED.add_field(name="Server",
                        value=".server set <id> - set current server id\n",
                        inline=False)
        EMBED.add_field(name="Miscellaneous", # Misc commands
                        value=".clear - clear all messages",
                        inline=False)
        
        EMBED.set_footer(text='Developed by: scoot#2395 | %s' % (datetime.datetime.utcnow()))

        await ctx.send(embed=EMBED)


def setup(bot):
    bot.add_cog(Help(bot))