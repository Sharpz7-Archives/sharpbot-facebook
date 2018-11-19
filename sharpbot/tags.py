"""This is a short description of the file."""

commands = {}
functions = []
default = "!"


def tag(comm="command"):
    """A decorator that allows for the commands to generate themselves."""

    def actual_decorator(func):
        try:
            globals().get(comm, command).create(func)
        except Exception:
            command.create(func)

        return func
    return actual_decorator


def find(_type):
    """Return the list of Pages when called."""

    try:
        return globals().get(_type.lower(), command).pages
    except Exception:
        return command.pages


class Pages():
    """
    Creates the new page instance.

    Allows for lots of pages with less code.
    """

    def __init__(self, page_type):
        """Initialise class attributes."""
        self.page_type = page_type
        self.category = {}
        self.help = {}
        self.pages = [{}]

    def create(self, func):
        """Create a new page."""

        commands[func.__name__] = func
        self.category[func.__name__] = func

        self.help["!" + str(func.__name__)] = "- " + func.__doc__.translate(
            str.maketrans('', '', "\n"))

        if (len(self.category) + 5) % 5 == 0:

            self.pages[-1].update(self.help.copy())
            self.help.clear()
            self.pages.append(dict())
        else:
            self.pages[-1].update(self.help.copy())


# Normal commands:
command = Pages("normal")

# Extra Commands:
admin = Pages("admin")
functions.append("admin")

games = Pages("games")
functions.append("games")

maths = Pages("maths")
functions.append("maths")
