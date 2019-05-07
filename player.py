import numpy as np


class Player:
    def __init__(self, playSpeed=5):
        self.cards = []
        #self.playSpeed = playSpeed

        # Normally distributed around playSpeed, standard deviation = 2
        sd = 2
        self.playSpeed = np.random.normal(playSpeed,sd)

    def getNextCard(self):
        if len(self.cards) == 0:
            return None

        return self.cards.pop(0)

    # Expects cards in list form
    def addCards(self, cards):
        self.cards = self.cards + cards

    def getPlaySpeed(self):
        return self.playSpeed

    def hasCards(self):
        return len(self.cards) > 0
