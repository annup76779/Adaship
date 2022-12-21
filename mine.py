from board import Board
from ships import Ship


class Mine:
    def __init__(self, x: int, y: int, board: Board):
        self.x = x
        self.y = y
        if isinstance(board, Board):
            self.board = board
        else:
            raise ValueError("Cannot connect to board")
        if isinstance(self.board[self.x][self.y], Ship):
            # name the mine to the name of the ship on which the mine is set
            self.name = self.board[self.x][self.y].name.lower()

            # hold the ship object in ship_obj to reference to it later
            self.ship_obj = self.board[self.x][self.y]
            self.board[self.x][self.y] = self
            self.is_ship_and_mine = True
        else:
            self.name = "%"  # this is how mines are represented on the board
