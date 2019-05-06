class Player:
    def __init__(self, playSpeed=5):
        self.cards = []
        self.playSpeed = playSpeed

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
