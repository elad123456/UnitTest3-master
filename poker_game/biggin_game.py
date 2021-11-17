from players import *
from open_cards import *
from DeckOfCards import *
class Game:
    def __init__(self,deck:DeckOfCards):
        self.deck=deck
        self.players=Players(deck)
        self.open_cards=open_cards(deck)
        self.kupa=0
    def get_winner(self):
        max=self.players[0]
        for i in self.players:
            if i.money>max.money:
                max=self.players[i]
        return max.name
    def bet(self):
        print(self.open_cards.cards)
        max=self.players.players[0].money
        min=0
        for i in range(len(self.players.players)):
            bool=True
            while bool:
                print(f'{self.players.players[i].name} bet:')
                num = int(input("your bet is: "))
                self.players.players[i].bet=num
                if num==-1:
                    self.players.players.remove(self.players.players[i])
                    bool = False
                elif min<=num<=max:
                    bool=False
                min=num
    def get_winner_round(self):
        for player in self.players:
            win=player

