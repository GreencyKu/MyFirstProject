"""
File: DoubleBeepers.py
Name: Greency Ku
-------------------------------
TODO:
"""

from karel.stanfordkarel import *


def main():
    """
    Karel will double the beepers
    """
    move()
    double_beepers()
    put_back_beepers()
    go_home()


def double_beepers():
    while on_beeper():
        # old beepers, facing East
        pick_beeper()
        move()
        put_beeper()
        put_beeper()
        # new beepers, facing East
        turn_around()
        move()
        # old beepers, facing West
        turn_around()


def turn_around():
    turn_left()
    turn_left()


def put_back_beepers():
    move()
    while on_beeper():
        pick_beeper()
        turn_around()
        move()
        put_beeper()
        turn_around()
        move()


def go_home():
    turn_around()
    move()
    move()
    turn_around()


# ----- DO NOT MODIFY CODE BELOW THIS LINE ----- #
if __name__ == '__main__':
    execute_karel_task(main)
