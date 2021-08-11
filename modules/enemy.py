import json
import requests
import asyncio
import time

from modules.config import ConfigModule

from core.embed import default_embed

class EnemyModule:

    @staticmethod
    def get_enemy_list() -> list:
        """ Return the list of enemy names """
        with open("data.json", "r") as file:
            data = json.load(file)
            names = data["enemy_data"]["names"]

            return names
    
    @staticmethod
    def check_enemy_activity(names):
        """ Check if enemies are online on the current server """
        
        EMBED_MSG = ""
        ONLINE = []
        OFFLINE = []

        server_id = ConfigModule.get_server_id()
        res = requests.get(f"https://api.battlemetrics.com/servers/{server_id}?include=session").text

        for name in names:
            if name in res:
                ONLINE.append(name)
            else:
                OFFLINE.append(name)

        for name in ONLINE:
            EMBED_MSG += name + " - Online\n"

        for name in OFFLINE:
            EMBED_MSG += name + " - Offline\n"

        embed = default_embed()
        embed.title = "Enemy Checker"
        embed.description = EMBED_MSG

        return embed

    @staticmethod
    def remove_enemy_from_list(name):
        """ Remove enemy from enemy list """

        def write_to_file(data):
            with open("data.json", "w") as file2:
                json.dump(data, file2, indent=4)

        with open("data.json", "r") as file:
            data = json.load(file)
            for _name in data["enemy_data"]["names"]:
                if name == _name:
                    data["enemy_data"]["names"].remove(name)
                    write_to_file(data)
                    return True
                    
            return False

    @staticmethod
    def add_enemy_to_list(name):
        """ Add enemy to enemy list """

        with open("data.json", "r") as file:
            data = json.load(file)
            data["enemy_data"]["names"].append(name)
            
        with open("data.json", "w") as file2:
            json.dump(data, file2, indent=4)