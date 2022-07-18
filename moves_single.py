from functools import reduce
from typing import List, Tuple

from color import Color
from move import Move
from moves_utils import get_moves_with_direction
from piece import Piece


def get_moves(board_size: int, piece: Piece, pieces: List[Piece]) -> List[Move]:
    """Returns the available moves of the given piece in the given board"""
    switcher = {
        "P": get_moves_pawn,
        "R": get_moves_rook,
        "N": get_moves_knight,
        "B": get_moves_bishop,
        "Q": get_moves_queen,
        "K": get_moves_king
    }

    return switcher[piece.name](board_size, piece, pieces)


def get_moves_pawn(board_size: int, piece: Piece, pieces: List[Piece]) -> List[Move]:
    """Returns the available moves of the given pawn in the given board"""
    direction = -1 if piece.color == Color.BLACK else 1

    forward: List[Move] = get_moves_with_direction(board_size, piece, pieces, 0, direction, 1 if piece.moved else 2,
                                                   stop_on_enemy=True)
    right: List[Move] = get_moves_with_direction(board_size, piece, pieces, 1, direction, 1,
                                                 only_on_enemy=True)
    left: List[Move] = get_moves_with_direction(board_size, piece, pieces, -1,
                                                direction, 1,
                                                only_on_enemy=True)
    # Todo: add en-passant capture
    # Todo: add promotion
    return forward + right + left


def get_moves_rook(board_size: int, piece: Piece, pieces: List[Piece]) -> List[Move]:
    """Returns the available moves of the given rook in the given board"""
    deltas = [(0, 1), (0, -1), (1, 0), (-1, 0)]
    return get_moves_from_deltas(board_size, piece, pieces, deltas)


def get_moves_bishop(board_size: int, piece: Piece, pieces: List[Piece]) -> List[Move]:
    """Returns the available moves of the given bishop in the given board"""
    deltas = [(1, 1), (1, -1), (-1, 1), (-1, -1)]
    return get_moves_from_deltas(board_size, piece, pieces, deltas)


def get_moves_knight(board_size: int, piece: Piece, pieces: List[Piece]) -> List[Move]:
    """Returns the available moves of the given knight in the given board"""
    deltas = [(2, 1), (2, -1), (-2, 1), (-2, -1), (1, 2), (1, -2), (-1, 2), (-1, -2)]
    return get_moves_from_deltas_with_max_distance(board_size, piece, pieces, deltas, 1)


def get_moves_queen(board_size: int, piece: Piece, pieces: List[Piece]) -> List[Move]:
    """Returns the available moves of the given queen in the given board"""
    deltas = [(0, 1), (0, -1), (1, 0), (-1, 0), (1, 1), (1, -1), (-1, 1), (-1, -1)]
    return get_moves_from_deltas(board_size, piece, pieces, deltas)


def get_moves_king(board_size: int, piece: Piece, pieces: List[Piece]) -> List[Move]:
    """Returns the available moves of the given king in the given board"""
    deltas = [(0, 1), (0, -1), (1, 0), (-1, 0), (1, 1), (1, -1), (-1, 1), (-1, -1)]
    # Todo: Add castling
    return get_moves_from_deltas_with_max_distance(board_size, piece, pieces, deltas, 1)


def get_moves_from_deltas(board_size: int, piece: Piece, pieces: List[Piece], deltas: List[Tuple[int, int]]) \
        -> List[Move]:
    """Returns the available moves of the given piece in the given directions with standard breaks"""
    return reduce(lambda x, y: x + y,
                  [get_moves_with_direction(board_size, piece, pieces, d[0], d[1], board_size) for d in deltas])


def get_moves_from_deltas_with_max_distance(board_size: int, piece: Piece, pieces: List[Piece],
                                            deltas: List[Tuple[int, int]], max_distance: int) -> List[Move]:
    """Returns the available moves of the given piece in the given directions with standard breaks"""
    return reduce(lambda x, y: x + y,
                  [get_moves_with_direction(board_size, piece, pieces, d[0], d[1], max_distance) for d in deltas])
