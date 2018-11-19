import tags
import random as ran
import fbchat.models as model


@tags.tag('games')
def t(self):
    """
    Adds a card to your blackjack game.
    """

    if (self.author, self.thread_id, self.thread_type) not in blackjack_dict:
        self.message(
            "A game has't been started, try '" + tags.default +
            "bjack'")
    else:

        blackjack_dict[self.author, self.thread_id, self.thread_type].vtwist()


@tags.tag('games')
def s(self):
    """
    Stops adding cards to your blackjack game.
    """

    if (self.author, self.thread_id, self.thread_type) not in blackjack_dict:
        self.message(
            "A game has't been started, try '" + tags.default +
            "bjack'")
    else:
        blackjack_dict[self.author, self.thread_id, self.thread_type].vstick()


@tags.tag('games')
def bjack(self):
    """
    Play a game of blackjack, get as close to 21 as you can.
    """

    if (self.author, self.thread_id, self.thread_type) not in blackjack_dict:

        blackjack_dict[
            self.author,
            self.thread_id,
            self.thread_type
        ] = Blackjack(
            self.author,
            self.thread_id,
            self.thread_type,
            self.bot()
        )

    blackjack_dict[self.author, self.thread_id, self.thread_type].bjack()


class Blackjack():
    def __init__(self, author, thread, thread_type, client):
        self.cpu = self.cards()
        self.player = self.cards()
        self.player2 = []
        self.author = author
        self.thread = thread
        self.thread_type = thread_type
        self.text = "♣ ♥ ♣\n{0}\n\nPlayer - {1}, Sharpbot - {2}\n♣ ♥ ♣"
        self.client = client

    def message(self, message):
        if self.author != 101:
            self.client.send(
                model.Message(text=message), thread_id=self.thread,
                thread_type=self.thread_type
            )
        else:
            print(message)

    def cards(self):
        hand = []
        suits = ['♥️', '♦️', '♣️', '♠️']
        ranks = [
            '2', '3', '4', '5', '6', '7', '8', '9',
            '10', 'J', 'Q', 'K', 'A'
        ]

        self.deck = [[y, x] for x in suits for y in ranks]

        first = ran.choice(self.deck)
        self.deck.remove(first)
        second = ran.choice(self.deck)
        self.deck.remove(second)
        hand.append(''.join(first))
        hand.append(''.join(second))
        return hand

    def twist(self, x):
        first = ran.choice(self.deck)
        self.deck.remove(first)
        x.append(''.join(first))
        return x

    def sumcard(self, args):
        cards1 = []
        cards2 = []
        total1 = 0
        total2 = 0
        for card in args:

            try:
                card = int(card[:-2])
                cards1.append(card)
                cards2.append(card)

            except Exception:
                if card[0] == 'A':
                    cards1.append(1)
                    cards2.append(11)

                else:
                    cards1.append(10)
                    cards2.append(10)

        for item in cards1:
            total1 += item

        for item in cards2:
            total2 += item

        return (total1, total2)

    def logic(self, x):
        total1 = self.sumcard(x)[0]
        total2 = self.sumcard(x)[1]
        if total2 <= 21:
            total = total2
        else:
            total = total1

        if total < 21 and total > 15:
            return x
        elif total < 15:
            self.twist(x)
            self.logic(x)
            return x

        else:
            return x

    def bjack(self):
        player = self.player
        total = self.sumcard(self.player)[0]
        total2 = self.sumcard(self.player)[1]
        if total == total2:
            text = (
                "♣ ♥ ♣\nTotal: {}\nCards = {}\n\nStick or Twist? :\n"
                "(type '" + tags.default +
                "t' to add a card, '" + tags.default + "s' to stay)\n♣ ♥ ♣"
            )
            text = text.format(total, player)
            self.message(text)
        else:
            text = (
                "♣ ♥ ♣\nTotal: {} or {}\nCards = {}\n\nStick or Twist? :\n"
                "(type '" + tags.default +
                "t' to add a card, '" + tags.default + "s' to stay)\n♣ ♥ ♣"
            )
            text = text.format(total, total2, player)
            self.message(text)

    def vtwist(self):
        self.player = self.twist(self.player)
        if self.sumcard(self.player)[0] >= 21:
            self.vstick()

        else:
            self.bjack()

    def vstick(self, bust=False):
        if bust is False:
            self.cpu = self.logic(self.cpu)
        cpu = self.sumcard(self.cpu)[0]
        player1 = self.sumcard(self.player)[0]
        player2 = self.sumcard(self.player)[1]
        if player2 <= 21:
            player = player2
        else:
            player = player1

        if cpu == player:
            text = self.text.format("You lose...", player, cpu)
            self.end()
            self.message(text)
            return

        elif cpu > 21 and player > 21:
            text = self.text.format("Tie!", player, cpu)
            self.end()
            self.message(text)
            return

        elif cpu > 21:
            text = self.text.format("You win!", player, cpu)
            self.end()
            self.message(text)
            return

        elif player > 21:
            text = self.text.format("You lose...", player, cpu)
            self.end()
            self.message(text)
            return

        elif player > cpu:
            text = self.text.format("You win!", player, cpu)
            self.end()
            self.message(text)
            return

        elif cpu > player:
            text = self.text.format("You lose...", player, cpu)
            self.end()
            self.message(text)
            return

    def end(self):
        del blackjack_dict[self.author, self.thread, self.thread_type]


@tags.tag('games')
def slots(self):
    """
    Play slots. Bank is work in progress.
    """

    keys = ['💰', '🆒', '💵', '💳', '💲', '💷']
    winner = Slots()
    check = ran.choice(winner.wins)
    if check is True:
        slot = ran.choice(keys)
        text = (
            "🎰🎰🎰🎰🎰🎰\n\n          Slots\n\n[ {1} ] [ {1} ] [ {1} ]"
            "\n\n      {0}\n\n🎰🎰🎰🎰🎰🎰"
        )
        self.message(text.format("You win!!", slot))

    if check is False:
        slot1 = ran.choice(keys)
        slot2 = ran.choice(keys)
        slot3 = ran.choice(keys)
        text = (
            "🎰🎰🎰🎰🎰🎰\n\n          Slots\n\n[ {1} ] [ {2} ] [ {3} ]"
            "\n\n      {0}\n\n🎰🎰🎰🎰🎰🎰"
        )
        self.message(text.format("You lose.", slot1, slot2, slot3))


class Slots():
    def __init__(self):
        self.wins = []
        self.make()

    def make(self):
        for i in range(0, 30):
            self.wins.append(True)

        for i in range(0, 70):
            self.wins.append(False)


blackjack_dict = {}
