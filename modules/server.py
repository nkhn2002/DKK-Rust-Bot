import requests, re

from discord.ext import commands
from discord.ext.commands import Cog

from modules.config import ConfigModule
from core.embed import default_embed

EMBED = default_embed()

class ServerModule():

  def server_information():
        server_id = ConfigModule.get_server_id()
        res = requests.get("https://www.battlemetrics.com/servers/rust/%s" % (server_id)).text

        regex = re.findall(r"\"game_id\":\"rust\",\"name\":\"(.+?)\",\"address\":\"(.+?)\",\".*port\":(.+?),\"port_query\":\d+,\"players\":(.+?),\"maxPlayers\":(.+?),\"", res)
        
        server_title = regex[0][0]
        server_ip = regex[0][1] + ":" + regex[0][2]
        server_player_count = regex[0][3] + "/" + regex[0][4]

        EMBED.add_field(name="Server ID", value=server_id, inline=False)
        EMBED.add_field(name="Server Title", value=server_title, inline=False)
        EMBED.add_field(name="Server IP", value=server_ip, inline=False)
        EMBED.add_field(name="Player Count", value=server_player_count, inline=False)

        return EMBED