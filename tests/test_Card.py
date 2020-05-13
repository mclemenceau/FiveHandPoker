import unittest

from FiveHandPoker.Card import Card

class TestCard(unittest.TestCase):

    def setUp(self): 
        self.card_1 = Card("A♠")
        self.card_2 = Card("K◆")
        self.card_3 = Card("7♥")
        self.card_4 = Card("3♣")

    def tearDown(self):
            pass

    def test_suit(self):
        self.assertEqual(self.card_1.suit,"♠")
        self.assertEqual(self.card_2.suit,"◆")
        self.assertEqual(self.card_3.suit,"♥")
        self.assertEqual(self.card_4.suit,"♣")

        self.card_1.suit = "◆"
        self.card_2.suit = "♥"
        self.card_3.suit = "♣"
        self.card_4.suit = "♠"

        self.assertEqual(self.card_1.suit,"◆")
        self.assertEqual(self.card_2.suit,"♥")
        self.assertEqual(self.card_3.suit,"♣")        
        self.assertEqual(self.card_4.suit,"♠")     

    def test_index(self):
        self.assertEqual(self.card_1.index,0)
        self.assertEqual(self.card_2.index,1)
        self.assertEqual(self.card_3.index,7)
        self.assertEqual(self.card_4.index,11)

    def test_str(self):
        self.assertEqual(str(self.card_1),"A♠")
        self.assertEqual(str(self.card_2),"K◆")
        self.assertEqual(str(self.card_3),"7♥")
        self.assertEqual(str(self.card_4),"3♣")

    def test_compareTo(self):
        self.assertGreater(self.card_1.compareTo(self.card_2),0)
        self.assertGreater(self.card_2.compareTo(self.card_3),0)
        self.assertGreater(self.card_2.compareTo(self.card_4),0)
        self.assertGreater(self.card_3.compareTo(self.card_4),0)

        self.assertEqual(self.card_1.compareTo(Card("A♥")),0)
        self.assertEqual(self.card_2.compareTo(Card("K♣")),0)

        self.assertLess(self.card_2.compareTo(self.card_1),0)
        self.assertLess(self.card_3.compareTo(self.card_2),0)
        self.assertLess(self.card_4.compareTo(self.card_3),0)
        self.assertLess(self.card_4.compareTo(self.card_1),0)

if __name__ == '__main__':
    unittest.main()


