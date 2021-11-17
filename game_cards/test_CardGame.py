from unittest import TestCase
from CardGame import *

class TestCardGame(TestCase):
    def setUp(self):
        self.cardgame=CardGame('elad',26,'liav',26)

    # check if the init define the deckofcard and the two players
    def test_init(self):
        self.assertEqual(type(self.cardgame.deckofcards),DeckOfCards)
        self.assertEqual(type(self.cardgame.player1), Player)
        self.assertEqual(type(self.cardgame.player2), Player)

    # check if the init share cards to the players
    def test_init_share(self):
        # check if player1 get num of cards which define to him
        self.assertEqual(len(self.cardgame.player1.deckcards),self.cardgame.player1.card_num)
        # check if player2 get num of cards which define to him
        self.assertEqual(len(self.cardgame.player2.deckcards), self.cardgame.player2.card_num)

    # check if the init get invalid values
    def test_init_invalid(self):
        self.assertTrue(type(self.cardgame.player1.name), str)
        self.assertTrue(type(self.cardgame.player2.name), str)

    # check if call to new_game not from cardgame share cards to the players
    def test_new_game_NotFromCardGame(self):
        self.cardgame.player1.deckcards=[]
        self.cardgame.player2.deckcards = []
        self.cardgame.new_game()
        self.assertTrue(len(self.cardgame.player1.deckcards)==0)
        self.assertTrue(len(self.cardgame.player2.deckcards) == 0)
    # check if the function return the player with more cards
    def test_get_winner(self):
        game=CardGame('elad',26,'Liav',10)
        self.assertEqual(game.get_winner(),game.player1)
        game = CardGame('elad', 16, 'Liav', 17)
        self.assertEqual(game.get_winner(), game.player2)
        game = CardGame('elad', 26, 'Liav', 9)
        # check if the function return None when the amount of cards is equal
        self.assertEqual(game.get_winner(), None)
        game = CardGame('elad', 15, 'Liav', 15)
        self.assertEqual(game.get_winner(), None)
