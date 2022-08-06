'''simple tictaktoe game'''

from random import randint


board = ['0',
         ' ', ' ', ' ',
         ' ', ' ', ' ',
         ' ', ' ', ' '
         ]


class Player():
    '''A class representing a player'''

    def __init__(self, name = '', marker='', score=0, turn=False):
        self.name = name
        self.marker = marker
        self.turn = turn
        self.score = score

    def ask_marker(self):
        '''Ask what marker the player wants'''
        self.marker = input(
            f'{self.name}, what marker do want to use? (X or O)\n').upper()

        while self.marker not in ('X', 'O'):
            print('You must specify a marker to use\nTry again')
            self.marker = input(
            f'{self.name}, what marker do want to use? (X or O)\n').upper()

    def marker_placement(self):
        '''Ask where the player want to place their marker'''
        while True:
            try:
                marker_placement = int(
                    input('Where do you want to place your marker?\n'))
                if board[marker_placement] != ' ':
                    print('Area not available')
                else:
                    return marker_placement
            except (ValueError, IndexError):
                print('Invalid Placement!!\nTry again.')

    def place_marker(self):
        '''Place marker at position'''
        print(f'It {self.name} turn')
        board[self.marker_placement()] = self.marker
        return False, True

    def __str__(self):
        '''Display the player's score'''
        return f'{self.name} score: {self.score}'


def player_marker():
    '''Ask player for a marker they want to use and give the available one to the next player'''
    if randint(1, 2) == 1:
        print(f'{player_1.name} gets to pick marker 1st.')
        player_1.ask_marker()
        if player_1.marker == 'X':
            player_2.marker = 'O'
        else:
            player_2.marker = 'X'
    else:
        print(f'{player_2.name} gets to pick marker 1st.')
        player_2.ask_marker()
        if player_2.marker == 'X':
            player_1.marker = 'O'
        else:
            player_1.marker = 'X'


def check_for_win():
    '''Check if a player has won or the game in a tie'''

    def display():
        print(board[1], '|', board[2], '|', board[3])
        print('--+---+---')
        print(board[4], '|', board[5], '|', board[6])
        print('--+---+---')
        print(board[7], '|', board[8], '|', board[9])
        print()

    def win(player):

        marker = player.marker
        if board[1] == marker and board[2] == marker and board[3] == marker:
            return True
        if board[4] == marker and board[5] == marker and board[6] == marker:
            return True
        if board[7] == marker and board[8] == marker and board[9] == marker:
            return True
        if board[1] == marker and board[4] == marker and board[7] == marker:
            return True
        if board[2] == marker and board[5] == marker and board[8] == marker:
            return True
        if board[3] == marker and board[6] == marker and board[9] == marker:
            return True
        if board[1] == marker and board[5] == marker and board[9] == marker:
            return True
        if board[3] == marker and board[5] == marker and board[7] == marker:
            return True

        return False
    if win(player_1):
        display()
        print(f'{player_1.name} has won')
        player_1.score += 1
        return True
    if win(player_2):
        display()
        print(f'{player_2.name} has won')
        player_2.score += 1
        return True

    count = 0
    for i in board:
        if i in ('X', 'O'):
            count += 1
    if count == 9:
        display()
        print('Game ended in a tie')
        return True
    return False


def display_game():
    '''display the board'''
    print(board[1], '|', board[2], '|', board[3])
    print('--+---+---')
    print(board[4], '|', board[5], '|', board[6])
    print('--+---+---')
    print(board[7], '|', board[8], '|', board[9])

    print('\n\n')
    print('for reference')
    print('1', '|', '2', '|', '3')
    print('--+---+---')
    print('4', '|', '5', '|', '6')
    print('--+---+---')
    print('7', '|', '8', '|', '9')
    print('\n')


def who_play_1st():
    '''determine who play 1st'''
    if randint(1, 2) == 1:
        player_1.turn = True
        print(f'{player_1.name} plays 1st')
    else:
        player_2.turn = True
        print(f'{player_2.name} plays 1st')


player_1 = Player()
player_2 = Player()

# system ('cls')

# print('Welcome to a game of Tic Tak Toe\n')
# while True:
#     player_marker()
#     system ('cls')
#     who_play_1st()

#     while not check_for_win():
#         display_game()

#         if player_1.turn:
#             player_1.turn, player_2.turn = player_1.place_marker()
#         elif player_2.turn:
#             player_2.turn, player_1.turn = player_2.place_marker()

#         system ('cls')


#     print(player_1, player_2, sep='\n')
#     end_game = input('Do you want to stop playing?\n').lower()
#     if end_game == 'yes':
#         break

#     board = ['0',
#              ' ', ' ', ' ',
#              ' ', ' ', ' ',
#              ' ', ' ', ' '
#              ]
#     system('cls')
