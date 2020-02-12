from typing import List, Iterable
import random
from Packages.player import Player
from . import board
#from . import move

class AIPlayer(Player):
    def __init__(self, other_players: Iterable["Player"], blank_character: str, player_number) -> None:
        super().__init__(other_players, blank_character, player_number)

    def take_turn(self, the_board: "Board", the_board_hidden: "Board", opponent: "Player") -> None:
        super().take_turn(the_board, the_board_hidden, opponent)

    def get_name_from_player(self, other_players) -> str:
        possible_names = ["1", "2"]
        while True:
            name = random.choice(possible_names)
            return name

    def get_move(self, the_board: "board.Board") -> "move.Move":

        empty_coordinates = the_board.get_empty_coordinates()
        coord = random.choice(empty_coordinates)
        return move.Move(self, *coord)

    def get_empty_coordinates(self) -> List:
        empty_coords=[]

        for row in range(self.num_rows):
            for col in range(self.num_cols):
                if self[row][col] == self.blank_character:
                    empty_coords.append((row, col))

        return empty_coords

    def make_move(self, move: List[int], the_board: "board.Board", the_board_hidden: "board.Board") -> None:
        super().make_move(move, the_board, the_board_hidden)