"""
In Nim, players take 1-3 stones from the table until one player takes the
final stones.

It is clear that if there are only one, two, or three stones in the pile, and it
is your turn, you can win the game by taking all of them. Like the problem
description says, if there are exactly four stones in the pile, you will lose.
Because no matter how many you take, you will leave some stones behind for your
opponent to take and win the game. So in order to win, you have to ensure that
you never reach the situation where there are exactly four stones on the pile on
your turn.
"""

def can_win_nim(num):
    """
    :type n: int
    :rtype: bool

    If the number of stones is divisible by 4 you cannot win because, in Nim,
    you can only remove 1, 2, or 3 stones from the table.
    """
    return num % 4 != 0

# MAIN

print(can_win_nim(3))
print(can_win_nim(4))
print(can_win_nim(9))
print(can_win_nim(16))
