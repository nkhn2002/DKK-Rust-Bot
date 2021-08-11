from discord.ext import commands
from discord.ext.commands import Cog

class Misc(Cog):
    def __init__(self, bot) -> None:
        self.bot = bot

    @commands.command(name="clear")
    async def clear(self, ctx, amount=None):
        if amount == None:
            await ctx.channel.purge(limit=1000000)
        else:
            try:
                int(amount)
            except: # Error handler
                await ctx.send('Enter a valid amount.')
            else:
                await ctx.channel.purge(limit=amount)

def setup(bot):
    bot.add_cog(Misc(bot))