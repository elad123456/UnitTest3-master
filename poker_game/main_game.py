from biggin_game import *
a=1
game=Game(DeckOfCards())
for i in game.players.players:
    print(f'{i.name} your cards are: {i.cards}')
print(f'the cards are: ')
game.bet()
game.open_cards.add_card()
game.bet()
game.open_cards.add_card()
game.bet()

