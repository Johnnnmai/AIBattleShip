from typing import Iterable, List
from Packages.user_input import user_input, MoveError
import abc
from . import board


class Player(abc.ABC):
    def __init__(self, other_players: Iterable["Player"], blank_character: str, player_number) -> None:
        self.player_number = player_number
        self.name = self.get_name_from_player(other_players)
        self.blank_character = blank_character

    def __str__(self) -> str:
        return self.name

    def take_turn(self, the_board: "board.Board", the_board_hidden: "Board", opponent: "Player") -> None:
        self.opponent = opponent
        while True:
            try:
                move = self.get_move(the_board)
                self.make_move(move, the_board, the_board_hidden)
                return
            except MoveError as moveError:
                print(moveError)

    def get_name_from_player(self, other_players) -> str:

        ...

    def get_move(self, the_board: "board.Board") -> List[int]:
        ...

    def make_move(self, move: List[int], the_board: "board.Board", the_board_hidden: "board.Board") -> None:
        row = move[0]
        col = move[1]
        if not the_board.is_in_bounds(row, col):
            raise MoveError(f'{row}, {col} is not in bounds of our {the_board.num_rows} X {the_board.num_cols} board.')
        elif (the_board[row][col] == "X") or (the_board[row][col] == "O"):  # the_board.blank_char:
            raise MoveError(f"You have already fired at {row}, {col}.")
        elif the_board[row][col] == self.blank_character:
            the_board[row][col] = "O"
            the_board_hidden[row][col] = "O"
            print("Miss")
        else:
            the_board.ship_hit(the_board[row][col], self.opponent.name)
            the_board[row][col] = "X"
            the_board_hidden[row][col] = "X"



