import random as ran
import re
import urllib.parse
import urllib.request

import urbandictionary as ud
import wikipedia

import tags


@tags.tag()
def wiki(self, *args):
    """
    Search wikipedia, add your keywords after !wiki
    """

    try:
        num = int(args[-1])
        text = ' '.join(list(args)[:-1])
    except Exception:
        num = 6
        text = ' '.join(list(args))
    try:
        result = wikipedia.summary(text, sentences=num)
        self.message(result)
    except wikipedia.exceptions.DisambiguationError as e:
        error = "Multiple items found, try:\n\n{}"

        self.message(error.format(str(e.options)))


@tags.tag()
def urban(self, *args):
    """
    Search urbandictionary, add your keywords after !urban
    """

    try:
        num = int(args[-1])
        defs = ud.define(' '.join(list(args)[:-1]))
    except Exception:
        num = 2
        defs = ud.define(' '.join(list(args)))

    if num == 0:
        num = len(defs)
    defs = defs[:num]
    for d in defs:
        self.message(d.definition)


@tags.tag()
def random(self):
    """
    Get a random word for urbandictionary.
    """

    rand = ud.random()[1:]
    for d in rand:
        word = (d.word)
        defs = (d.definition)

    text = "{}\n\n{}"
    self.message(text.format(word, defs))


@tags.tag()
def finlay(self):
    """
    Because he is funny - Over 250 defintions.
    """

    var = ran.randint(1, 5)
    if var == 1:
        defs = ud.define('Finlay')
        defs = ran.choice(defs)
        self.message(defs.definition)
    if var == 2:
        defs = ud.define('Finley')
        defs = ran.choice(defs)
        self.message(defs.definition)
    if var == 3:
        defs = ud.define('Finn')
        defs = ran.choice(defs)
        self.message(defs.definition)
    if var == 4:
        defs = ud.define('Findlay')
        defs = ran.choice(defs)
        self.message(defs.definition)
    if var == 5:
        defs = ud.define('Fin')
        defs = ran.choice(defs)
        self.message(defs.definition)


@tags.tag()
def youtube(self, *args):
    """
    Get a video from youtube.
    """

    search = ' '.join(args)
    query_string = urllib.parse.urlencode({"search_query": search})
    html_content = urllib.request.urlopen(
        "http://www.youtube.com/results?" +
        query_string
    )
    search_results = re.findall(
        r'href=\"\/watch\?v=(.{11})',
        html_content.read().decode())
    self.message("https://youtu.be/" + search_results[0])


@tags.tag()
def leaderboard(self):
    """
    Get a leaderboard of peoples scores.
    """

    pass


@tags.tag()
def test(self, x=None):
    """
    Test command.
    """

    pass


class Leader():
    def __init__(self):
        self.leaderboard = "test"
