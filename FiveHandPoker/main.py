#!/usr/bin/python3

import sys
import random      

from Card import *
from Hand import *


print ("Five Hands Poker by bncmatt")

#Create a deck of 52 cards
game_deck = []

for suit in card_suits:
    for strenght in card_strengths:
        game_deck.append(strenght + suit)

# Shuffle Up and Deal
random.shuffle(game_deck)

assert len(game_deck) == 52 , 'Not enough card in the deck'
# Deal 5 cards to the 2 players

player1_hand = Hand(game_deck[0]+','+game_deck[2]+','+game_deck[4]+','+game_deck[8]+','+game_deck[10])
print(str(player1_hand) + " => " + player1_hand.handTypeStr())

player2_hand = Hand(game_deck[1]+','+game_deck[3]+','+game_deck[5]+','+game_deck[7]+','+game_deck[9])
print(str(player2_hand) + " => " + player2_hand.handTypeStr())

del game_deck[0:10]

