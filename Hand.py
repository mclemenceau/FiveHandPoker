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

hand_types = {  "Invalid":0,
                "High Card":1,
                "One Pair":2,
                "Two Pairs":3,
                "Three of a Kind":4,
                "Straight":5,
                "Flush":6,
                "Full House":7,
                "Quads":8,
                "Straight Flush":9,
                "Royal Flush":10}

class Hand:

    def __init__(self,cardstr,separator = ','):
        'Initialise with 5 cards'
        self.cards = []
        self.proc_suits = {}
        self.proc_strengths = {}
        self.setCards(cardstr,separator)

    def setCards(self,cardstr,separator = ','):
        'assign 5 cards at once to a hand in a String format [A'
        'A♥10♥K♥J♥Q♥'
        'A♥,10♥,K♥,J♥,Q♥'
        cards_list = cardstr.split(separator)
        # Reset existing cards
        self.cards.clear()
        for card in cards_list:
            self.addCard(Card(card))  

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
                            return hand_types["Royal Flush"]
                        else:
                            return hand_types["Straight Flush"]
                    else:
                        return hand_types["Straight"]
                elif self.isFlush():
                    return hand_types["Flush"]
                else:
                    return hand_types["High Card"]
            # One Pair
            elif count == 4:
                return hand_types["One Pair"]
            elif count == 3:
                if 3 in self.proc_strengths.values():
                    return hand_types["Three of a Kind"]
                else:
                    return hand_types["Two Pairs"]
            elif count == 2:    
                if 3 in self.proc_strengths.values():
                    return hand_types["Full House"]
                else:
                    return hand_types["Quads"]
        return hand_types["Invalid Hand"]

    def handTypeStr(self):
        num = self.handType()
        for key in hand_types.keys():
            if hand_types[key] == num:
                return key
        return "Invalid"
        
    # Compare two hands
    def against(self,other):
        hand_type = self.handType() 
        other_type = other.handType()
        if hand_type == other_type:
            # High Card will be compared one by one until a card is smaller
            if hand_type == hand_types["High Card"]:
                for self_card,other_card in zip(self.cards,other.cards):
                    if self_card.index != other_card.index:
                        if self_card.index < other_card.index:
                            return "WIN"
                        else:
                            return "LOSE"
                # If all the cards are the same, it is a split
                return "SPLIT"
            # Check if pair is higher otherwise, check the remaining 3 cards one by one 
            elif hand_type == hand_types["One Pair"]:
                self.debugPrint()
                other.debugPrint()
                return "LOSE"
            elif hand_type == hand_types["Two Pairs"]:
                return "LOSE"
            elif hand_type == hand_types["Three of a Kind"]:
                return "LOSE"
            elif hand_type == hand_types["Straight"]:
                return "LOSE"
            elif hand_type == hand_types["Flush"]:
                return "LOSE"
            elif hand_type == hand_types["Quads"]:
                return "LOSE"
            elif hand_type == hand_types["Straight Flush"]:
                return "LOSE"
            elif hand_type == hand_types["Royal Flush"]:
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
assert Hand("8♥,10♥,6♥,A♥,2♥").isFlush() , 'Hand is not a flush'

assert not Hand("8♥,8♥,6♥,A♥,2♥").isFlush() , 'Hand is a flush'
assert not Hand("8♠,10♥,6♠,A♥,2♥").isFlush() , 'Hand is a flush'
assert Hand("A♥,10♥,K♥,J♥,Q♥").isFlush() , 'Hand is a Flush'

# Test isStraight
# Ordered Straight
assert Hand("A♥,K♥,Q♥,J♥,10♥").isStraight() , 'Hand should be a Straight'
assert Hand("Q♥,J♣,10♥,9♣,8♥").isStraight() , 'Hand should be a Straight'

# Not Ordered Stragith
assert Hand("A♥,10♥,K♥,J♥,Q♥").isStraight() , 'Hand should be a Straight'
assert Hand("A♣,5♥,3♥,2◆,4◆").isStraight() , 'Hand should be a Straight'
assert Hand("7♥,6♥,8♥,5♥,9♥").isStraight() , 'Hand should be a Straight'
assert Hand("K♣,J♥,Q♥,9◆,10◆").isStraight() , 'Hand should be a Straight'
assert not Hand("8♥,10♥,6♥,A♥,2♥").isStraight() , 'Hand should not be a straight'

# Hand Type
assert Hand("A♥,10♥,K♥,J♥,Q♥").handType() == hand_types["Royal Flush"], 'Should be Royal Flush'
assert Hand("J♥,9◆,Q♥,K♣,10◆").handType() == hand_types["Straight"], 'Should be a Straight'
assert Hand("8♥,10♥,6♥,A♥,2♥").handType() == hand_types["Flush"], 'Should be a Flush'
assert Hand("8♥,5♥,6♥,A♥,2♥").handType()  == hand_types["Flush"] , 'Should be a Flush'
assert Hand("8♠,10♥,6♠,A♥,2♥").handType() == hand_types["High Card"], 'Should be High Card'
assert Hand("A♥,10♥,K♥,J♥,K♣").handType() == hand_types["One Pair"], 'Should be One Pair'
assert Hand("A♥,K♥,J◆,J♥,A◆").handType()  == hand_types["Two Pairs"], 'Should be two Pairs'

assert Hand("Q◆,J♣,Q♥,9♣,Q♣").handType()  == hand_types["Three of a Kind"], 'Hand should be a Three of a Kind'
assert Hand("Q◆,9♥,Q♥,9♣,Q♣").handType()  == hand_types["Full House"], 'Hand should be a Full House'

assert Hand("A♣,5♥,A♥,A◆,A♠").handType()  == hand_types["Quads"], 'Hand should be Quads'
assert Hand("K◆,J◆,Q◆,9◆,10◆").handType() == hand_types["Straight Flush"] , 'Hand should be a Straight Flush'

# Comparison

# High Cards # ['♠','♥','◆','♣']
assert Hand("A♠,10♥,7♥,5♥,Q♣").against(Hand("J♥,9◆,2♣,3♣,10◆")) == "WIN"
assert Hand("A♠,10♥,7♥,5♥,Q♣").against(Hand("A♥,10◆,5♣,7♣,Q◆")) == "SPLIT"
assert Hand("A♠,10♥,7♥,5♥,Q♣").against(Hand("A♥,Q◆,5♣,7♣,K◆")) == "LOSE"

# assert Hand("8♥,10♥,6♥,2♥,2♣").against(Hand("8♣,A♥,6♥,A♥,2♥")) == "WIN"
# assert Hand("8♠,10♥,6♠,A♥,2♥").against(Hand("A♥,10♥,K♥,J♥,K♣")
# assert Hand("A♥,K♥,J◆,J♥,A◆") > Hand("Q◆,J♣,Q♥,9♣,Q♣")
# assert Hand("Q◆,9♥,Q♥,9♣,Q♣") > Hand("A♣,5♥,A♥,A◆,A♠")

