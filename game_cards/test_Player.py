from unittest import TestCase, mock
from unittest.mock import patch
from Player import *
from DeckOfCards import *

class TestPlayer(TestCase):
    def setUp(self):
        self.player=Player('aviad',14)

    # check if the object create player with the right details and create an empty list
    def test_init(self):
        self.assertEqual(self.player.card_num, 14)
        self.assertEqual(self.player.name, 'aviad')
        self.assertEqual(type(self.player.deckcards), list)


    def test_invalid_init(self):
        # check if the function fail when the player get num of cards that isn't int
        with self.assertRaises(TypeError):
            p1 = Player('rami', 'string')
        # check if the function fail when the player get name that isn't str
        with self.assertRaises(TypeError):
            p2 = Player(123, 23)

    # check if the default of number of cards is 26
    def test_default_init(self):
        # check if the object get a default of 26 when the number of card smaller than 10
        p=Player('STRING',9)
        self.assertEqual(p.card_num,26)
        # check if the object get a default of 26 when the number of card bigger than 26
        p = Player('STRING', 27)
        self.assertEqual(p.card_num, 26)
        # check if the object get a default of 26 when the object get only name by defined
        p = Player('erik')
        self.assertEqual(p.card_num, 26)

    # check if the function update the player's deck
    def test_set_hand(self):
        self.player.card_num=1
        with patch('DeckOfCards.DeckOfCards.deal_one') as mock_do:
            mock_do.return_value=Card(5,'Spade')
            self.player.set_hand(DeckOfCards())
            card=Card(5,'Spade')
            self.assertTrue(card in self.player.deckcards)

    # check if the function update the player's deck when it get deckofcards by different cards
    def test_set_hand2(self):
        # check if the player get the exactly amount that he supposed to get
        self.player.set_hand(DeckOfCards())
        self.assertEqual(len(self.player.deckcards),self.player.card_num)
        # check if the player got different cards
        for i in range(len(self.player.deckcards)):
            if self.player.deckcards[i] in self.player.deckcards[i+1:]:
                self.fail()

    # check if the function return error if it get argument which isn't deckofcard
    def test_invalid_set_hand(self):
        with self.assertRaises(TypeError):
            self.player.set_hand('string')

    # create a deck, give to player the amount of cards to the game and
    # get one card from the player's deck
    def test_get_card(self):
        self.player.set_hand(DeckOfCards())
        card = self.player.get_card()
        # check if the function return Card object
        self.assertTrue(type(card) == Card)
        # check if the card in the player's deck
        self.assertIn(card, self.player.deckcards)

    def test_add_card(self):
        # create deck and player and give the player 10 cards.
        # add card to the player's deck and check if now the player has 11 cards
        # add card not check duplicates because it part only of CardGame and add cards of your opponent
        # the function set_hand make sure there is no duplicated
        d = DeckOfCards()
        p1 = Player('ram', 10)
        p1.set_hand(d)
        p1.add_card(d.deal_one())
        self.assertEqual(len(p1.deckcards), 11)

