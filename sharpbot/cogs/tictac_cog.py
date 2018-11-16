import fbchat.models as model

import tags


@tags.tag('games')
def tictac(self):
    """
    Give this 2 cordinates and it give's the linear equation.
    """

    for keys in players:
        if self.author in keys:
            self.message("Sorry, you are already in a game, try playing it!")
            return

    if player.one is None:
        player.one = [self.author, self.thread_id, self.thread_type]
        self.message(
            "Waiting for second player... ("
            + tags.default + "tictac)")
        return

    elif player.two is None:
        player.two = [self.author, self.thread_id, self.thread_type]
        players[
            player.one[0],
            player.two[0]
        ] = tictacC(
            self.bot(),
            player.one[0],
            player.one[1],
            player.one[2],
            player.two[0],
            player.two[1],
            player.two[2])

        players[player.one[0], player.two[0]].send()

        player.one = None
        player.two = None
        return
    return


@tags.tag('games')
def box(self, x):
    """
    Add a piece to the board
    """

    for keys in players:
        if self.author in keys:
            players[keys].box(x, self.author)
            return

    self.message(
        "You have not started a game yet, do "
        + tags.default + "tictac")


@tags.tag('game')
def end(self):
    """
    End a game of tictac
    """

    for keys in players:
        if self.author in keys:
            players[keys].end(self.author)
            return

    self.message(
        "You have not started a game yet, do "
        + tags.default + "tictac")


class tictacC():
    def __init__(self, client, player1, id1, type1, player2, id2, type2):
        self.board = self.make()
        self.player1 = player1
        self.player2 = player2
        self.thread1 = id1
        self.thread_type1 = type1
        self.thread2 = id2
        self.thread_type2 = type2
        self.turn = 1
        self.fill = 0
        self.game = True
        self.client = client
        if self.thread1 == self.thread2:
            self.message1("Its your turn. (Player 1)")
        else:
            self.message2("Game started, wait for your turn...")
            self.message1("Its your turn. (Player 1)")

    def message(self, message):
        if self.game is False:
            return

        if self.thread1 == self.thread2:

            self.client.send(
                model.Message(text=message),
                thread_id=self.thread1,
                thread_type=self.thread_type1)

        else:

            self.client.send(
                model.Message(text=message),
                thread_id=self.thread1,
                thread_type=self.thread_type1)

            self.client.send(
                model.Message(text=message),
                thread_id=self.thread2,
                thread_type=self.thread_type2)

    def message1(self, message):
        if self.game is False:
            return

        self.client.send(
            model.Message(text=message),
            thread_id=self.thread1,
            thread_type=self.thread_type1)

    def message2(self, message):
        if self.game is False:
            return

        self.client.send(
            model.Message(text=message),
            thread_id=self.thread2,
            thread_type=self.thread_type2)

    def make(self):
        board = [
            '  1  ', '  2  ', '  3  ', '  4  ',
            '  5  ', '  6  ', '  7  ', '  8  ', '  9  '
        ]
        return board

    def send(self):
        text = "?🀄🀄🀄🀄🀄?\n\n       :Board:\n\n{}\n\n{}\n\n{}\n\n?🀄🀄🀄🀄🀄?"
        self.message(
            text.format(
                self.pretty(self.board[0:3]),
                self.pretty(self.board[3:6]),
                self.pretty(self.board[6:9]))
        )

    def box(self, x, author):
        if author == self.player1:
            x = int(x)
            if self.turn is 2:
                if self.author1 == self.author2:
                    pass

                else:
                    self.message1("Sorry, it is not you turn.")
                    return

            if self.board[x-1] == ' ⛔️ ' or self.board[x-1] == ' ❎ ':
                self.message1("There is already a piece here.")
                return

            self.board[x-1] = ' ❎ '
            self.possibilities()
            self.message2("Its your turn. (Player 2)")
            self.send()
            self.turn = 2
            self.fill += 1
            return

        if author == self.player2:
            x = int(x)
            if self.turn is 1:
                if self.author1 == self.author2:
                    pass
                else:
                    self.message2("Sorry, it is not you turn.")
                    return

            if self.board[x-1] == ' ❎ ' or self.board[x-1] == ' ⛔️ ':
                self.message2("There is already a piece here.")
                return

            self.board[x-1] = ' ⛔️ '
            self.possibilities()
            self.message1("Its your turn. (Player 1)")
            self.send()
            self.turn = 1
            self.fill += 1
            return

    def check_win(self, x, y, z):
        if all(self.board[i] == ' ❎ ' for i in (x, y, z)):
            if self.thread1 == self.thread2:
                self.message("Player 1 Wins!")
                self.send()
                self.end()
            else:
                self.message1("You Win!")
                self.message2("You Lose.")
                self.send()
                self.end()

        if all(self.board[i] == ' ⛔️ ' for i in (x, y, z)):
            if self.thread1 == self.thread2:
                self.message("Player 2 Wins")
                self.send()
                self.end()

            else:
                self.message1("You Lose.")
                self.message2("You Win!")
                self.send()
                self.end()

    def possibilities(self):
        if self.fill == 8:
            self.message("Its a tie.")
            self.send()
            self.end()
            return
        else:
            self.check_win(0, 1, 2)
            self.check_win(3, 4, 5)
            self.check_win(6, 7, 8)
            self.check_win(0, 3, 6)
            self.check_win(1, 4, 7)
            self.check_win(2, 5, 8)
            self.check_win(0, 4, 8)
            self.check_win(2, 4, 6)

    def pretty(self, x):
        x = str(x)
        x = x.translate(str.maketrans("'", "|", ",[]"))
        return x

    def end(self):
        del players[self.player1, self.player2]
        self.game = False


class player():
    def __init__(self):
        self.one = None
        self.two = None


players = {}
player = player()
