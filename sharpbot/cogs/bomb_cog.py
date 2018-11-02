import tags
import random as ran


@tags.tag('games')
def bomb(self):
    """
    Don't let the bomb go off!
    Do !bomb to continue the game, ", 
    """

    if bombC.plus is False:
        bombC.func = bombC()
        bombC.plus = True
        self.message(bombC.func.game())

    else:
        self.message(bombC.func.game())


class bombC():
    def __init__(self):
        self.score = 1
        self.total = ran.randint(1, 10)
        bombC.plus = False

    def game(self):
        self.score = self.score + 1
        if self.score > self.total:
            bombC.plus = False
            return("The bomb exploded! - You lose")

        else:
            return("Tick added to bomb")


bombC.plus = False
