from card import *
from DeckOfCards import *
class open_cards:
    def __init__(self,deck:DeckOfCards):
        self.cards=[]
        for i in range(3):
            self.cards.append(deck.deal_one())
    def add_card(self,deck:DeckOfCards):
        self.cards.append(deck.deal_one())
