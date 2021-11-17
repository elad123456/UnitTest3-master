from Card import *
import random
class DeckOfCards:

    # the function define list of 52 different cards
    def __init__(self):
        '''the function define list of 52 different cards'''
        self.cards=[]
        for i in range(1,14):
            self.cards.append(Card(i,'Diamond'))
            self.cards.append(Card(i, 'Spade'))
            self.cards.append(Card(i, 'Heart'))
            self.cards.append(Card(i, 'Club'))

    # the function shuffle the cards in the list of DeckOfCards
    def cards_shuffle(self):
        '''the function shuffle the cards in the list of DeckOfCards '''
        random.shuffle(self.cards)

    # choose random card from the list and return it
    def deal_one(self):
        '''choose random card from the list and return it'''
        card=random.choice(self.cards)
        self.cards.remove(card)
        return card

    # return the list of the current Deck
    def __repr__(self):
        '''return the list of the current Deck'''
        return f"{self.cards}"
if __name__=='__main__':
    deck=DeckOfCards()
    print(deck)
    deck.cards_shuffle()
    print(deck)
    print(deck.deal_one())

    deck=DeckOfCards()
    #help(DeckOfCards)
    help(deck.deal_one)
