from unittest import TestCase
from DeckOfCards import *

class TestDeckOfCards(TestCase):
    def setUp(self):
        self.deckofcard=DeckOfCards()
    # check if the object deckofcard organized a neat deck
    def test_init(self):
        # check if the object deckofcard organized a neat deck
        self.assertEqual(self.deckofcard.cards[4].suit,'Diamond')
        self.assertEqual(self.deckofcard.cards[4].value, 2)
        # check if the object deckofcard organized a neat deck
        self.assertEqual(self.deckofcard.cards[5].suit, 'Spade')
        self.assertEqual(self.deckofcard.cards[5].value, 2)
        # check if the object deckofcard organized a neat deck
        self.assertEqual(self.deckofcard.cards[6].suit, 'Heart')
        self.assertEqual(self.deckofcard.cards[6].value, 2)
        # check if the object deckofcard organized a neat deck
        self.assertEqual(self.deckofcard.cards[7].suit, 'Club')
        self.assertEqual(self.deckofcard.cards[7].value, 2)
        # check if the deck define 52 cards
        self.assertEqual(len(self.deckofcard.cards),52)
    # check if the object defined list that include only cards
    def test_init_TypeCard(self):
        for i in self.deckofcard.cards:
            if type(i) != Card:
                self.fail()

    # create 2 decks, shuffle only one deck, and check if the order of the cards is not equal
    def test_cards_shuffle(self):
        counter=0
        deck=DeckOfCards()
        deck.cards_shuffle()
        for i in range(len(self.deckofcard.cards)):
            if self.deckofcard.cards[i]==deck.cards[i]:
                counter+=1
        self.assertNotEqual(counter,52)


    # check if the function return card
    def test_deal_one(self):
        self.assertEqual(type(self.deckofcard.deal_one()), Card)

    # check if the function remove one card from the DeckOfCard
    def test_deal_one_remove(self):
        card=self.deckofcard.deal_one()
        self.assertFalse(card in self.deckofcard.cards)

