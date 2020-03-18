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

# TEST
# Initial testing of Card object
assert(Card("A♠").suit == "♠")
assert(Card("K◆").suit == "◆")
assert(Card("7♥").suit == "♥")
assert(Card("3♣").suit == "♣")
assert(Card("10♣").suit == "♣")

assert(Card("2♠").index == 12)
assert(Card("8♥").index == 6)
assert(Card("J♥").index == 3)
assert(Card("K♣").index == 1)
assert(Card("A♥").index == 0)

assert(str(Card("3♠"))  == "3♠")
assert(str(Card("10♠")) == "10♠")
assert(str(Card("J♠"))  == "J♠")

# TEST Card Value
assert(Card("A♠").compareTo(Card("K♠")))
assert(Card("A♠").compareTo(Card("Q♠")))
assert(Card("A♠").compareTo(Card("3♠")))
assert(Card("J♠").compareTo(Card("8♥")))

assert(Card("A♠").compareTo(Card("A♥"))==0)
assert(Card("10♥").compareTo(Card("10♣"))==0)

assert(Card("K♥").compareTo(Card("A♥"))<0)
assert(Card("K♥").compareTo(Card("A♣"))<0)
assert(Card("Q♠").compareTo(Card("K♣"))<0)
assert(Card("8♠").compareTo(Card("J♣"))<0)
assert(Card("4♠").compareTo(Card("8♣"))<0)