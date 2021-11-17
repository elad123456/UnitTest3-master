from DeckOfCards import *
from player import *
class Players:
    def __init__(self,deck):
        self.players=[]
        counter=2
        money=int(input("enter how much money to share: "))
        self.money=money
        name=input("enter the name of player 1: ")
        while name!='stop':
            self.players.append(player(name,money,2))
            name = input(f"enter the name of player {counter} : ")
            counter+=1
        self.share(deck)
    def share(self,deck):
        for i in self.players:
            i.set_hand(deck)


