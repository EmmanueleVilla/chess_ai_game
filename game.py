import subprocess

import jsonpickle

from board import build_pieces
from game_state import GameState
from moves import get_moves
from utils import print_board


def play(board_size, args):
    """Starts the game"""
    turn_number = 0
    pieces = build_pieces(board_size)
    while True:
        print_board(pieces)
        turn_color = "W"
        turn_number += 1
        print(jsonpickle.encode(get_moves(pieces[12], pieces)))
        pieces = play_turn(board_size, turn_number, turn_color, pieces, args[0])
        print_board(pieces)
        turn_color = "B"
        turn_number += 1
        pieces = play_turn(board_size, turn_number, turn_color, pieces, args[0])
        break


def play_turn(board_size, turn_number, turn_color, pieces, cmd):
    """Plays the turn with the given executable command"""
    state = GameState(board_size, turn_number, turn_color, pieces)
    with subprocess.Popen(
            f'{cmd} "{jsonpickle.encode(state)}"',
            stdout=subprocess.PIPE,
            bufsize=1,
            universal_newlines=True,
            shell=True
    ) as process:
        for line in process.stdout:
            print(line)
    return pieces
