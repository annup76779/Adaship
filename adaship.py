from random import shuffle
import sys

from players import Player, Computer


def one_vs_computer(salvo = False, with_mine=False):
    # place ships on the board
    print("Place boats on the board: ")
    player = Player(1)
    computer = Computer(1)

    # make each other opponent of each other
    player.opponent = computer
    computer.opponent = player

    # setup boards
    if player.set_up_board(with_mine) == "quit":
        print("Exiting this game play.")
        return
    computer.set_up_board(with_mine)

    # finally show boards of each player after setting up
    player.show_board()
    computer.show_board()

    print("\n\nStarting battle ...")
    players = [player, computer]
    shuffle(players)
    iteration = 0
    current_player = None
    while player.board.board_status and computer.board.board_status:
        current_player = players[iteration % 2]
        if salvo:
            current_player.play_salvo()
        else:
            current_player.play()
        iteration += 1

    winner = players[(iteration+1) % 2]
    not_winner = players[iteration % 2]
    print("Winner is", winner)
    winner.show_board()
    not_winner.show_board()


def two_players(salvo=False, with_mine = False):

    # place ships on the board
    print("Place boats on the board: ")
    player = Player(1)
    player_2 = Player(2)

    # make each other opponent of each other
    player.opponent = player_2
    player_2.opponent = player

    # setup boards
    if player.set_up_board(with_mine) == "quit":
        print("Exiting this game play.")
        return
    if player_2.set_up_board(with_mine)== "quit":
        print("Exiting this game play.")
        return

    # finally show board of both the players
    player.show_board()
    player_2.show_board()

    print("\n\nStarting battle ...")
    players = [player, player_2]
    shuffle(players)
    iteration = 0
    current_player = None
    while player.board.board_status and player_2.board.board_status:
        current_player = players[iteration % 2]
        if salvo:
            current_player.play_salvo()
        else:
            current_player.play()
        iteration += 1

    winner = players[(iteration+1) % 2]
    not_winner = players[iteration % 2]
    print("Winner is", winner)
    winner.show_board()
    not_winner.show_board()


def computer_vs_computer(salvo=False, with_mine=False):
    # place ships on the board
    print("Place boats on the board: ")
    computer1 = Computer(1)
    computer2 = Computer(2)

    # make each other opponent of each other
    computer1.opponent = computer2
    computer2.opponent = computer1

    # setup boards
    computer1.set_up_board(with_mine)
    computer2.set_up_board(with_mine)

    # finally show boards of each player after setting up
    computer1.show_board()
    computer2.show_board()

    print("\n\nStarting battle ...")
    players = [computer1, computer2]
    shuffle(players)
    iteration = 0
    current_player = None
    while computer1.board.board_status and computer2.board.board_status:
        current_player = players[iteration % 2]
        if salvo:
            current_player.play_salvo()
        else:
            current_player.play()
        iteration += 1

    winner = players[(iteration+1) % 2]
    not_winner = players[iteration % 2]
    print("Winner is", winner)
    winner.show_board()
    not_winner.show_board()


if __name__ == '__main__':
    while True:
        c = input("1. One player v computer game\n"
                  "2. Two player game\n"
                  "3. One player v computer (salvo) game\n"
                  "4. Two player game (salvo) game\n"
                  "5. One player v computer (hidden mines) game\n"
                  "6. Two player game (hidden mines) game\n"
                  "7. Computer v computer (hidden mines)\n"
                  "8. Quit\n")
        if c.strip() == "1":
            one_vs_computer()
        elif c.strip() == "2":
            two_players()
        elif c.strip() == "3":
            one_vs_computer(True)
        elif c.strip() == "4":
            two_players(True)
        elif c.strip() == "5":
            one_vs_computer(False, True)
        elif c.strip() == "6":
            two_players(False, True)
        elif c.strip() == "7":
            computer_vs_computer(False, True)
        elif c.strip() == "8":
            sys.exit(0)

        print("\n\n")
