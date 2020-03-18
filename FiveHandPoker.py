#!/usr/bin/python3

import sys
import random      

from Card import *
from Hand import *


# Gamea Rules
# one deck of 52 cards
# 4 suits Heart, Diamond, Clubs and Spade
# 13 cards per suit
# 2 players
# 5 players against 5 players
# 4 public and 1 private

# Deck is shuffled - Ok
# One player is the first dealer
# Each player is delt 5 cards (the private player)

# Game begin
# Person after the dealer picks up the first card of the deck
# Either position that card on any public deck or reject one card either the one that was just pulled or any from the private player)
#   Can only reject 2 cards
# Once the last card of the deck is pulled out there should be 5 players completed
# 4 private against 4 private and the 2 public ones
# Winner is the one with at least 3 winning players


# global variables
# Creating the deck and Shuffling the Deck


print ("Five Hands Poker by bncmatt")

#Create a deck of 52 cards
game_deck = []

for suit in card_suits:
    for strenght in card_strengths:
        game_deck.append(Card(strenght + suit))

# Shuffle Up and Deal
random.shuffle(game_deck)

assert len(game_deck) == 52 , 'Not enough card in the deck'
# Deal 5 cards to the 2 players

player1_hand = Hand(game_deck[0],game_deck[2],game_deck[4],game_deck[8],game_deck[10])
print(str(player1_hand) + " => " + hand_types[ player1_hand.handType() ] )

player2_hand = Hand(game_deck[1],game_deck[3],game_deck[5],game_deck[7],game_deck[9])
print(str(player2_hand) + " => " + hand_types[ player2_hand.handType() ] )

del game_deck[0:10]

