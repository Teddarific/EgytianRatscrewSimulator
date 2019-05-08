import numpy as np


class Player:
    def __init__(self, sd=2, playSpeed=5, slapSpeed=5):
        self.cards = []
        #self.playSpeed = playSpeed
        self.sd = sd
        self.playSpeed = playSpeed
        self.slapSpeed = slapSpeed

        self.playSpeed = np.random.normal(playSpeed, sd)
        self.slapSpeed = np.random.normal(slapSpeed,sd)

    def getNextCard(self):
        if len(self.cards) == 0:
            return None

        return self.cards.pop(0)

    # Expects cards in list form
    def addCards(self, cards):
        self.cards = self.cards + cards

    def getPlayTime(self):
        return np.random.normal(self.playSpeed, self.sd)

    def getSlapTime(self):
        return np.random.normal(self.slapSpeed, self.sd)

    def hasCards(self):
        return len(self.cards) > 0
