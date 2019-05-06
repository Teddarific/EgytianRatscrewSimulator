import random

class Deck:
    def initDefaultDeck(self):
        cards = []
        for i in range(2, 11):
            for j in range(0, 4):
                cards.append(str(i))

        for i in ["A", "J", "Q", "K"]:
            for j in range(0, 4):
                cards.append(i)

        self.cards = cards

    def shuffleDeck(self):
        # In-place shuffling algorithm
        for i in range(0, len(self.cards)):
            k = random.randint(i, len(self.cards) - 1)
            temp = self.cards[k]

            # Swap
            self.cards[k] = self.cards[i]
            self.cards[i] = temp

    def dealCards(self, numPlayers):
        hands = []
        for i in range(0, numPlayers):
            hands.append([])

        playerI = 0
        for i in range(0, len(self.cards)):
            hands[playerI].append(self.cards[i])
            playerI = (playerI + 1) % numPlayers

        return hands
