"""The main file, controls the Cogs and termial"""

import json
import os
import sys

import fbchat.models as model
from fbchat import Client

import tags
import cogs


class SharpBot(Client):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.thread_type = None
        self.thread_id = None
        self.string = None
        self.author = None
        self.pause = False

    def onMessage(
        self, author_id, message_object, thread_id, thread_type,
        **kwargs
    ):
        self.string = message_object.text
        self.thread_id = thread_id
        self.author = author_id
        self.thread_type = thread_type
        self.find()

    def message(self, message):
        client.send(
            model.Message(text=str(message)),
            thread_id=self.thread_id,
            thread_type=self.thread_type
        )

    def find(self):
        if self.string.startswith(tags.default):
            if self.admin(self.author) is True:
                self.command()
                return

            if self.pause is True:
                self.message("Sorry, the bot is currently disabled.")
                return

            if self.check(self.author) is True:
                self.message("Sorry, you are banned")
                return

            else:
                self.command()

    def command(self):
        self.string = (
            self.string.
            replace(tags.default, "", 1)
        )
        func, *args = self.string.split()
        try:
            tags.commands[func.lower()](self, *args)

        except KeyError:
            pass

        except TypeError:
            self.message(
                "Sorry, please check you typed the command correctly"
                "- TypeError"
            )

            tags.commands[func.lower()](self, *args)

    def admin(self, x):
        x = str(x)
        if x in os.environ["ADMINS"]:
            return True

        if x == str(client.uid):
            return True

    def mod(self, x):
        return x in os.environ["MODS"]

    def check(self, x):
        current = self.read('ban')

        for i in current.keys():
            if i == str(x):
                return True

    def bot(self):
        return client

    def read(self, x='ban'):
        if x == 'users':
            with open('data/memory.json') as f:
                data = json.load(f)
                Users = [
                    row["Users"] for row in data["data"] if "Users" in row
                ][0]
                return Users

        if x == 'ban':
            with open('data/memory.json') as f:
                data = json.load(f)
                Banned = [
                    row["Banned"] for row in data["data"] if "Banned" in row
                ][0]
                return Banned

    def write(self, data, place, *args):
        if place == 'ban':
            try:
                ban = self.read('ban')
                ban[data] = ''.join(args)
                user = self.read("users")

            except Exception:
                if type(data) is dict:
                    ban = data
                    user = self.read("users")

        if place == 'users':
            user = data
            ban = self.read('ban')

        users = user
        banned = ban

        dic = {
            "Users": users,
            "Banned": banned
        }

        filename = "data/memory.json"

        json_dict = {}
        data = []

        for k, v in dic.items():
            tmp_dict = {}
            tmp_dict[k] = v
            data.append(tmp_dict)

        json_dict["filename"] = filename
        json_dict["data"] = data

        with open("data/memory.json", "w") as outfile:
            json.dump(json_dict, outfile, indent=4, sort_keys=True)

    """You can check if your cog works by writing it here first."""


if os.environ["GITLAB"] == "DEPLOY":
    sys.exit()

else:
    try:
        with open("data/memory.json", "x") as outfile:
            outfile.write("""s
                {
                    "data": [
                        {
                            "Users": {}
                        },
                        {
                            "Banned": {}
                        }
                    ],
                    "filename": "data/memory.json"
                }
            """)

    except FileExistsError:
        pass

    print("\n\n\n\n")
    text = (
        f"                    SHARPBOT                     \n\n"
        f"                 Version : 0.2.0                 \n\n"
        f"* * * * * * * * * * * * * * * * * * * * * * * * *\n\n"
        f"Plugins:                                         \n\n"
        f"{cogs.mods}                                        \n"
    )

    print("Loading.....")

    client = SharpBot(
        os.environ["EMAIL"],
        os.environ["PASS"],
        logging_level=30)

    print("\n\n\n\n")
    print("Successfully logged in.  (Listening)")
    client.listen()
