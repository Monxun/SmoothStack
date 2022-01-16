import random

player_a = 0
player_b = 0

def check_score(player_a, player_b):
    if player_a > player_b:
        print(f"player a is winning: {player_a}")
    elif player_b > player_a:
        print(f"player b is winning: {player_b}")
    else:
        print(f"It's a tie! A: {player_a}, B: {player_b}")


def turn(player_a, player_b):
    player_a += random.randrange(0, 100)
    print(player_a)

    player_b += random.randrange(0, 100)
    print(player_b)

    check_score(player_a, player_b)

turn(player_a, player_b)
turn(player_a, player_b)
turn(player_a, player_b)
turn(player_a, player_b)
