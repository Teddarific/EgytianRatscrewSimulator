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
    extraDraw = 0
    playerInitExtraDraw = None

    while True:
        pLeft = 0
        aLeft = None
        for pIndex in range(0, len(players)):
            if players[pIndex].hasCards():
                pLeft = pLeft + 1
                aLeft = pIndex

        if pLeft == 1:
            print("We have a winner: " + str(aLeft))
            break

        playSpeedSeed = players[turn].getPlaySpeed()
        nextCardTime = random.randint(MIN_TURN_TIME, MIN_TURN_TIME + playSpeedSeed)

        while not players[turn].hasCards():
            turn = (turn + 1) % len(players)

        card = players[turn].getNextCard()
        print("Player " + str(turn) + ": " + str(card))
        pile.append(card)

        # If player is on a face card, and needs to continue placing cards.
        # Do not iterate turn unless player puts down another face card
        if extraDraw > 0:
            if card == "A":
                playerInitExtraDraw = turn
                turn = (turn + 1) % len(players)
                extraDraw = 4
            elif card == "J":
                playerInitExtraDraw = turn
                turn = (turn + 1) % len(players)
                extraDraw = 1
            elif card == "Q":
                playerInitExtraDraw = turn
                turn = (turn + 1) % len(players)
                extraDraw = 2
            elif card == "K":
                playerInitExtraDraw = turn
                turn = (turn + 1) % len(players)
                extraDraw = 3
            else:
                extraDraw = extraDraw - 1

            if extraDraw == 0:
                players[playerInitExtraDraw].addCards(pile)
                print("Player " + str(playerInitExtraDraw) + ": Wins the pile of " + str(len(pile)))
                pile = []
                playerInitExtraDraw = None
        # If player is not on a face card, iterate turn
        else:
            if card == "A":
                playerInitExtraDraw = turn
                extraDraw = 4
            elif card == "J":
                playerInitExtraDraw = turn
                extraDraw = 1
            elif card == "Q":
                playerInitExtraDraw = turn
                extraDraw = 2
            elif card == "K":
                playerInitExtraDraw = turn
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
