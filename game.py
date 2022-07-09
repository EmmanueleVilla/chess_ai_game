import subprocess

import jsonpickle

from board import build_pieces
from game_state import GameState
from utils import print_board


def play(board_size, args):
    """Starts the game"""
    pieces = build_pieces(board_size)
    print_board(pieces)
    pieces = play_turn(board_size, pieces, args[0])
    print_board(pieces)


def play_turn(board_size, pieces, cmd):
    """Plays the turn with the given executable command"""
    state = GameState(board_size, pieces)
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
