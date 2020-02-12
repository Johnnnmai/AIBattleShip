# from fileinput import filename
from typing import Any, Tuple, List, Iterator

class Configuration(object):
    def __init__(self, filename: str) -> None:
        self.read_config_file(filename)
        self.board_row = self.breakup_config_list_board_row()
        self.board_col = self.breakup_config_list_board_col()
        self.ship_list_of_tuples = self.breakup_config_list_ship_tuples(self.config_list)

    def read_config_file(self, filename: str) -> List[Tuple[str, int]]:
        self.config_list = []
        with open(filename) as fil:
            for line in fil:
                first, second = line.split()
                tup = first, second
                self.config_list.append(tup)
        return self.config_list

    def get_board_rows(self) -> int:
        return self.board_row

    def get_board_cols(self) -> int:
        return self.board_col

    def get_ship_list(self) -> List[Tuple[str, int]]:
        return self.ship_list_of_tuples

    def breakup_config_list_board_row(self) -> int:
        row_str, col_str = self.config_list[0]
        row_int: int = int(row_str)
        return row_int

    def breakup_config_list_board_col(self) -> int:
        row_str, col_str = self.config_list[0]
        col_int: int = int(col_str)
        return col_int

    def breakup_config_list_ship_tuples(self, config_list: List[Tuple[str, int]]) -> List[Tuple[str, int]]:
        return self.config_list[1:]

    def __str__(self) -> str:
        sep = " "
        rep = str(self.board_row) + sep + str(self.board_col) + '\n'
        for row in enumerate(self):
            rep += str(row[0]) + sep + str(row[1]) + '\n'
        return rep

    def __iter__(self) -> Iterator[List[Tuple[str, int]]]:
        return iter(self.ship_list_of_tuples)

    def __getitem__(self, index: int) -> List[str]:
        return self.ship_list_of_tuples[index]