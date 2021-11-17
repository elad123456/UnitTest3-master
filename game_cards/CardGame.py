from Player import *
from DeckOfCards import *
from Card import *
class CardGame:
    # the function get name of two players, two amount of cards and create two players, deck of cards and call to new_game function
    def __init__(self,name1,num_cards1,name2,num_cards2):
        '''create two players and one deck of cards and call to new_game function'''
        self.deckofcards=DeckOfCards()
        self.player1=Player(name1,num_cards1)
        self.player2=Player(name2,num_cards2)
        self.new_game()
    # the function give cards to the first player and than to the second player and check that the second player dont get the same cards as the player1 has
    def new_game(self):
        '''the function update the card-lists of the players'''
        try:
            if __name__ != '__main__':
                # shuffle the deck of cards
                self.deckofcards.cards_shuffle()
                # give some cards to player1
                self.player1.set_hand(self.deckofcards)
                self.player2.set_hand((self.deckofcards))
        except:
            print("you cant call new_game from the main")


    # check which player has more cards and return this player, if they have the same number of cards return None
    def get_winner(self):
        '''return the player with the most cards and return None if they have the same amount of cards'''
        if len(self.player1.deckcards) > len(self.player2.deckcards):
            return self.player1
        if len(self.player1.deckcards) < len(self.player2.deckcards):
            return self.player2
        return None


if __name__=='__main__':
    game=CardGame('liav', 26, 'elad', 26)
    print(game.player1.deckcards)
    print(game.player2.deckcards)
