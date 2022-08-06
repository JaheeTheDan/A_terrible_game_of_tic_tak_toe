'''A game of tic_tak_toe but with an "AI"'''

from os import system
from random import choice, randint
from time import sleep
import tic_tak_toe as game

def player_marker():
    '''Ask player for a marker  they want to use'''
    if randint(1,2) == 1:
        print(f'{player_1.name} gets to pick marker 1st.')
        player_1.ask_marker()
        if player_1.marker == 'X':
            player_2.marker = 'O'
        else:
            player_2.marker = 'X'
    else:
        player_2.marker = choice(('O','X'))
        print(f'{player_2.name} gets to pick marker 1st.\nAnd its choice is {player_2.marker}')
        sleep(4)
        if player_2.marker == 'X':
            player_1.marker = 'O'
        else:
            player_1.marker = 'X'


player_1 = game.player_1
player_2 = game.player_2

player_1.name = ('Player 1')
player_2.name = ('Computer')

system ('cls')

print('Welcome to a game of Tic Tak Toe\n')
while True:
    player_marker()
    system ('cls')
    game.who_play_1st()

    while not game.check_for_win():

        if player_1.turn:
            game.display_game()
            player_1.turn, player_2.turn = player_1.place_marker()

        elif player_2.turn:
            placement = 0
            while game.board[placement] != ' ':
                placement = randint(1,9)
            game.board[placement] = player_2.marker

            game.display_game()
            print(f'{player_2.name} has pick a placement for it marker at {placement}')
            sleep(3)

            player_1.turn, player_2.turn = (True, False)
        
        system ('cls')

    print(player_1, player_2, sep='\n')
    end_game = input('Do you want to stop playing?\n').lower()
    if end_game == 'yes':
        break

    game.board = ['0',
             ' ', ' ', ' ',
             ' ', ' ', ' ',
             ' ', ' ', ' '
             ]
    system('cls')
