"""
Game - Rock Paper Scissors
"""

import random


def rock_paper_scissors():
    player_one = random.randint(1, 3)
    player_two = random.randint(1, 3)

    print('ROCK PAPER SCISSORS SHOOT!')
    print()
    print(f'{player_name(player_one)} vs {player_name(player_two)}')

    if player_one == 1:
        if player_two == 1:
            player_draws(player_one, player_two)
        elif player_two == 2:
            player_loses(player_one, player_two)
        else:
            player_wins(player_one, player_two)
    elif player_one == 2:
        if player_two == 1:
            player_wins(player_one, player_two)
        elif player_two == 2:
            player_draws(player_one, player_two)
        else:
            player_loses(player_one, player_two)
    else:
        if player_two == 1:
            player_loses(player_one, player_two)
        elif player_two == 2:
            player_wins(player_one, player_two)
        else:
            player_draws(player_one, player_two)


def player_name(player_key_arg):
    if player_key_arg == 1:
        return 'ROCK'
    elif player_key_arg == 2:
        return 'PAPER'
    else:
        return 'SCISSORS'


def player_draws(player_one, player_two):
    print(f'{player_name(player_one)} DRAWS {player_name(player_two)}')


def player_loses(player_one, player_two):
    print(f'{player_name(player_one)} LOSES to {player_name(player_two)}')


def player_wins(player_one, player_two):
    print(f'{player_name(player_one)} BEATS {player_name(player_two)}')


rock_paper_scissors()
