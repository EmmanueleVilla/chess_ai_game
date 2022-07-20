import hashlib
import subprocess
from calendar import timegm
from datetime import datetime
from typing import List, Tuple, Union, Set

import pygame.display

from board import build_pieces
from color import Color
from game_result import GameResult
from game_state import GameState
from log import get_session_id, init_files, write_board, write_message, MESSAGE_FILENAME, write_an, GAMES_FILENAME, \
    init_game_log_file, write_game
from move import Move
from moves import get_all_moves
from moves_applier import apply_move
from piece import Piece
from utils import board_to_string, show_board


def start_game(args: List[str]) -> None:
    """Starts 10 games"""
    path = get_session_id()
    init_game_log_file(path)
    white_points = 0.0
    black_points = 0.0
    pygame.init()  # pylint: disable=maybe-no-member
    screen = pygame.display.set_mode((1280, 720))
    for i in range(0, 10):
        result = play(screen, 8, args, i, path)
        white_points += result.white
        black_points += result.black
        message = f'{result.get_white()}-{result.get_black()} ({result.message})'
        print(message)
        write_game(path, message + "\n")
        show_board(screen, 8, result.pieces, path + GAMES_FILENAME)
        start = timegm(datetime.utcnow().utctimetuple())
        while timegm(datetime.utcnow().utctimetuple()) - start < 3:
            pygame.event.pump()
    message = f'Results: {white_points}-{black_points}'
    print(message)
    write_game(path, message)


def play(screen: pygame.surface.Surface, board_size: int, args: List[str], game_id: int, base_path: str) -> GameResult:
    """Starts the game"""
    message = f'Game {game_id}: '
    write_game(base_path, message)
    print(message, end="")
    turn_number = 1
    pieces = build_pieces(board_size)

    path = init_files(base_path, game_id)

    board = board_to_string(board_size, pieces)
    write_board(path, board)
    fifty_rule_count = 0
    repetitions: dict[str, int] = {}

    show_board(screen, board_size, pieces, base_path + GAMES_FILENAME)

    while turn_number < 1000:
        pygame.event.pump()
        write_an(path, f'{turn_number}. ')
        turn_color = Color.WHITE
        result = play_turn(board_size, turn_number, turn_color, pieces, args[0],
                           path + "/" + MESSAGE_FILENAME)
        pieces = result[1]
        write_an(path, result[0])
        board = board_to_string(board_size, pieces)
        show_board(screen, board_size, pieces, base_path + GAMES_FILENAME)
        write_board(path, board)
        board_hash = hashlib.md5(board.encode('utf-8')).hexdigest()
        board_count = repetitions.get(board_hash, 0)
        repetitions[board_hash] = board_count + 1

        end = check_end_turn(board_count + 1, fifty_rule_count, result[0], turn_color, pieces)
        if end is not None:
            write_an(path, f' {end.get_white()}-{end.get_black()}')
            return end

        if "+" in result[0]:
            fifty_rule_count = 0

        turn_color = Color.BLACK
        result = play_turn(board_size, turn_number, turn_color, pieces, args[1],
                           path + "/" + MESSAGE_FILENAME)
        pieces = result[1]
        write_an(path, f' {result[0]}\n')
        board = board_to_string(board_size, pieces)
        show_board(screen, board_size, pieces, base_path + GAMES_FILENAME)
        write_board(path, board)

        board_hash = hashlib.md5(board.encode('utf-8')).hexdigest()
        board_count = repetitions.get(board_hash, 0)
        repetitions[board_hash] = board_count + 1

        end = check_end_turn(board_count + 1, fifty_rule_count, result[0], turn_color, pieces)
        if end is not None:
            write_an(path, f' {end.get_white()}-{end.get_black()}')
            return end

        if "+" in result[0]:
            fifty_rule_count = 0

        turn_number += 1
        fifty_rule_count += 1

    return GameResult(0.5, 0.5, "Turns elapsed", pieces)


def check_end_turn(board_count: int, fifty_rule_count: int, move: str, color: Color, pieces: Set[Piece]) \
        -> Union[GameResult, None]:
    """Check if the match is ended"""
    if board_count == 3:
        return GameResult(0.5, 0.5, "Repetition", pieces)

    if fifty_rule_count == 50:
        return GameResult(0.5, 0.5, "50 Rule", pieces)

    if "#" in move:
        return GameResult(1 if color == Color.WHITE else 0, 0 if color == Color.WHITE else 1, "Checkmate", pieces)

    if "Stalemate" in move:
        return GameResult(0.5, 0.5, "Stalemate", pieces)

    return None


def encode_game_state(state: GameState) -> str:
    """Encodes the game state"""
    return str(state)


def play_turn(board_size: int, turn_number: int, turn_color: Color, pieces: Set[Piece], cmd: str, path: str) \
        -> Tuple[str, Set[Piece]]:
    """Asks the AI to return the move to be played"""
    moves = get_all_moves(board_size, pieces, turn_color)
    if len(moves) == 0:
        return "Stalemate", pieces
    state = GameState(board_size, turn_number, turn_color, pieces, moves)
    encoded = encode_game_state(state)
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


def process_move(pieces: Set[Piece], move: str, moves: List[Move]) -> Tuple[str, Set[Piece]]:
    """Process the move returned by the AI"""
    move_detail = [m for m in moves if m.an_string == move]
    if len(move_detail) == 0:
        return f'Invalid Move {move}', pieces
    return move, apply_move(pieces, move_detail[0])
