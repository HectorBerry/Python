# ROCK, PAPER, SCISSORS
from random import choice
GAME_CHOICES = ['rock', 'paper', 'scissors']
ROCK = 'rock'
PAPER = 'paper'
SCISSORS = 'scissors'
WIN_P1 = 'Player 1 wins'
WIN_P2 = 'Player 2 wins'


def game_choice(p1, p2):
    if not p1 or (not p2):
        print('One of the players didnt entered anything')
    elif p1 == ROCK and p2 == SCISSORS:
        print(WIN_P1)
    elif p1 == SCISSORS and p2 == PAPER:
        print(WIN_P1)
    elif p1 == PAPER and p2 == ROCK:
        print(WIN_P1)
    elif p1 == p2:
        print('Its a tie!')
    else:
        print(WIN_P2)
    return


def anti_cheating():
    x = 0
    while x < 150:
        print('****************CHEATER********************')
        x += 1


print('...rock...')
print('...paper...')
print('...scissors...')
number_of_players = input('How many players (1, 2): ')
if not number_of_players:
    print('Error')
elif int(number_of_players) == 1:
    print('Okay, you are playing with AI')
    player2 = choice(GAME_CHOICES)
    player1 = input('(enter Player 1\'s choice): ')
    game_choice(player1, player2)
    print(f'Player 2 picked: {player2}')
elif int(number_of_players) == 2:
    player1 = input('(enter Player 1\'s choice): ')
    anti_cheating()
    player2 = input('(enter Player 2\'s choice): ')
    game_choice(player1, player2)
else:
    print('There was an error, try again')

