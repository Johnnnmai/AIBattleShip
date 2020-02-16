import sys
from BattleShip.src import game
import BattleShip.configs
import unittest


if __name__ == '__main__':

    seed = None

    if len(sys.argv) < 2:

        print('Not enough arguments given.')
    elif len(sys.argv) >= 3:
        seed = int(sys.argv[2])
        game_of_battle_ship = game.Game(sys.argv[1], seed)
        game_of_battle_ship.play()

    else:

        game_of_battle_ship = game.Game(sys.argv[1], seed)
        game_of_battle_ship.play()
