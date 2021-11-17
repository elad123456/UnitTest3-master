from CardGame import *
# input the names of the players
name1=input("enter the name of the first player:")
name2=input("enter the name of the second player:")
while name1==name2:
    print("the names must be different")
    name1 = input("enter the name of the first player:")
    name2 = input("enter the name of the second player:")
# create a game with two players and print their cards
game=CardGame(name1,26,name2,26)
print(f"{name1} your cards are: {game.player1.deckcards}")
print(f"{name2} your cards are: {game.player2.deckcards}")
# make ten rounds of war card game, print in each round the cards that where chosen and the winner of the round
for i in range(10):
    card1=game.player1.get_card()
    card2 = game.player2.get_card()
    print(f'{game.player1.name} ---- {card1}')
    print(f'{game.player2.name} ---- {card2}')
    if card1>card2:
        game.player2.deckcards.remove(card2)
        game.player1.add_card(card2)
        print(f"{game.player1.name} is the winner of the round")
    # check who win the round
    if card1<card2:
        game.player1.deckcards.remove(card1)
        game.player2.add_card(card1)
        print(f"{game.player2.name} is the winner of the round")
# call the get_winner function and print his name
print("the winner is:",game.get_winner())


