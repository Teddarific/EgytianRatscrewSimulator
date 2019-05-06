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
    noneCount = 0
    extraDraw = 0

    while True:
        # TODO: NEED TO CHECK IF THERE IS A WINNER HERE

        playSpeedSeed = players[turn].getPlaySpeed()
        nextCardTime = random.randint(MIN_TURN_TIME, MIN_TURN_TIME + playSpeedSeed)

        while not players[turn].hasCards():
            turn = (turn + 1) % len(players)

        card = players[turn].getNextCard()
        pile.append(card)

        # If player is on a face card, and needs to continue placing cards.
        # Do not iterate turn unless player puts down another face card
        if extraDraw > 0:
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

            extraDraw = extraDraw - 1
        # If player is not on a face card, iterate turn
        else:
            if card == "A":
                extraDraw = 4
            elif card == "J":
                extraDraw = 1
            elif card == "Q":
                extraDraw = 2
            elif card == "K":
                extraDraw = 3

            turn = (turn + 1) % len(players)

        lastCard = card

if __name__ == "__main__":
    PLAYERS = []

    PLAYER_ONE = Player()
    PLAYERS.append(PLAYER_ONE)

    PLAYER_TWO = Player()
    PLAYERS.append(PLAYER_TWO)

    PLAYER_THREE = Player()
    PLAYERS.append(PLAYER_THREE)

    initGame(players=PLAYERS)
