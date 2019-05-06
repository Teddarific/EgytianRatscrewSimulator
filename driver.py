# Egyptian Ratscrew Driver
# Author: Teddy Ni
# May 2019

from deck import Deck
from player import Player

def initGame(numPlayers = 4):
    deck = Deck()
    deck.initDefaultDeck()
    deck.shuffleDeck()
    hands = deck.dealCards(numPlayers)
    print(hands)



if __name__ == "__main__":
    NUM_PLAYERS = 4

    initGame(numPlayers=NUM_PLAYERS)
