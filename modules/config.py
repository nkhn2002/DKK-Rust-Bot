import json

class ConfigModule:

    @staticmethod
    def get_server_id():
        """ return the current server id """
        with open("data.json", "r") as file:
            data = json.load(file)

            id = data["server_id"]

            return id
    
    @staticmethod
    def set_server_id(server_id):
        """ Set server id """

        def write_to_file(data):
            with open("data.json", "w") as file2:
                json.dump(data, file2, indent=4)

        with open("data.json", "r") as file:
            data = json.load(file)
            data["server_id"] = server_id
            write_to_file(data)
        