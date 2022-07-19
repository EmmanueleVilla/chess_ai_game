import hashlib
import os.path
import subprocess
from typing import List, Tuple

import jsonpickle  # type: ignore

from board import build_pieces
from color import Color
from game_state import GameState
from log import get_session_id, init_files, write_board, write_message, MESSAGE_FILENAME, write_an
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

    board = board_to_string(board_size, pieces)
    print(board)
    write_board(path, board)
    fifty_rule_count = 0
    repetitions: dict[str, int] = {}
    while turn_number < 1000:
        an_log = f'{turn_number}. '
        turn_color = Color.WHITE
        result = play_turn(board_size, turn_number, turn_color, pieces, args[0],
                           path + "/" + MESSAGE_FILENAME)
        pieces = result[1]
        an_log += result[0]
        board = board_to_string(board_size, pieces)
        print(board)
        write_board(path, board)
        board_hash = hashlib.md5(board.encode('utf-8')).hexdigest()
        board_count = repetitions.get(board_hash, 0)
        repetitions[board_hash] = board_count + 1

        if board_count + 1 == 3:
            an_log += " 1/2-1/2 (Repetition)"
            write_an(path, an_log)
            break

        if "#" in result[0]:
            an_log += " 1-0"
            write_an(path, an_log)
            break

        if "Stalemate" in result[0]:
            an_log += " 1/2-1/2 (Stalemate)"
            write_an(path, an_log)
            break

        if "+" in result[0]:
            fifty_rule_count = 0

        turn_color = Color.BLACK
        result = play_turn(board_size, turn_number, turn_color, pieces, args[0],
                           path + "/" + MESSAGE_FILENAME)
        pieces = result[1]
        an_log += f' {result[0]}\n'
        board = board_to_string(board_size, pieces)
        print(board)
        write_board(path, board)

        board_hash = hashlib.md5(board.encode('utf-8')).hexdigest()
        board_count = repetitions.get(board_hash, 0)
        repetitions[board_hash] = board_count + 1

        if board_count + 1 == 3:
            an_log += " 1/2-1/2 (Repetition)"
            write_an(path, an_log)
            break

        if "#" in result[0]:
            an_log += " 0-1"
            write_an(path, an_log)
            break

        if "Stalemate" in result[0]:
            an_log += " 1/2-1/2 (Stalemate)"
            write_an(path, an_log)
            break

        if fifty_rule_count == 50:
            an_log += " 1/2-1/2 (50 rule)"
            write_an(path, an_log)
            break

        if "+" in result[0]:
            fifty_rule_count = 0

        write_an(path, an_log)

        turn_number += 1
        fifty_rule_count += 1


def play_turn(board_size: int, turn_number: int, turn_color: Color, pieces: List[Piece], cmd: str, path: str) \
        -> Tuple[str, List[Piece]]:
    """Asks the AI to return the move to be played"""
    moves = get_all_moves(board_size, pieces, turn_color)
    if len(moves) == 0:
        return "Stalemate", pieces
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
        return "None", pieces


def process_move(pieces: List[Piece], move: str, moves: List[Move]) -> Tuple[str, List[Piece]]:
    """Process the move returned by the AI"""
    move_detail = [m for m in moves if m.to_an() == move]
    if len(move_detail) == 0:
        return "Invalid Move", pieces
    return move, apply_move(pieces, move_detail[0])
