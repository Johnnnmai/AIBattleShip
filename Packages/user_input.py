from typing import Iterable, List


class MoveError(Exception):
    def __init__(self, value):
        self.value = value

    def __str__(self):
        return (self.value)

class user_input:
    @staticmethod
    def get_move(self) -> "Move":
        str_move = input(f'{self} enter where you want to play in the form row, col: ')
        return Move.from_str(self, str_move)


    @staticmethod #this is used in the player class
    def get_name_from_player(name) -> str:
            message = input('Please enter your name: ')
            return message

    @staticmethod #this is used in the player class
    def from_str(str_move: str) -> List[int]:
        try:
            row, col = str_move.split(',')
        except ValueError:
            raise MoveError(f'{str_move} is not a valid location.\nEnter the firing location in the form row, column')

        try:
            row = int(row)
        except ValueError:
            raise MoveError(f'Row should be an integer. {row} is NOT an integer.')

        try:
            col = int(col)
        except ValueError:
            raise MoveError(f'Column should be an integer. {col} is NOT an integer.')

        return ([row, col])

    @staticmethod
    def input_integer(message: str, min_value : int, max_value : int) -> int:
        print(message)
        return(1);

    @staticmethod
    def input_float(message: str, min_value : float, max_value : float) -> float:
        print(message)
        return(1)

    @staticmethod
    def select_from_list(message: str, items : []) -> None:
        print(message)
        return(items[0])

    @staticmethod
    def input_string(message: str) -> str:
        print(message)
        return("test")

