from random import choice
def winner(option1,option2):
    options_of_winning = {'rock': 'seissors', 'seissors': 'paper', 'paper': 'rock'}
    if options_of_winning[option1] is option2:
        return 1
    if options_of_winning[option2] is option1:
        return 2


player1=input("enter the name of the first player: ")
player2=input("enter the name of the second player: ")
points1=0
points2=0
options = ['rock', 'seissors', 'paper']
while points1!=3 and points2!=3:
    option1=choice(options)
    option2=choice(options)
    print(f"{player1}:{option1}")
    print(f"{player2}:{option2}")

    if option1 != option2:
        winner_player = winner(option1, option2)
        if winner_player == 1:
            points1+=1
        elif winner_player == 2:
            points2 += 1
    print(f"{player1}:{points1},{player2}:{points2} \n")
if points1==3:
    print(f"the winner is {player1}")
if points2==3:
    print(f"the winner is {player2}")

