from unittest import TestCase
from Card import *

class TestCard(TestCase):
    def setUp(self):
        self.card=Card(13,'Diamond')
    # check if the update of the card has done correctly
    def test__init__(self):
        # check if the value was updated
        self.assertEqual(self.card.value,13)
        # check if the suit was updated
        self.assertEqual(self.card.suit,'Diamond')

    # check if the update of the card has done incorrectly
    def test__init__invalid(self):
        # check if value isn't int
        with self.assertRaises(TypeError):
            card=Card('123','Club')
        # check if suit isn't string
        with self.assertRaises(TypeError):
            card = Card(1, [])
        # check if suit isn't Diamond,Club,spade or heart
        with self.assertRaises(TypeError):
            card = Card(1, 'something')
        # check if value can be over 13
        with self.assertRaises(TypeError):
            card = Card(14, 'Diamond')
        # check if value can be beneath 1
        with self.assertRaises(TypeError):
            card = Card(0, 'Diamond')
    # check if current card is bigger than the argument
    def test__gt__(self):
        # check if the function return True when the current card is bigger than the argument
        card=Card(2,'Diamond')
        self.assertTrue(self.card>card)
        # check if the function return False when the current card is smaller than the argument
        card = Card(2, 'Diamond')
        self.assertFalse(self.card < card)
    # check if the function return error when the argument isn't Card
    def test__gt__invalid(self):
        with self.assertRaises(TypeError):
            self.card.__gt__()
    # different cases of cards
    def test__gt__(self):
        # check if card with value 1 is bigger than card with value which isn't 1
        card1=Card(1,'Diamond')
        self.assertTrue(card1>self.card)
        # check if the function can distinguish between cards with the same value but different suits and knows the priority of the suits
        card2 = Card(1, 'Spade')
        self.assertTrue(card2 > card1)
        # check if the value of the argument is 1 is bigger than the current card with any value except of 1
        card2 = Card(1, 'Spade')
        self.assertFalse(self.card > card2)

    def test__eq__(self):
        # return True if the cards are equal
        card=Card(13,'Diamond')
        self.assertTrue(self.card==card)
        # return False if the cards aren't equal according to the value
        card = Card(12, 'Diamond')
        self.assertFalse(self.card == card)
        # return False if the cards aren't equal according to the suit
        card = Card(13, 'Spade')
        self.assertFalse(self.card == card)
        # check if the argument isn't Card
        with self.assertRaises(TypeError):
            self.card=='string'




