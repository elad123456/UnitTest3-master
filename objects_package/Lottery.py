from random import randint
class Loterry:
    def __init__(self,max_win=1000000):
        self.max_win=max_win
        self.numbers=[]
        while len(self.numbers)<6:
            num=randint(1,45)
            if num not in self.numbers:
                self.numbers.append(num)
    def __str__(self):
        return self.numbers
    def isexist(self,num):
        if num in self.numbers:
            return True
        else:
            return False
    def wining(self,guesses):
        if guesses<=1:
            return 0
        else:
            return self.max_win*guesses/6
lottery=Loterry(20000000)
#print(lottery.__str__())
guesses=0
list_guesses=[]
for i in range(6):
    num=int(input("guess a number between 1-45: "))
    if num<1 or num>45 or (num in list_guesses):
        print("your guess is invalied")
        break
    else:
        if lottery.isexist(num):
            guesses+=1
    list_guesses.append(num)
print(f"you reached {lottery.wining(guesses)} dolars")
print(guesses)