from random import shuffle, randint, choice

from board import Board
from config import ships, board_size

import sys

from utils import get_coordinates_tuple


def one_vs_computer():
    # place ships on the board
    print("Place boats on the board: ")
    first_player_board = Board("Player")
    computer_board = Board("Computer")
    while True:
        placed, not_placed = first_player_board.get_placed_and_not_placed_ships()
        print("\nBoats placed on the board: ")
        if not placed:
            print("\tNo boats on the board!")
        else:
            print("\to ", "\n\to  ".join(placed))

        print("\nShip yet to be placed: ")
        if not not_placed:
            print("\tNo boats to be placed on the board!")
            break
        else:
            print("\to ", "\n\to  ".join(not_placed))

        # starting asking for the boat details to place it
        # also have option to automatically place ships legally
        print("\n\nPlease Choose options from bellow options: ")
        print("1. Press Enter to 'Auto place rest of the boat': ")
        print("2. Enter the name fo the boat want to place: ")
        boat = input().strip().title()

        if boat == "":  # this means auto_fill is chosen
            first_player_board.auto_place_remaining_ship()
            break

        if boat not in ships.keys():
            print("Invalid boat name!!!")
            continue
        coordinates = input("Enter the coordinates of the %s. E.g.: F3: " % boat).strip().capitalize()
        x, y = get_coordinates_tuple(coordinates)
        # in case co-ordinates are not in valid format
        while x is None or y is None:
            print("Invalid coordinates!!! Please enter in (E.g.: F3) format.")
            coordinates = input().strip().capitalize()
            x, y = get_coordinates_tuple(coordinates)

        # asking for direction of the ship
        print("Please enter the direction in which the boat is facing: ")
        print("For Vertical direction, enter 'V' or 'v'")
        print("For Horizontal direction, enter 'H' or 'h'")
        direction = input().strip().capitalize()[:1]

        # updating the board with the new entry of the boat placement
        first_player_board.update_board(x, y, direction, boat)
    print("Generating computer board...")
    computer_board.auto_place_remaining_ship()
    print("Computer has generated it's board.")
    print("\n\nStarting battle ...")

    target_group = [first_player_board, computer_board]
    shuffle(target_group)
    iteration = 0
    while first_player_board.board_status and computer_board.board_status:

        # this way we will get the next target board in each iteration
        target = target_group[iteration % 2]
        if target.player.title() == "Player":
            print("Computer's chance - ")
            print(computer_board)

            x = choice(tuple(Board.cols.keys()))
            y = randint(0, board_size[0] - 1)
            while not target.hit(x, y, True):
                x = choice(tuple(Board.cols.keys()))
                y = randint(0, board_size[0] - 1)
            input("Press any key to continue:- ")
        else:
            print("Player's chance - ")
            print(first_player_board)
            coordinates = input("Enter the coordinates to hit E.g.: F3: ").strip().capitalize()
            x, y = get_coordinates_tuple(coordinates)
            if x is None or y is None:
                print("Invalid coordinates, considered as complete Miss.")
            else:
                target.hit(x, y)
        print("%s\n\n" % ("--" * board_size[1]))
        iteration += 1


if __name__ == '__main__':
    c = input("1. One player v computer game\n2. Quit\n")
    if c.strip() == "1":
        one_vs_computer()
    else:
        sys.exit(0)
