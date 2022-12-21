from functools import reduce

from config import board_size, ships
from mine import Mine
from ships import Ship

from random import randint, choice


class Board:
    # dict of accepted columns of the board, e.g. A
    cols = dict()
    alpha = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

    # creating the columns automatically
    for col in range(board_size[1]):
        if col < 26:
            key = alpha[col]
        else:
            key = alpha[(col // 26) - 1] + alpha[col % 26]
        cols[key] = col

    def __init__(self):
        self.board = [["."] * board_size[1] for _ in range(board_size[0])]
        self.onboard_ships: dict = {ship_name: Ship(ship_name, size) for ship_name, size in ships.items()}

    def reset(self):
        for i in range(board_size[0]):
            for j in range(board_size[1]):
                self.board[i][j] = "."

    def validate_ship_placement(self, x: int, y: int, direction: str, size: int):
        sum_of_free_place = 0
        try:
            if direction.lower() == "v":  # for vertical alignment of boat
                for index in range(size):
                    if self.board[index + y][x] != ".":
                        sum_of_free_place += 1
            elif direction.lower() == "h":  # for horizontal alignment of boat
                for index in range(size):
                    if self.board[y][index + x] != ".":
                        sum_of_free_place += 1
            return sum_of_free_place == 0
        except IndexError:
            return False

    def release_ship_position(self, ship: str):
        ship_obj = self.onboard_ships.get(ship)
        x, y, direction = ship_obj.get_xyd
        try:
            if direction.lower() == "v":  # for vertical alignment of boat
                for index in range(ship_obj.size):
                    self.board[index + y][x] = 0
            elif direction.lower() == "h":  # for horizontal alignment of boat
                for index in range(ship_obj.size):
                    self.board[y][index + x] = ship_obj
        except IndexError:
            return

    def update_board(self, x: str, y: int, direction: str, ship: str, is_auto=False) -> bool:
        size: int = ships.get(ship)
        if size is None:
            if not is_auto:
                print("Failed: Boat %s not found" % ship, end="\n\n")
            return False

        if self.onboard_ships.get(ship).x is not None:
            self.release_ship_position(ship)

        # get the col of the board
        col = self.cols.get(x.upper())
        if col is None:
            if not is_auto:
                print("Failed: Coordinate %s cannot be accessed." % x + str(y), end="\n\n")
            return False

        if not self.validate_ship_placement(col, y, direction, size):
            if not is_auto:
                print("Failed: to place %s at coordinates (%s, %d)" % (ship, x, y))
            return False

        # Make a Ship class object to be used for the placement of the ship on the board
        # same Ship class object will be placed on all the coordinates of the board that belong to that ship
        ship_obj = self.onboard_ships.get(ship)
        ship_obj.x = col
        ship_obj.y = y
        ship_obj.direction = direction

        # placing the ship in the required direction
        if direction.lower() == "v":  # for vertical alignment of boat
            for index in range(size):
                self.board[index + y][col] = ship_obj
        elif direction.lower() == "h":  # for horizontal alignment of boat
            for index in range(size):
                self.board[y][index + col] = ship_obj
        return True

    def auto_place_remaining_ship(self):
        for ship, ship_obj in self.onboard_ships.items():
            if ship_obj.x is None:
                y = randint(0, board_size[0])
                x = choice(tuple(self.cols.keys()))
                direction = choice(("H", "V"))
                while not self.update_board(x, y, direction, ship, True):
                    y = randint(0, board_size[0])
                    x = choice(tuple(self.cols.keys()))
                    direction = choice(("H", "V"))
        return True

    def hit(self, x: str, y: int, auto_hit=False):
        # get the col of the board
        col = self.cols.get(x.upper())
        if col is None:
            print(f"{x.upper()}{y}", "is not a valid choice for the board.")
            return False
        try:
            if self.board[y][col] == "M" or self.board[y][col] == "H":
                print("Already cleared this spot!")
                return "exists"
        except IndexError:
            print(f"{x.upper()}{y}", "is not a valid choice for the board.")
            return False

        coordinate_state = self.board[y][col]
        if isinstance(coordinate_state, Ship) and (not coordinate_state.is_sunken()):
            coordinate_state.hit()
            self.board[y][col] = "H"
            return "Hit"
        elif isinstance(coordinate_state, Mine):
            coordinate_state.blast()
            return "Blast"
        else:
            self.board[y][col] = "M"
            return "Miss"

    def get_ship_sunken_status(self):
        return {key: value.is_sunken() for key, value in self.onboard_ships.items()}

    @property
    def board_status(self):
        return not all(boat_obj.is_sunken() == True for boat_obj in self.onboard_ships.values())

    def get_live_boats(self):
        return [boat for boat, status in self.get_ship_sunken_status().items() if status == False]

    def get_placed_and_not_placed_ships(self) -> tuple:
        """
        Use this method to get the separated list of completed ships placement and not placed ships list
        :return: tuple of placed and not placed ships
        """
        placed = []
        not_placed = []
        for ship_name, ship_obj in self.onboard_ships.items():
            if ship_obj.x is not None:
                placed.append(ship_name)
            else:
                not_placed.append(ship_name)
        return placed, not_placed

    def __str__(self):
        board = "+ " + (" ".join(self.cols.keys()) + "\n")
        row_index = 0
        for row in self.board:
            board += str(row_index) + " " + (" ".join(map(str, row)) + "\n")
            row_index += 1

        return board
