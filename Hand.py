from Card import *

# A Hand is a group of 5 Cards (Card Object)
# a Hand could have higher value than another Hand
# a Hand can be any of the following type of hands (weaker to stronger)
#       High Card
#       Pair
#       Two Pairs
#       Three of a Kind
#       Straight
#       Flush
#       Full House
#       Quads
#       Straight Flush
#       Royal Flush
# 

hand_types = [  "Invalid",
                "High Card",
                "One Pair",
                "Two Pairs",
                "Three of a Kind",
                "Straight",
                "Flush",
                "Full House",
                "Quads",
                "Straight Flush",
                "Royal Flush"]

class Hand:

    
    def __init__(self, card1, card2, card3, card4, card5):
        'Initialise with 5 cards'
        self.cards = []
        self.proc_suits = {}
        self.proc_strengths = {}
        self.addCard(card1)
        self.addCard(card2)
        self.addCard(card3)
        self.addCard(card4)
        self.addCard(card5)

    def __processCard(self,card):
        'will update internal structures to help decide hand strength'
        if card.strength in self.proc_strengths:
            self.proc_strengths[card.strength] += 1
        else:
            self.proc_strengths[card.strength] = 1
        if card.suit in self.proc_suits:
            self.proc_suits[card.suit] += 1
        else:
            self.proc_suits[card.suit] = 1
        # When there's 5 Cards, sort them by index
        if len(self.cards) == 5:
            new_cards = sorted(self.cards, key=lambda card: card.index)
            self.cards = new_cards.copy()
            del new_cards        
    
    def isFlush(self):
        'Return true if the hand is a Flush'
        return len(self.proc_suits) == 1 and len(self.proc_strengths) == 5

    def isStraight(self):
        'Return true if the hand is a Straight'
        if len(self.proc_strengths) == 5:
            # If there's 4 index between two cards it is a straight
            if self.cards[4].index - self.cards[0].index == 4:    
                return True
            # special case with A, 2, 3, 4, 5
            elif self.cards[0].strength == 'A':
                if self.cards[4].index - self.cards[1].index == 3:    
                    return True
        return False
    
    def highCard(self):
        return self.cards[0]

    def addCard(self,card):
        'Add a Card to a hand'
        self.cards.append(card)
        self.__processCard(card)

    def handType(self):
        'This hand return the actual hand Type a hand represents'
        if len(self.cards) == 5:
            count = len(self.proc_strengths)
            #high card, straight, flush, straight flush or royal flush
            if count == 5:
                if self.isStraight():
                    if self.isFlush():
                        if self.highCard().strength == 'A':
                            return hand_types.index("Royal Flush")
                        else:
                            return hand_types.index("Straight Flush")
                    else:
                        return hand_types.index("Straight")
                elif self.isFlush():
                    return hand_types.index("Flush")
                else:
                    return hand_types.index("High Card")
            # One Pair
            elif count == 4:
                return hand_types.index("One Pair")
            elif count == 3:
                if 3 in self.proc_strengths.values():
                    return hand_types.index("Three of a Kind")
                else:
                    return hand_types.index("Two Pairs")
            elif count == 2:    
                if 3 in self.proc_strengths.values():
                    return hand_types.index("Full House")
                else:
                    return hand_types.index("Quads")
        return hand_types.index("Invalid Hand")
    
    # Compare two hands
    def against(self,other):
        hand_type = self.handType() 
        other_type = other.handType()
        if hand_type == other_type:
            # High Card will be compared one by one until a card is smaller
            if hand_type == hand_types.index("High Card"):
                for self_card,other_card in zip(self.cards,other.cards):
                    if self_card.index != other_card.index:
                        if self_card.index < other_card.index:
                            return "WIN"
                        else:
                            return "LOSE"
                # If all the cards are the same, it is a split
                return "SPLIT"
            # Check if pair is higher otherwise, check the remaining 3 cards one by one 
            elif hand_type == hand_types.index("One Pair"):
                self.debugPrint()
                other.debugPrint()
                return "LOSE"
            elif hand_type == hand_types.index("Two Pairs"):
                return "LOSE"
            elif hand_type == hand_types.index("Three of a Kind"):
                return "LOSE"
            elif hand_type == hand_types.index("Straight"):
                return "LOSE"
            elif hand_type == hand_types.index("Flush"):
                return "LOSE"
            elif hand_type == hand_types.index("Quads"):
                return "LOSE"
            elif hand_type == hand_types.index("Straight Flush"):
                return "LOSE"
            elif hand_type == hand_types.index("Royal Flush"):
                return "LOSE"
        else:
            if hand_type > other_type:
                return "WIN"
            else:
                return "LOSE"

    def __str__(self):
        return str(self.cards)

    def debugPrint(self):
        print(self.cards)
        print(self.proc_suits)
        print(self.proc_strengths)

# Testing
# ['♠','♥','◆','♣']

# Test isFlush
assert Hand(Card("8♥"),Card("10♥"),Card("6♥"),Card("A♥"),Card("2♥")).isFlush() , 'Hand is not a flush'
assert not Hand(Card("8♥"),Card("8♥"),Card("6♥"),Card("A♥"),Card("2♥")).isFlush() , 'Hand is a flush'
assert not Hand(Card("8♠"),Card("10♥"),Card("6♠"),Card("A♥"),Card("2♥")).isFlush() , 'Hand is a flush'
assert Hand(Card("A♥"),Card("10♥"),Card("K♥"),Card("J♥"),Card("Q♥")).isFlush() , 'Hand is a Flush'

# Test isStraight
# Ordered Straight
assert Hand(Card("A♥"),Card("K♥"),Card("Q♥"),Card("J♥"),Card("10♥")).isStraight() , 'Hand should be a Straight'
assert Hand(Card("Q♥"),Card("J♣"),Card("10♥"),Card("9♣"),Card("8♥")).isStraight() , 'Hand should be a Straight'

# Not Ordered Stragith
assert Hand(Card("A♥"),Card("10♥"),Card("K♥"),Card("J♥"),Card("Q♥")).isStraight() , 'Hand should be a Straight'
assert Hand(Card("A♣"),Card("5♥"),Card("3♥"),Card("2◆"),Card("4◆")).isStraight() , 'Hand should be a Straight'
assert Hand(Card("7♥"),Card("6♥"),Card("8♥"),Card("5♥"),Card("9♥")).isStraight() , 'Hand should be a Straight'
assert Hand(Card("K♣"),Card("J♥"),Card("Q♥"),Card("9◆"),Card("10◆")).isStraight() , 'Hand should be a Straight'
assert not Hand(Card("8♥"),Card("10♥"),Card("6♥"),Card("A♥"),Card("2♥")).isStraight() , 'Hand should not be a straight'

# Hand Type
assert hand_types[ Hand(Card("A♥"),Card("10♥"),Card("K♥"),Card("J♥"),Card("Q♥")).handType() ] == "Royal Flush", 'Should be Royal Flush'
assert hand_types[ Hand(Card("J♥"),Card("9◆"),Card("Q♥"),Card("K♣"),Card("10◆")).handType() ] == "Straight", 'Should be a Straight'
assert hand_types[ Hand(Card("8♥"),Card("10♥"),Card("6♥"),Card("A♥"),Card("2♥")).handType() ] == "Flush", 'Should be a Flush'
assert hand_types[ Hand(Card("8♥"),Card("5♥"),Card("6♥"),Card("A♥"),Card("2♥")).handType()  ] == "Flush" , 'Should be a Flush'
assert hand_types[ Hand(Card("8♠"),Card("10♥"),Card("6♠"),Card("A♥"),Card("2♥")).handType() ] == "High Card", 'Should be High Card'
assert hand_types[ Hand(Card("A♥"),Card("10♥"),Card("K♥"),Card("J♥"),Card("K♣")).handType() ] == "One Pair", 'Should be One Pair'
assert hand_types[ Hand(Card("A♥"),Card("K♥"),Card("J◆"),Card("J♥"),Card("A◆")).handType()  ] == "Two Pairs", 'Should be two Pairs'

assert hand_types[ Hand(Card("Q◆"),Card("J♣"),Card("Q♥"),Card("9♣"),Card("Q♣")).handType()  ] == "Three of a Kind", 'Hand should be a Three of a Kind'
assert hand_types[ Hand(Card("Q◆"),Card("9♥"),Card("Q♥"),Card("9♣"),Card("Q♣")).handType()  ] == "Full House", 'Hand should be a Full House'

assert hand_types[ Hand(Card("A♣"),Card("5♥"),Card("A♥"),Card("A◆"),Card("A♠")).handType()  ] == "Quads", 'Hand should be Quads'
assert hand_types[ Hand(Card("K◆"),Card("J◆"),Card("Q◆"),Card("9◆"),Card("10◆")).handType() ] == "Straight Flush" , 'Hand should be a Straight Flush'

# Comparison

# High Cards # ['♠','♥','◆','♣']
assert Hand(Card("A♠"),Card("10♥"),Card("7♥"),Card("5♥"),Card("Q♣")).against(Hand(Card("J♥"),Card("9◆"),Card("2♣"),Card("3♣"),Card("10◆"))) == "WIN"
assert Hand(Card("A♠"),Card("10♥"),Card("7♥"),Card("5♥"),Card("Q♣")).against(Hand(Card("A♥"),Card("10◆"),Card("5♣"),Card("7♣"),Card("Q◆"))) == "SPLIT"
assert Hand(Card("A♠"),Card("10♥"),Card("7♥"),Card("5♥"),Card("Q♣")).against(Hand(Card("A♥"),Card("Q◆"),Card("5♣"),Card("7♣"),Card("K◆"))) == "LOSE"

assert Hand(Card("8♥"),Card("10♥"),Card("6♥"),Card("2♥"),Card("2♣")).against(Hand(Card("8♣"),Card("A♥"),Card("6♥"),Card("A♥"),Card("2♥"))) == "WIN"
assert Hand(Card("8♠"),Card("10♥"),Card("6♠"),Card("A♥"),Card("2♥")) > Hand(Card("A♥"),Card("10♥"),Card("K♥"),Card("J♥"),Card("K♣"))
assert Hand(Card("A♥"),Card("K♥"),Card("J◆"),Card("J♥"),Card("A◆")) > Hand(Card("Q◆"),Card("J♣"),Card("Q♥"),Card("9♣"),Card("Q♣"))
assert Hand(Card("Q◆"),Card("9♥"),Card("Q♥"),Card("9♣"),Card("Q♣")) > Hand(Card("A♣"),Card("5♥"),Card("A♥"),Card("A◆"),Card("A♠"))

