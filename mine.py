from board import Board
from config import board_size
from ships import Ship


class Mine:
    def __init__(self, x: str, y: int, board: Board):
        self.col = x
        self.x = Board.cols.get(x.upper())
        self.y = y
        if isinstance(board, Board):
            self.board = board
        else:
            raise ValueError("Cannot connect to board")
        print(y, x)
        if isinstance(self.board.board[self.y][self.x], Ship):
            # name the mine to the name of the ship on which the mine is set
            self.name = self.board.board[self.y][self.x].name[:1].lower()

            # hold the ship object in ship_obj to reference to it later
            self.ship_obj = self.board.board[self.y][self.x]
            self.board.board[self.y][self.x] = self
            self.is_ship_and_mine = True
        else:
            self.name = "%"  # this is how mines are represented on the board
            self.is_ship_and_mine = False

    def blast(self):
        if self.is_ship_and_mine:
            self.ship_obj.hit()
            self.board.board[self.y][self.x] = "H"

        # hit the neighbors 8 coordinates of the board
        # first Column
        try:
            self.board.hit(tuple(Board.cols.keys())[self.x - 1], self.y - 1)
        except IndexError:
            pass
        try:
            self.board.hit(tuple(Board.cols.keys())[self.x], self.y - 1)
        except IndexError:
            pass
        try:
            self.board.hit(tuple(Board.cols.keys())[self.x + 1], self.y - 1)
        except IndexError:
            pass

        # second Column
        try:
            self.board.hit(tuple(Board.cols.keys())[self.x - 1], self.y)
        except IndexError:
            pass
        try:
            self.board.hit(tuple(Board.cols.keys())[self.x + 1], self.y)
        except IndexError:
            pass

        # third Column
        try:
            self.board.hit(tuple(Board.cols.keys())[self.x - 1], self.y + 1)
        except IndexError:
            pass
        try:
            self.board.hit(tuple(Board.cols.keys())[self.x], self.y + 1)
        except IndexError:
            pass
        try:
            self.board.hit(tuple(Board.cols.keys())[self.x + 1], self.y + 1)
        except IndexError:
            pass

    def __str__(self):
        return self.name

    def __repr__(self):
        return self.name
