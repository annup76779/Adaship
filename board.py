from config import board_size, ships
from ships import Ship


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

    def validate_ship_placement(self, x: int, y: int, direction: str, size: int):
        sum_of_free_place = 0
        try:
            if direction.lower() == "v":  # for vertical alignment of boat
                for index in range(size):
                    if self.board[index+y][x] != ".":
                        sum_of_free_place += 1
            elif direction.lower() == "h":  # for horizontal alignment of boat
                for index in range(size):
                    if self.board[y][index+x] != ".":
                        sum_of_free_place += 1
            print(sum_of_free_place)
            return sum_of_free_place == 0
        except IndexError:
            return False

    def release_ship_position(self, ship: str):
        ship_obj = self.onboard_ships.get(ship)
        x, y, direction = ship_obj.get_xyd
        try:
            if direction.lower() == "v":  # for vertical alignment of boat
                for index in range(ship_obj.size):
                    self.board[index+y][x] = 0
            elif direction.lower() == "h":  # for horizontal alignment of boat
                for index in range(ship_obj.size):
                    self.board[y][index + x] = ship_obj
        except IndexError:
            return

    def update_board(self, x: str, y: int, direction: str, ship: str) -> bool:
        size: int = ships.get(ship)
        if size is None:
            print("Failed: Ship %s not found" % ship, end="\n\n")
            return False

        if self.onboard_ships.get(ship).x is not None:
            self.release_ship_position(ship)

        # get the col of the board
        col = self.cols.get(x.upper())
        if col is None:
            print("Failed: Coordinate %s cannot be accessed." % x+str(y), end="\n\n")
            return False

        if not self.validate_ship_placement(col, y, direction, size):
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
                self.board[index+y][col] = ship_obj
        elif direction.lower() == "h":  # for horizontal alignment of boat
            for index in range(size):
                print("X", x, col)
                self.board[y][index+col] = ship_obj
        return True

    def hit(self, x:str, y:int):
        # get the col of the board
        col = self.cols.get(x.upper())
        coordinate_state = self.board[y][col]
        if isinstance(coordinate_state, Ship) and (not coordinate_state.is_sunken()):
            coordinate_state.hit()
        self.board[y][col] = "H"

    def get_ship_sunken_status(self):
        return {key: value.is_sunken() for key, value in self.onboard_ships.items()}

    def __str__(self):
        board = "  "+ (" ".join(self.cols.keys()) + "\n")
        row_index = 0
        for row in self.board:
            board += str(row_index)+" " + (" ".join(map(str, row)) + "\n")
            row_index += 1

        return board
