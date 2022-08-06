'''A game of tic_tak_toe with 2 players'''

from os import system
import tic_tak_toe as game


player_1 = game.player_1
player_2 = game.player_2

player_1.name = ('Player 1')
player_2.name = ('Player 2')

system ('cls')

print('Welcome to a game of Tic Tak Toe\n')
while True:
    game.player_marker()
    system ('cls')
    game.who_play_1st()

    while not game.check_for_win():
        game.display_game()

        if player_1.turn:
            player_1.turn, player_2.turn = player_1.place_marker()
        elif player_2.turn:
            player_2.turn, player_1.turn = player_2.place_marker()

        system ('cls')


    print(player_1, player_2, sep='\n')
    end_game = input('Do you want to stop playing?\n').lower()
    if end_game == 'yes':
        break

    board = ['0',
             ' ', ' ', ' ',
             ' ', ' ', ' ',
             ' ', ' ', ' '
             ]
    system('cls')
