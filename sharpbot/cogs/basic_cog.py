import os
import pprint
import sys
from fuzzywuzzy import fuzz

import json
import tags


@tags.tag()
def help(self):
    """
    Get infomation about the bot.
    """

    text = (
        "⚔️ Hello,  I am Sharpbot. ⚔️\n\nI am made just for fun, so try me "
        "out!\n\nYou can do `" + tags.default +
        "commands` to get a list of all the commands "
        "you can use.\n\n⚔️ Disclaimer: This bot can read your messages"
        " for obvious reasons. ⚔️"
    )
    self.message(text)


@tags.tag()
def commands(self, Type="normal", x=1):
    """
    Gets the list of commands.
    """

    try:
        if Type.isdigit() is True:
            x = Type
            Type = None
    except Exception:
        pass
    x = int(x) - 1
    if not isinstance(x, int):
        x = 0
    if x >= len(tags.find(Type)):
        x = len(tags.find(Type)) - 1
    format_args = []
    for i in tags.find(Type)[x].items():
        format_args.append(i)
        format_args.append(None)
    comms = (
        str(pprint.pformat(format_args))
        .translate(str.maketrans('', '', "',()[]")).
        replace("None", "")
    )

    text = (
        "⚔️ Sharpbot commands: ⚔️\n\n{}\n\nPage {} / {}\n\n"
        "Do " + tags.default + "commands (Catagory) (Page number)\n\n"
        "⚔️Current Catagories are {}⚔️"
    )
    self.message(text.format(
        comms, x + 1,
        len(tags.find(Type)),
        tags.functions)
    )


@tags.tag('admin')
def ban(self, *args):
    """
    Bans a player from using the bot.
    """

    string = ' '.join(args)
    string = string.split(" ! ")
    thread = string[0]
    try:
        reason = string[1]
    except Exception:
        reason = "No reason given."

    if self.admin(self.author) is True:
        if thread.startswith("@"):
            thread = thread[1:]

        if thread.isdigit() is True:
            self.write(thread, 'ban', reason)
            self.message("User is banned")

        else:
            users = self.read('users')
            for key, value in users.items():
                if key == thread:
                    thread = value

            if thread.isdigit() is False:
                self.message("Name was not found. did you spell it correctly?")
                return

            self.write(thread, 'ban', reason)
            self.message("User is banned")

    else:
        self.message("Sorry, you are not a Admin.")


@tags.tag('admin')
def unban(self, *args):
    """
    Unbans a player from using the bot.
    """

    if self.admin(self.author) is True:
        thread = ' '.join(args)
        if thread.startswith("@"):
            thread = thread[1:]

        if thread.isdigit() is True:
            check = self.read('ban')
            for k, v in check.items():
                if k == thread:
                    self.message("User was unbanned")
                    del check[k]
                    self.write(check, 'ban')
                    return

        else:
            users = self.read('users')
            for key, value in users.items():
                if key == thread:
                    thread = value

            check = self.read('ban')
            for k, v in check.items():
                if k == thread:
                    self.message("User was unbanned")
                    del check[k]
                    self.write(check, 'ban')
                    return
    else:
        self.message("Sorry, you are not an Admin")


@tags.tag('admin')
def update(self):
    """
    Updates the Users list.
    """

    if self.admin(self.author) is True:
        self.message("...")
        self.thread = Threads(self.bot())

        self.write(self.thread.get(), 'users')
        self.message("Database Updated")
        self.message(str(self.read('users')))

    else:
        self.message("Sorry, you are not an Admin")


@tags.tag('admin')
def restart(self):
    """
    Restarts the bot.
    """

    if self.admin(self.author) is True:
        self.message("Restarting...")
        os.execl(sys.executable, sys.executable, *sys.argv)
    else:
        self.message("Sorry, you are not an Admin")


@tags.tag('admin')
def disable(self):
    """
    Disables the bot.
    """

    if self.admin(self.author) is True:
        self.pause = True
        self.message("Bot disabled")
    else:
        self.message("Sorry, you are not an admin.")


@tags.tag('admin')
def enable(self):
    """
    Enables the bot.
    """

    if self.admin(self.author) is True:
        self.pause = False
        self.message("Bot enabled")
    else:
        self.message("Sorry, you are not an admin.")


@tags.tag('admin')
def read(self):
    """
    Reads the Database.
    """

    if self.admin(self.author) is True:
        text = self.read('users')
        self.message(pprint.pformat(text, width=1))

    else:
        self.message("Sorry, you are not an admin.")


@tags.tag('admin')
def reset(self):
    """
    Reset the bots Databases.
    """

    if self.admin(self.author) is True:
        users = {}
        banned = {}

        dic = {
            "Users": users,
            "Banned": banned
        }

        filename = "memory.json"

        json_dict = {}
        data = []

        for k, v in dic.items():
            tmp_dict = {}
            tmp_dict[k] = v
            data.append(tmp_dict)

        json_dict["filename"] = filename
        json_dict["data"] = data

        with open("memory.json", "x") as outfile:
            json.dump(json_dict, outfile, indent=4, sort_keys=True)

        self.message("Database reset.")
    else:
        self.message("Sorry, you are not a Admin.")


@tags.tag()
def info(self, *args):
    """
    Get users info.
    """

    try:
        if args == ():
            arg = str(self.author)
        else:
            arg = ' '.join(args)
            if arg.startswith("@"):
                arg = arg[1:]
        if arg.isdigit() is True:
            check = self.read('users')

            for key, value in check.items():
                if value == arg:
                    name = key

            if arg in os.environ["MODS"]:
                Mod = "Yes"
            else:
                Mod = "No"

            if arg in os.environ["ADMINS"]:
                admin = "Yes"
            else:
                admin = "No"

            if arg in self.read('ban'):
                banned = "Yes"
            else:
                banned = "No"
            text = (
                "⚔️ Player: {0} ⚔️\n\nThread_ID: {1}\n\nAdmin: {2}\n\n"
                "Mod: {3}\n\nBanned: {4}\n\n⚔️ Player: {0} ⚔️"
            )
            self.message(text.format(name, arg, admin, Mod, banned))

        else:
            check = self.read('users')

            for key, value in check.items():
                if fuzz.partial_ratio(key.lower(), arg.lower()) > 85:
                    thread = value
                    arg = key

            if thread in os.environ["MODS"]:
                Mod = "Yes"
            else:
                Mod = "No"

            if thread in os.environ["ADMINS"]:
                admin = "Yes"
            else:
                admin = "No"

            if thread in self.read('ban'):
                banned = "Yes"
            else:
                banned = "No"

            text = (
                "⚔️ Player: {0} ⚔️\n\nThread_ID: {1}\n\nAdmin: {2}\n\n"
                "Mod: {3}\n\nBanned: {4}\n\n⚔️ Player: {0} ⚔️"
            )
            self.message(text.format(arg, thread, admin, Mod, banned))

    except UnboundLocalError:
        self.message(
            "Sorry, there was a error. Did you type the name"
            "correctly? (UnboundLocalError)"
        )

    except AttributeError:
        self.message(
            "Sorry, there was a error. To use this command, "
            "you need to have done " + tags.default +
            "update once."
        )


class Threads():

    def __init__(self, client):
        self.client = client

    def remove_duplicates(self, values):
        output = []
        seen = set()
        for value in values:
            if value not in seen:
                output.append(value)
                seen.add(value)
        return output

    def find_threads(self):
        threads = self.client.fetchThreadList()
        allusers = []
        allusernames = []
        for i in threads:
            i = str(i)
            thread = (i.split('(')[1].split(')')[0]).replace(" ", "")
            test = i[1:2]
            if test is "G":
                try:
                    group = self.client.fetchGroupInfo(thread)[thread]
                    listid = group.participants
                    for item in listid:
                        name = self.client.fetchThreadInfo(item)[item]
                        final = name.name
                        allusers.append(item)
                        allusernames.append(final)
                except Exception:
                    pass

            if test is "U":
                person = self.client.fetchThreadInfo(thread)[thread]
                final = person.name
                allusers.append(thread)
                allusernames.append(final)

        return (self.remove_duplicates(allusernames),
                self.remove_duplicates(allusers))

    def get(self):
        list1, list2 = self.find_threads()
        database = dict(zip(list1, list2))
        return database
