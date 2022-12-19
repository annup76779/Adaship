class Board:
  board = []
  ships = {
    'Carrier': 5,
    'Battleship': 4,
    'Destroyer': 3,
    'Submarine': 3,
    'Patrol Boat': 2
  }

  def __init__(self, row, column) -> None:
    self.row = row
    self.column = column

  def emptyBoard(self):
    for i in range(10):
      row = []
      for j in range(10):
        row.append(' ')
      Board.board.append(row)
    return Board.board

  def displayBoard(self, board):

    for i in range(len(board)):
      print('|'.join(board[i]))
      print('-' * 20)

  def updateBoard(self, row, column, ship, direction):
    if direction.upper() == 'V':
      for i in range(row, row + ships[ship]):
        Board.board[i][column] = ship[0]
    elif direction.upper() == 'H':
      for i in range(column, column + ships[ship]):
        Board.board[row][i] = ship[0]
    return Board.board


obj = Board(10, 10)
board = obj.emptyBoard()
obj.displayBoard(board)

mainMenu = '''1. One Player v Computer 
2. Two Player 
3. Computer v Computer 
0. Quit'''
print(mainMenu)
menuChoice = input("Enter game choice: ")
print(menuChoice)

menuBoardSetup = '''1. Select and Place a Ship
2. Select and Auto-Place a Ship 
3. Auto-Place All Available Ships
4. Auto-place All Ships
5. Reset Board'''

print(menuBoardSetup)
setupChoice = input("Select board setup to conitinue: ")
print(setupChoice)

coordinates = {
  'A': 0,
  'B': 1,
  'C': 2,
  'D': 3,
  'E': 4,
  'F': 5,
  'G': 6,
  'H': 7,
  'I': 8,
  'J': 9,
}

ships = {
  'Carrier': 5,
  'Battleship': 4,
  'Destroyer': 3,
  'Submarine': 3,
  'Patrol Boat': 2
}

selectShip = input("Select a ship: ")
directionShip = input("Vertical or Horizontal: [V/H]: ")
coordinateShip = input("Enter ship coardinates: ")

column, row = list(coordinateShip)
print(row, column)
row_index = int(row) - 1
col_index = coordinates[column]
print(row_index, col_index)
print(selectShip + directionShip + coordinateShip)

board = obj.updateBoard(row_index, col_index, selectShip, directionShip)
obj.displayBoard(board)
