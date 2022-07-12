from functools import reduce

from moves_utils import get_moves_with_direction


def get_moves(board_size, piece, pieces):
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


def get_moves_pawn(board_size, piece, pieces):
    """Returns the available moves of the given pawn in the given board"""
    direction = -1 if piece.color == "B" else 1

    forward = get_moves_with_direction(board_size, piece, pieces, 0, direction, 1 if piece.moved else 2,
                                       stop_on_enemy=True)
    right = get_moves_with_direction(board_size, piece, pieces, 1, direction, 1,
                                     only_on_enemy=True)
    left = get_moves_with_direction(board_size, piece, pieces, -1,
                                    direction, 1,
                                    only_on_enemy=True)
    # Todo: add en-passant capture
    return forward + right + left


def get_moves_rook(board_size, piece, pieces):
    """Returns the available moves of the given rook in the given board"""
    deltas = [(0, 1), (0, -1), (1, 0), (-1, 0)]
    return get_moves_from_deltas(board_size, piece, pieces, deltas)


def get_moves_bishop(board_size, piece, pieces):
    """Returns the available moves of the given bishop in the given board"""
    deltas = [(1, 1), (1, -1), (-1, 1), (-1, -1)]
    return get_moves_from_deltas(board_size, piece, pieces, deltas)


def get_moves_knight(board_size, piece, pieces):
    """Returns the available moves of the given knight in the given board"""
    deltas = [(2, 1), (2, -1), (-2, 1), (-2, -1), (1, 2), (1, -2), (-1, 2), (-1, -2)]
    return get_moves_from_deltas_with_max_distance(board_size, piece, pieces, deltas, 1)


def get_moves_queen(board_size, piece, pieces):
    """Returns the available moves of the given queen in the given board"""
    deltas = [(0, 1), (0, -1), (1, 0), (-1, 0), (1, 1), (1, -1), (-1, 1), (-1, -1)]
    return get_moves_from_deltas(board_size, piece, pieces, deltas)


def get_moves_king(board_size, piece, pieces):
    """Returns the available moves of the given king in the given board"""
    deltas = [(0, 1), (0, -1), (1, 0), (-1, 0), (1, 1), (1, -1), (-1, 1), (-1, -1)]
    # Todo: Add castling
    return get_moves_from_deltas_with_max_distance(board_size, piece, pieces, deltas, 1)


def get_moves_from_deltas(board_size, piece, pieces, deltas):
    """Returns the available moves of the given piece in the given directions with standard breaks"""
    return reduce(lambda x, y: x + y,
                  [get_moves_with_direction(board_size, piece, pieces, d[0], d[1], board_size) for d in deltas])


def get_moves_from_deltas_with_max_distance(board_size, piece, pieces, deltas, max_distance):
    """Returns the available moves of the given piece in the given directions with standard breaks"""
    return reduce(lambda x, y: x + y,
                  [get_moves_with_direction(board_size, piece, pieces, d[0], d[1], max_distance) for d in deltas])
