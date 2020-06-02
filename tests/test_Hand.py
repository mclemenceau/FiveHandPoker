import unittest

from FiveHandPoker.Hand import Hand,hand_types

class TestHand(unittest.TestCase):

    def setUp(self): 
        # Incorrect
        self.hand_0 = Hand("8♥,8♥,6♥,A♥,2♥")

        # High Card Hand
        self.hand_10 = Hand("8♠,10♥,6♠,A♥,2♥")
        self.hand_11 = Hand("A♠,10♥,7♥,5♥,Q♣")
        self.hand_12 = Hand("J♥,9◆,2♣,3♣,10◆")
        self.hand_13 = Hand("A♥,10◆,5♣,7♣,Q◆")
        self.hand_14 = Hand("A♥,Q◆,5♣,7♣,K◆")

        # Pair Hand
        self.hand_20 = Hand("A♥,10♥,K♥,J♥,K♣")

        # Two Pairs Hands
        self.hand_30 = Hand("A♥,K♥,J◆,J♥,A◆")
        
        # 3 of a Kind Hands
        self.hand_40 = Hand("Q◆,J♣,Q♥,9♣,Q♣")

        # Straight
        self.hand_51 = Hand("Q♥,J♣,10♥,9♣,8♥")

        # Not Ordered Straight
        self.hand_52 = Hand("A♥,10♥,K♥,J♥,Q♥")
        self.hand_53 = Hand("A♣,5♥,3♥,2◆,4◆")

        # Flush Hand
        self.hand_60 = Hand("8♥,10♥,6♥,A♥,2♥")
        self.hand_61 = Hand("A♥,10♥,K♥,J♥,Q♥")

        # Full House
        self.hand_70 = Hand("Q◆,9♥,Q♥,9♣,Q♣")

        # Quad
        self.hand_80 = Hand("A♣,5♥,A♥,A◆,A♠")

        # Straight Flush
        self.hand_90 = Hand("K◆,J◆,Q◆,9◆,10◆")

        # Royal Flush
        self.hand_100 = Hand("A♥,10♥,K♥,J♥,Q♥")

        
    def tearDown(self):
        pass

    def test_isFlush(self):
        self.assertTrue(self.hand_60.isFlush())
        self.assertTrue(self.hand_61.isFlush())

        self.assertFalse(self.hand_0.isFlush())
        self.assertFalse(self.hand_40.isFlush())
        
    def test_isStraight(self):        
        self.assertTrue(self.hand_51.isStraight())
        self.assertTrue(self.hand_52.isStraight())
        self.assertTrue(self.hand_53.isStraight())
        
        self.assertTrue(self.hand_90.isStraight())
        self.assertTrue(self.hand_100.isStraight())

    def test_handType(self):
        self.assertEqual(self.hand_10.handType(),hand_types["High Card"])
        self.assertEqual(self.hand_20.handType(),hand_types["One Pair"])
        self.assertEqual(self.hand_10.handType(),hand_types["High Card"])
        self.assertEqual(self.hand_30.handType(),hand_types["Two Pairs"])
        self.assertEqual(self.hand_40.handType(),hand_types["Three of a Kind"])
        self.assertEqual(self.hand_51.handType(),hand_types["Straight"])
        self.assertEqual(self.hand_60.handType(),hand_types["Flush"])
        self.assertEqual(self.hand_70.handType(),hand_types["Full House"])
        self.assertEqual(self.hand_80.handType(),hand_types["Quads"])
        self.assertEqual(self.hand_90.handType(),hand_types["Straight Flush"])

    def test_against_highcard(self):
        self.assertEqual(self.hand_10.against(self.hand_11),"LOSE")
        self.assertEqual(self.hand_11.against(self.hand_12),"WIN")        
        self.assertEqual(self.hand_11.against(self.hand_13),"SPLIT")
        self.assertEqual(self.hand_11.against(self.hand_14),"LOSE")


if __name__ == '__main__':
    unittest.main()

