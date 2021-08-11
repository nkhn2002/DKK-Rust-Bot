from discord.embeds import Embed
from discord.ext import commands
from discord.ext.commands import Cog

from core.embed import default_embed
from modules.enemy import EnemyModule

EMBED = default_embed()

class Enemy(Cog):

    def __init__(self, bot) -> None:
        self.bot = bot

    @commands.command(name="enemy")
    async def execute(self, ctx, *args):
        """ Add, remove enemies from the list and view the list of enemies """
        enemy = ' '.join(args[1:])        

        if args[0] == "list":
            await ctx.send(embed=EnemyModule.check_enemy_activity(EnemyModule.get_enemy_list()))
            
        elif args[0] == "add":
            EnemyModule.add_enemy_to_list(enemy)
            EMBED.title = "Success"
            EMBED.description = "Successfully added " + f'\'{enemy}\'' + " as an enemy!"
            await ctx.send(embed=EMBED)
        
        elif args[0] == "del":
            if EnemyModule.remove_enemy_from_list(enemy):
                EMBED.title = "Success"
                EMBED.description = "Successfully removed " + f'\'{enemy}\'' + " as an enemy!"
                await ctx.send(embed=EMBED)

            elif not EnemyModule.remove_enemy_from_list(enemy):
                EMBED.title = "Error"
                EMBED.description = "That player is not in the enemy list!"
                await ctx.send(embed=EMBED)

            else:
                EMBED.title = "Error"
                EMBED.description = "Something went wrong while removing enemy"
                await ctx.send(embed=EMBED)


def setup(bot):
    bot.add_cog(Enemy(bot))