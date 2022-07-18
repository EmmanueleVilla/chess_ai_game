import subprocess
from typing import List

import jsonpickle  # type: ignore

from board import build_pieces
from color import Color
from game_state import GameState
from moves_single import get_moves
from piece import Piece
from utils import print_board


def play(board_size: int, args: List[str]):
    """Starts the game"""
    turn_number = 0
    pieces = build_pieces(board_size)
    while True:
        print_board(board_size, pieces)
        turn_color = Color.WHITE
        turn_number += 1
        print(jsonpickle.encode(get_moves(board_size, pieces[10], pieces)))
        pieces = play_turn(board_size, turn_number, turn_color, pieces, args[0])
        print_board(board_size, pieces)
        turn_color = Color.BLACK
        pieces = play_turn(board_size, turn_number, turn_color, pieces, args[0])
        break


def play_turn(board_size: int, turn_number: int, turn_color: Color, pieces: List[Piece], cmd: str):
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
