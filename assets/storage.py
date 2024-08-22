import configparser
import os
import json 

class Storage:
    def __init__(self) -> None:
        self.config = configparser.ConfigParser()
        self.table = {}
        
        if not os.path.exists("table.json"):
            with open("table.json","w") as t:
                t.write("{}")
        
        self.config.read("config.ini")
        self.remote = self.config["DEFAULT"].getboolean("remote",fallback=False)
        self.remoteurl = self.config["DEFAULT"].get("remoteurl",fallback="127.0.0.1")

    #TODO add config.ini saving

    def load(self) -> dict:
        """Load a table from a file/remote server"""
        if self.remote:
            pass
            #TODO
        else:
            if os.path.exists("table.json"):
                with open("table.json","r") as t:
                    self.table = json.loads(t.read())
        return self.table

    def save(self):
        """Save the table to a file/remote server"""

        if self.remote:
            #TODO
            pass
        else:
            if os.path.exists("table.json"):
                    with open("table.json","w") as t:
                        t.write(json.dumps(self.table))