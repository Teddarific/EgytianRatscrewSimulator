class Player:
    def __init__(self, cards):
        self.cards = cards

    def getNextCard(self):
        if len(self.cards) == 0:
            return None

        return self.cards.pop(0)

    # Expects cards in list form
    def addCards(self, cards):
        self.cards = self.cards + cards
