from DeckOfCards import *
import random
class Player:

    # the function get the name of the player and his number of cards with default of 26 and check that the player won't get more than 26 card or less than 10
    def __init__(self,name,card_num=26):
        '''create a player with name and number of cards between 10-26'''
        if type(name)!=str or type(card_num)!=int:
            raise TypeError("name must be string and number of cards must be int")
        self.name=name
        if card_num>26 or card_num<10:
            card_num=26
        self.card_num=card_num
        self.deckcards=[]

    # the function get deck of cards and give the number of cards as defined so and check that the player won't get the same card
    def set_hand(self,deck_of_cards:DeckOfCards):
        '''the function get deck and update the list card of the player'''
        if type(deck_of_cards)!=DeckOfCards:
            raise TypeError("the argument must be deckofcard")
        counter=0
        for i in range(self.card_num):
            card=deck_of_cards.deal_one()
            self.deckcards.append(card)

    # the function choose and return one random card from the player
    def get_card(self):
        '''the function return one card from the player's deck'''
        return random.choice(self.deckcards)

    # the function get card and insert it to the player's deck
    def add_card(self,card:Card):
        '''the function get card and insert it to the player's deck'''

        self.deckcards.append(card)

    # the function return the name of the player
    def __str__(self):
        '''the function return the name of the player'''
        return f"{self.name}"


if __name__=='__main__':
    player=Player('yonatan',26)
    deck=DeckOfCards()
    player.set_hand(deck)
    print(player)
    print(len(player.deckcards))
