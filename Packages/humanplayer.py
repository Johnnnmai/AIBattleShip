from typing import Iterable, List
from Packages.user_input import user_input, MoveError
from Packages.player import Player

class HumanPlayer(Player):
    def __init__(self, other_players: Iterable["HumanPlayer"], blank_character: str, player_number) -> None:
        super().__init__(other_players, blank_character, player_number)




    def get_name_from_player(self, other_players) -> str:
        already_used_names = set([player.name for player in other_players])
        while True:
            name = input(f'Player {self.player_number} please enter your name: ')
            if name not in already_used_names:
                return name
            else:
                print(f'Someone is already using {name} for their name.')
                print('Please choose another name.')

    def get_move(self, board) -> List[int]:
        while True:
            str_move = input(f'{self.name}, enter the location you want to fire at in the form row, column: ')
            try:
                move = user_input.from_str(str_move)
                return move
            except MoveError as moveError:
                print(moveError)

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



