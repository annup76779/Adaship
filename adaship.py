from random import shuffle

from board import Board
from config import ships, board_size
from game_play import play_adaship

import sys

from players import Player, Computer
from utils import get_coordinates_tuple


def one_vs_computer(salvo = False):
    # place ships on the board
    print("Place boats on the board: ")
    player = Player(1)
    computer = Computer(1)

    # make each other opponent of each other
    player.opponent = computer
    computer.opponent = player

    # setup boards
    player.set_up_board()
    computer.set_up_board()
    player.show_board()
    computer.show_board()

    print("\n\nStarting battle ...")
    players = [player, computer]
    shuffle(players)
    iteration = 0
    current_player = None
    while player.board.board_status and computer.board.board_status:
        current_player = players[iteration % 2]
        current_player.play()
        iteration += 1

    winner = players[(iteration+1) % 2]
    print("Winner is", winner)
    winner.show_board()
    player.show_board()


def two_players(salvo=False):
    pass



if __name__ == '__main__':
    c = input("1. One player v computer game\n"
              "2. Two player game\n"
              "3. One player v computer (salvo) game\n"
              "4. Two player game (salvo) game"
              "5. Quit\n")
    if c.strip() == "1":
        one_vs_computer()
    elif c.strip() == "2":
        two_players()
    elif c.strip() == "3":
        pass
    elif c.strip() == "4":
        pass
    else:
        sys.exit(0)
