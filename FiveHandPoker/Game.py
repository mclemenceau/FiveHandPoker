#!/usr/bin/python3

import sys
import random      

from FiveHandPoker.Card import Card,card_suits,card_strengths
from FiveHandPoker.Hand import Hand


class Game():

    def __init__(self):
        self.game_deck = []
        for suit in card_suits:
            for strenght in card_strengths:
                self.game_deck.append(strenght + suit)
        assert len(self.game_deck) == 52 , 'Not enough card in the deck'
        

    def shuffleUp(self):
        # Shuffle Up and Deal
        random.shuffle(self.game_deck)

    def play(self):
        print ("Five Hands Poker by bncmatt")

        self.shuffleUp()

        player1_hand = Hand(self.game_deck[0]+','+self.game_deck[2]+','+self.game_deck[4]+','+self.game_deck[8]+','+self.game_deck[10])
        print(str(player1_hand) + " => " + player1_hand.handTypeStr())

        player2_hand = Hand(self.game_deck[1]+','+self.game_deck[3]+','+self.game_deck[5]+','+self.game_deck[7]+','+self.game_deck[9])
        print(str(player2_hand) + " => " + player2_hand.handTypeStr())

        del self.game_deck[0:10]

