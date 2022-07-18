import os.path
import subprocess
from typing import List

import jsonpickle  # type: ignore
import jsonpickle  # type: ignore

from board import build_pieces
from color import Color
from game_state import GameState
from log import get_session_id, init_files, write_board, write_message, message_filename
from move import Move
from moves_applier import apply_move
from moves_global import get_all_moves
from piece import Piece
from utils import board_to_string


def start_game(args: List[str]) -> None:
    """Starts 10 games"""
    path = get_session_id()
    for i in range(0, 10):
        play(8, args, i, path)


def play(board_size: int, args: List[str], game_id: int, base_path: str) -> None:
    """Starts the game"""
    turn_number = 1
    pieces = build_pieces(board_size)
    path = os.path.join(base_path, f'{game_id}')
    init_files(path)
    while True:
        board = board_to_string(board_size, pieces)
        print(board)
        write_board(path, board)
        turn_color = Color.WHITE
        pieces = play_turn(board_size, turn_number, turn_color, pieces, args[0],
                           path + "/" + message_filename)
        board = board_to_string(board_size, pieces)
        print(board)
        write_board(path, board)
        # print_board(board_size, pieces)
        # turn_color = Color.BLACK
        # pieces = play_turn(board_size, turn_number, turn_color, pieces, args[0])
        turn_number += 1
        break


def play_turn(board_size: int, turn_number: int, turn_color: Color, pieces: List[Piece], cmd: str, path: str) \
        -> List[Piece]:
    """Asks the AI to return the move to be played"""
    my_pieces = [piece for piece in pieces if piece.color == turn_color]
    moves = get_all_moves(board_size, my_pieces, turn_color)
    state = GameState(board_size, turn_number, turn_color, pieces, moves)
    encoded = jsonpickle.encode(state)
    write_message(path, encoded)
    with subprocess.Popen(
            f'{cmd} "{path}"',
            stdout=subprocess.PIPE,
            bufsize=1,
            universal_newlines=True,
            shell=True
    ) as process:
        if process.stdout is not None:
            for line in process.stdout:
                return process_move(pieces, line.replace("\n", ""), moves)
        return pieces


def process_move(pieces: List[Piece], move: str, moves: List[Move]) -> List[Piece]:
    """Process the move returned by the AI"""
    move_detail = [m for m in moves if m.to_an() == move]
    if len(move_detail) == 0:
        # Todo: Handle move not defined
        return pieces
    return apply_move(pieces, move_detail[0])
