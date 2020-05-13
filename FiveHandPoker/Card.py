import sys

# a Card object is defined by 2 properties Strength and Suit but will also have a label and index
# For Example: A♠
#               name = A♠
#               strength = A
#               suit = ♠
#               index = 0 'This is the strength index compared to other card.'

card_strengths = ['A','K','Q','J','10','9','8','7','6','5','4','3','2']
card_suits = ['♠','♥','◆','♣']

class Card:
    'Standard deck card from 52 card deck'
    
    def __init__(self,card_name="A♠"):
        'Create a card from a string for ex: K♥'
        assert len(card_name) == 2 or len(card_name) == 3 , "Invalid Card " + card_name
        self.name = card_name
        self.strength = card_name[:-1]
        self.suit = card_name[-1:]
        assert self.strength in card_strengths and self.suit in card_suits , "Invalid Card " + card_name
        self.index = card_strengths.index(self.strength)

    def __str__(self):
            return self.name

    def __repr__(self):
            return "["+self.name+"]"
     
    def compareTo(self, vilain):
        'Compare Card Value to another Card '
        'return 0 if same value'
        'return -1 if smaller, 1 if bigger'
        if (self.index == vilain.index):
            return 0
        elif self.index < vilain.index :
                return 1
        else:
                return -1