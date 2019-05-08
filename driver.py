# Egyptian Ratscrew Driver
# Author: Teddy Ni
# May 2019

# Ruleset: We include sandwiches, but not double sandwiches

from deck import Deck
from player import Player

import time
import random
import numpy as np

VERBOSE = True
LIVE = False

def sp(player, text):
    if VERBOSE:
        print("Player " + str(player) + ": " + text)

def cw(delay):
    if LIVE:
        time.sleep(delay / 10)

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

    return play(players)

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
        # Check if we have a winner
        pLeft = 0
        aLeft = None
        for pIndex in range(0, len(players)):
            if players[pIndex].hasCards():
                pLeft = pLeft + 1
                aLeft = pIndex

        if pLeft == 1:
            # print("We have a winner: " + str(aLeft))
            return aLeft

        while not players[turn].hasCards():
            turn = (turn + 1) % len(players)

        # Simulate play speed vs slap speed
        slapCond = checkSlapConditions(pile)
        currPlayTime = players[turn].getPlayTime()
        if slapCond:
            #Get all the slap times for the players
            slapTimes = []
            for player in players:
                slapTimes.append(player.getSlapTime())

            slapTimes.append(currPlayTime)

            # Generate a random number between the slap times
            gen = np.random.uniform(0,np.sum(slapTimes))

            for i in range(0, len(slapTimes)):
                if gen < slapTimes[i]:
                    break

            if i < len(slapTimes) - 1:
                cw(slapTimes[i])
                sp(i, "Gets the slap! Wins the pile of " + str(len(pile)))

                players[turn].addCards(pile)
                # print("Player " + str(playerInitExtraDraw) + ": Wins the pile of " + str(len(pile)))
                pile = []
                playerInitExtraDraw = None
                extraDraw = 0
                continue

        cw(currPlayTime)
        card = players[turn].getNextCard()
        sp(turn, str(card))
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
                # print("Player " + str(playerInitExtraDraw) + ": Wins the pile of " + str(len(pile)))
                sp(playerInitExtraDraw, "Wins the pile of " + str(len(pile)))
                pile = []
                turn = playerInitExtraDraw
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

def checkSlapConditions(pile):
    if len(pile) <= 1:
        return False

    if pile[len(pile) - 1] == pile[len(pile) - 2]:
        return True

    if len(pile) > 2:
        if pile[len(pile)-1] == pile[len(pile) - 3]:
            return True

    return False

def runIterations(itr=1000):
    winnerScore = [0, 0, 0]
    for i in range(0, itr):
        print(i)
        PLAYERS = []

        PLAYER_ONE = Player()
        PLAYERS.append(PLAYER_ONE)

        PLAYER_TWO = Player()
        PLAYERS.append(PLAYER_TWO)

        PLAYER_THREE = Player()
        PLAYERS.append(PLAYER_THREE)

        winner = initGame(players=PLAYERS)
        winnerScore[int(winner)] = winnerScore[int(winner)] + 1

    print(winnerScore)


if __name__ == "__main__":
    # PLAYERS = []
    #
    # PLAYER_ONE = Player()
    # PLAYERS.append(PLAYER_ONE)
    #
    # PLAYER_TWO = Player()
    # PLAYERS.append(PLAYER_TWO)
    #
    # PLAYER_THREE = Player()
    # PLAYERS.append(PLAYER_THREE)
    #
    # initGame(players=PLAYERS)
    runIterations(itr=1)
