# Egyptian Ratscrew Driver
# Author: Teddy Ni
# May 2019

from deck import Deck
from player import Player

import random

def initGame(players):
    # Initialize the cards, and shuffle
    deck = Deck()
    deck.initDefaultDeck()
    deck.shuffleDeck()

    # Deal the cards
    hands = deck.dealCards(len(players))

    # Assign hands to the players
    for i in range(0, len(players)):
        players[i].addCards(hands[i])

    play(players)

def play(players):
    # Set constants
    MIN_TURN_TIME = 2

    # Set metadata
    turn = 0
    pile = []
    lastCard = None
    winner = None
    noneCount = 0
    extraDraw = 0

    while winner is not None:
        playSpeedSeed = players[turn].getPlaySpeed()
        nextCardTime = random.randint(MIN_TURN_TIME, MIN_TURN_TIME + playSpeedSeed)

        while not players[turn].hasCards():
            turn = (turn + 1) % len(players)

        if extraDraw > 0:
            card = players[turn].getNextCard()

            if card == "A":
                turn = (turn + 1) % len(players)
                extraDraw = 4
            elif card == "J":
                turn = (turn + 1) % len(players)
                extraDraw = 1
            elif card == "Q":
                turn = (turn + 1) % len(players)
                extraDraw = 2
            elif card == "K":
                turn = (turn + 1) % len(players)
                extraDraw = 3


        card = players[turn].getNextCard()

        # Check win condition, everyone is None except for one player
        if card is None:
            noneCount = noneCount + 1
            if noneCount == len(players) - 1:
                winner = (turn + 1) % len(players)
            continue

        noneCount = 0
        pile.append(card)




if __name__ == "__main__":
    PLAYERS = []

    PLAYER_ONE = Player()
    PLAYERS.append(PLAYER_ONE)

    PLAYER_TWO = Player()
    PLAYERS.append(PLAYER_TWO)

    PLAYER_THREE = Player()
    PLAYERS.append(PLAYER_THREE)

    initGame(players=PLAYERS)
