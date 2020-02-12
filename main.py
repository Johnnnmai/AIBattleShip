import sys
from Packages.configuration import Configuration
from Packages.game import BattleshipGame
#import os

if __name__ == '__main__':
    seed = None
    if len(sys.argv) < 2:
        filename = "config.txt"
    elif len(sys.argv) >= 3:
        seed = int(sys.argv[2])
    else:
        filename = sys.argv[1]
        #filename= "config.txt"
        #   print("Config file is ", filename)
        config = Configuration(filename)
        game = BattleshipGame(config.get_board_rows(), config.get_board_cols(), config.get_ship_list())
        game.play()




