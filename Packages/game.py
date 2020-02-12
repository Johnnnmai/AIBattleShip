from typing import Iterable, TypeVar, Optional
from Packages.board import Board
from Packages.humanplayer import HumanPlayer
from Packages.ai_player import AIPlayer
import random

T = TypeVar('T')


class BattleshipGame(object):
    def __init__(self, dimensions_x: int, seed: Optional[int], dimensions_y, ship_list: list, blank_char: str = '*') -> None:

        random.seed(seed)

        self.blank_char = blank_char
        self.ships_list = ship_list

        self.players = []

        player_type = self.pick_player_type()
        self.players.append(player_type(self.players, blank_char, 1))


        self.boards = []
        self.boards.append(Board(self.players[0], dimensions_x, dimensions_y, ship_list, blank_char))

        self.boards[0].placing_ships(ship_list)
        self.players.append(HumanPlayer(self.players, blank_char, 2))

        self.boards.append(Board(self.players[1], dimensions_x, dimensions_y, ship_list, blank_char))

        self.boards[1].placing_ships(ship_list)

        self.boards.append(Board(self.players[0], dimensions_x, dimensions_y, [], blank_char))
        self.boards.append(Board(self.players[1], dimensions_x, dimensions_y, [], blank_char))

        self._cur_player_turn = 0



    def play(self) -> None:
        while not self.is_game_over():
            self.display_game_state()
            opponent = (self._cur_player_turn + 1) % 2
            self.get_cur_player().take_turn(self.boards[opponent], self.boards[self._cur_player_turn + 2], self.get_cur_opponent())
            self.display_game_state()
            self.change_turn()
        self.display_the_winner()

    def pick_player_type(self):
        possible_player = {
            "human": HumanPlayer,
            "ai": AIPlayer

        }
        while True:
            picked_type = input(f'Pick One of the {list(possible_player)}for your type ').strip().lower()
            for name, type in possible_player.items():
                if name.startswith(picked_type):
                    return type
                else:
                    print(f"{picked_type} is not one of the {list(picked_type)}")


    def display_game_state(self) -> None:
        print(f"{self.get_cur_player()}'s Scanning Board")
        print(self.boards[((self._cur_player_turn)+2)], end="")
        print(f"{self.get_cur_player()}'s Board")
        print(self.boards[(self._cur_player_turn)], end="")

    def is_game_over(self) -> bool:
        if(self.boards[0].ship_hits_left() == 0):
            return True
        if(self.boards[1].ship_hits_left() == 0):
            return True

        return False

    def display_the_winner(self) -> None:
        if(self.boards[0].ship_hits_left() == 0):
            print(self.players[1].name + " won the game!")
        else:
            print(self.players[0].name + " won the game!")

    def someone_won(self) -> bool:
        return self.Ship.all_ships_sunk()

    @staticmethod
    def all_same(values: Iterable[T]) -> bool:
        iterator = iter(values)
        first_value = None
        try:
            first_value = next(iterator)
        except StopIteration:  # the iterable was empty
            return True  # so all elements are the same
        else:
            return all(
                (value == first_value for value in iterator)
            )

    def change_turn(self) -> None:
        self._cur_player_turn = (self._cur_player_turn + 1) % 2

    def get_cur_player(self) -> "HumanPlayer":
        return self.players[self._cur_player_turn]

    def get_cur_opponent(self) -> "HumanPlayer":
        return self.players[(self._cur_player_turn + 1) % 2]