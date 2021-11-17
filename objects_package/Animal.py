from random import randint
class Animal:
    def __init__(self,kind:str,hunger=5,energy=5):
        self.kind=kind
        self.hunger=hunger
        self.energy=energy
    def __str__(self):
        print( self.kind,self.hunger,self.energy)
    def eat(self,gram):
        if self.hunger-(gram//50)>0:
            self.hunger=self.hunger-(gram//50)
        else:
            print(f"the {self.kind} is not hungry already")
            self.hunger = 0
        if self.energy-(gram//100)<0:
            self.energy=self.energy-(gram//100)
        else:
            self.energy=0
    def play(self,minutes):
        if minutes//10>self.energy:
            self.energy=0
            print(f"the game has been paused because the {self.kind} is tired")
        else:
            self.energy=self.energy-(minutes//10)
        self.hunger=self.hunger+(minutes//10)
    def rest(self,sleep):
        if self.energy+(sleep//20)>10:
            self.energy=10
            print(f"the {self.kind} want to play")
        else:
            self.energy=self.energy+(sleep//20)
        if self.hunger+(sleep//30)>10:
            self.hunger=10
            print(f"the {self.kind} want to eat")
        else:
            self.hunger=self.hunger+(sleep//30)




lion=Animal('lion')
command=input("take care of your pat, it need something: ")
while command!='stop':
    num=randint(100,300)
    print(num)
    if command=='eat':
        lion.eat(num)
    elif command=='rest':
        lion.rest(num)
    elif command=='play':
        lion.eat(num)
    lion.__str__()
    command=input("take care of your pat, it need something: ")
