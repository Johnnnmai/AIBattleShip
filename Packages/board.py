from typing import Iterator, List, Union
from Packages.humanplayer import HumanPlayer
from Packages.user_input import user_input, MoveError


class Board(object):
    def __init__(self, player: HumanPlayer, num_rows: int, num_cols: int, player_ships: list, blank_char: str = "*") -> None:
        self.player_ships = player_ships
        self.contents = [[blank_char for col in range(num_cols)] for row in range(num_rows)]
        self.player = player
        self.blank_char = blank_char
        self.num_ship_hits = []

    def placing_ships(self, player_ships_list: list) -> None:
        print(self.player.name + "'s Placement Board")
        print(self, end="")
        for name, length in player_ships_list:
            length = int(length)
            self.num_ship_hits.append(length)
            self.place_ship(name, length)
            print(self.player.name + "'s Placement Board")
            print(self, end="")

    def ship_hits_left(self) -> int:
        total_hits_left = sum(self.num_ship_hits)
        return(total_hits_left)

    def input_placement_location(self,name,length) -> Union[int,int]:
           place_spot = input(f'{self.player.name}, enter the starting position for your {name} ship ,which is {length} long, in the form row, column: ')  # not sure why this doesn't work,

           try:
                ship_loc = self.from_str(place_spot)
                row = ship_loc[0]
                col = ship_loc[1]
                return row, col
           except MoveError as moveError:
                print(moveError)
                raise ValueError

    def from_str(self, str_move: str) -> List[int]:
        try:
            row, col = str_move.split(',')
        except ValueError:
            raise MoveError(f'{str_move} is not in the form x,y')

        try:
            row = int(row)
        except ValueError:
            raise MoveError(f'{row} is not a valid value for row.\nIt should be an integer between 0 and {self.num_rows-1}')

        try:
            col = int(col)
        except ValueError:
            raise MoveError(f'{col} is not a valid value for column.\nIt should be an integer between 0 and {self.num_cols-1}')

        return ([row, col])

    def ship_name_to_letter(self, ship_name: str) -> str:
        letter = ship_name[0]
        return letter

    def place_ship(self, name, length):
        while True:
            ship_posit = input(f'{self.player.name} enter horizontal or vertical for the orientation of {name} which is {length} long: ')  # any order of letters should work
            if "horizontal".startswith(ship_posit.lower().rstrip()):
                result = self.place_horizontally(name, length)  # will work for all prefixes but not all letters (if you
                if result:
                    return
            elif "vertical".startswith(ship_posit.lower().rstrip()):
                result = self.place_vertically(name, length)
                if result:
                    return
            else:
                print(f'{ship_posit} does not represent an Orientation')


    def place_horizontally(self, ship_name: str, ship_length: int) -> bool:
        try:
           row, col = self.input_placement_location(ship_name,ship_length)
        except:
           return False
        letter = self.ship_name_to_letter(ship_name)
        if(row < 0) or (col < 0) or (row > ((self.num_rows)-1)) or (col > ((self.num_cols)-1)):
            print(f'Cannot place {ship_name} horizontally at {row}, {col} because it would be out of bounds.')
            return False
        if(col > ((self.num_cols)-ship_length)):
            print(f'Cannot place {ship_name} horizontally at {row}, {col} because it would end up out of bounds.')
            return False
        for i in range(ship_length):
            ship_letter = self.contents[row][col + i]
            if (ship_letter != self.blank_char):
                print(f'Cannot place {ship_name} horizontally at {row}, {col} because it would overlap with ' + "['" + ship_letter + "']")
                return False
        for i in range(ship_length):
            self.contents[row][col + i] = letter
        return True

    def place_vertically(self, ship_name: str, ship_length: int) -> bool:
        try:
           row, col = self.input_placement_location(ship_name,ship_length)
        except:
           return False
        letter = self.ship_name_to_letter(ship_name)
        if(row < 0) or (col < 0) or (row > ((self.num_rows)-1)) or (col > ((self.num_cols)-1)):
            print(f'Cannot place {ship_name} vertically at {row}, {col} because it would be out of bounds.')
            return False
        if(row > ((self.num_rows)-ship_length)):
            print(f'Cannot place {ship_name} vertically at {row}, {col} because it would end up out of bounds.')
            return False
        for i in range(ship_length):
            ship_letter = self.contents[row + i][col]
            if (ship_letter != self.blank_char):
                print(f'Cannot place {ship_name} vertically at {row}, {col} because it would overlap with ' + "['" + ship_letter + "']")
                return False
        for i in range(ship_length):
            self.contents[row + i][col] = letter
        return True

    def ship_hit(self, first_char: str, opponent_name: str) -> None:
        index = 0
        for name, length in self.player_ships:
            if (first_char == name[0]):
                print("You hit", opponent_name + "'s " + name + "!")
                self.num_ship_hits[index] -= 1;
                if (self.num_ship_hits[index] == 0):
                    print("You destroyed", opponent_name + "'s " + name)
            index += 1
        return

    def player1_ship_placing(self):
        Board.placing_ships(self.player1_ships)
        return

    def player2_ship_placing(self):
        Board.placing_ships(self.player2_ships)
        return

    @property
    def num_rows(self) -> int:
        return len(self.contents)

    @property
    def num_cols(self) -> int:
        return len(self[0])

    def __str__(self) -> str:
        sep = ' ' * max([len(str(self.num_rows)), len(str(self.num_cols))])
        rep = 2*sep + sep.join((str(i) for i in range(self.num_cols))) + '\n'
        for row_index, row in enumerate(self):
            rep += str(row_index) + sep + sep.join(row) + '\n'
        return rep

    def __iter__(self) -> Iterator[List[str]]:
        return iter(self.contents)

    def __getitem__(self, index: int) -> List[str]:
        return self.contents[index]

    def is_in_bounds(self, row: int, col: int) -> bool:
        return (0 <= row < self.num_rows and
                0 <= col < self.num_cols)