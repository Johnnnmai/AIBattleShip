import random
from typing import List
from . import move
from BattleShip.src import move, ship, orientation, game_config, game,board
from.player import Player



class AIPlayer(Player):
    def __init__(self, player_num: int, config: game_config.GameConfig, other_players: List["Player"]) -> None:
        super().__init__(player_num, config, other_players)



    def init_name(self, player_num: int, other_players: List["Player"],player_type) -> None:
        other_players_names = [player.name for player in other_players]
        player_type = "Aiplayer"

        while True:
            self.name = player_type + " " + str((player_num))
            if self.name not in other_players_names:
                return self.name



    def add_opponent(self, opponent: "Player") -> None:
        super().add_opponent(opponent)

    def place_ships(self) -> None:
        super().place_ships()

    def place_ship(self, ship_: ship.Ship) -> None:
        super().place_ship(ship_)

    def get_ship_placement(self, ship_: ship.Ship):
        return super().get_ship_placement(ship_)

    def get_orientation(self, ship_: ship.Ship) -> orientation.Orientation:

        #Randomly select horizontal or vertical
        possible_orientation_ = ['horizontal', 'vertical']
        orientation_ = random.choice(possible_orientation_)

        return orientation.Orientation.from_string(orientation_)

    def get_start_coords(self, ship_: ship.Ship):
        #return super().get_start_coords(ship_)

        #self.num_rows
        #self.num_cols
        row = random.randint(0, self.board.num_rows)
        col = random.randint(0, self.board.num_cols)


        return row, col


    def all_ships_sunk(self) -> bool:
        return super().all_ships_sunk()

    def get_move(self, the_board: "board.Board") -> "Move":

        while True:
            row = random.randint(0, self.board.num_rows)
            col = random.randint(0, self.board.num_cols)
            print(row)
            print(col)
            coords =  str(col) + "," + str(row)
            print(coords)
            try:
                firing_location = move.Move.from_str(self, coords)
            except ValueError as e:
                print(e)
                continue
            return firing_location


    def fire_at(self, row: int, col: int) -> None:
        super().fire_at(row, col)

    def receive_fire_at(self, row: int, col: int) -> None:
        super().receive_fire_at(row, col)

    def __eq__(self, other: object) -> bool:
        return super().__eq__(other)

    def __ne__(self, other: object) -> bool:
        return super().__ne__(other)

    def display_placement_board(self) -> None:
        super().display_placement_board()

    def display_scanning_boards(self) -> None:
        super().display_scanning_boards()

    def display_firing_board(self) -> None:
        super().display_firing_board()

    def get_hidden_representation_of_board(self) -> str:
        return super().get_hidden_representation_of_board()

    def get_visible_representation_of_board(self) -> str:
        return super().get_visible_representation_of_board()

    def __str__(self) -> str:
        return super().__str__()