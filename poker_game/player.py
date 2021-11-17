from DeckOfCards import *
import random
class player:

    # the function get the name of the player and his number of cards with default of 26 and check that the player won't get more than 26 card or less than 10
    def __init__(self,name,money,card_num=2):
        '''create a player with name and number of cards between 10-26'''
        if type(name)!=str or type(card_num)!=int:
            raise TypeError("name must be string and number of cards must be int")
        self.name=name
        self.money=money
        if card_num!=2:
            card_num=2
        self.card_num=card_num
        self.cards=[]
        self.bet=0

    def take_money(self,take):
        self.money-=take

    def add_money(self,add):
        self.money+=add

    def set_hand(self,deck:DeckOfCards):
        for i in range(2):
            self.cards.append(deck.deal_one())


