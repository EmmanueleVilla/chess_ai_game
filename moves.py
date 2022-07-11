from functools import reduce

from board import search_by_indexes
from piece import to_letter, Piece


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


def append_piece(piece: Piece, i: int, j: int, capture: bool = False):
    """Joins the piece information and the arrival cell"""
    output = piece.name if piece.name != "P" else ""
    output += to_letter(piece.i()) if piece.name == "P" and capture else ""
    output += "x" if capture else ""
    output += to_letter(i)
    output += f'{j}'
    return output


def get_moves_with_direction(board_size: int, piece: Piece, pieces: [Piece], delta_i: int, delta_j: int,
                             stop_on_count: int, stop_on_enemy=False, only_on_enemy=False):
    """Calculate the possible moves in the given direction,
    moving by the given delta and stopping at the given conditions."""
    output = []
    i = piece.i()
    j = piece.j()
    for _ in range(stop_on_count):
        i += delta_i
        j += delta_j
        if i > board_size or j > board_size or i < 1 or j < 1:
            break
        occupier = search_by_indexes(pieces, i, j)
        if occupier is not None:
            if occupier.color == piece.color or stop_on_enemy:
                break
            output.append(append_piece(piece, i, j, True))
            break
        if occupier is None and only_on_enemy:
            break
        output.append(append_piece(piece, i, j))
    return output


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
    # add en-passant capture
    return forward + right + left


def get_moves_rook(board_size, piece, pieces):
    """Returns the available moves of the given rook in the given board"""
    deltas = [
        (0, 1),
        (0, -1),
        (1, 0),
        (-1, 0)
    ]
    return get_moves_from_deltas(board_size, piece, pieces, deltas)


def get_moves_bishop(board_size, piece, pieces):
    """Returns the available moves of the given bishop in the given board"""
    deltas = [
        (1, 1),
        (1, -1),
        (-1, 1),
        (-1, -1)
    ]
    return get_moves_from_deltas(board_size, piece, pieces, deltas)


def get_moves_knight(board_size, piece, pieces):
    """Returns the available moves of the given knight in the given board"""
    print(board_size)
    print(piece)
    print(pieces)
    return []


def get_moves_queen(board_size, piece, pieces):
    """Returns the available moves of the given queen in the given board"""
    deltas = [
        (0, 1),
        (0, -1),
        (1, 0),
        (-1, 0),
        (1, 1),
        (1, -1),
        (-1, 1),
        (-1, -1)
    ]
    return get_moves_from_deltas(board_size, piece, pieces, deltas)


def get_moves_king(board_size, piece, pieces):
    """Returns the available moves of the given king in the given board"""
    deltas = [
        (0, 1),
        (0, -1),
        (1, 0),
        (-1, 0),
        (1, 1),
        (1, -1),
        (-1, 1),
        (-1, -1)
    ]
    return get_moves_from_deltas_with_max_distance(board_size, piece, pieces, deltas, 1)


def get_moves_from_deltas(board_size, piece, pieces, deltas):
    """Returns the available moves of the given piece in the given directions with standard breaks"""
    return reduce(lambda x, y: x + y,
                  [get_moves_with_direction(board_size, piece, pieces, d[0], d[1], board_size) for d in deltas])


def get_moves_from_deltas_with_max_distance(board_size, piece, pieces, deltas, max_distance):
    """Returns the available moves of the given piece in the given directions with standard breaks"""
    return reduce(lambda x, y: x + y,
                  [get_moves_with_direction(board_size, piece, pieces, d[0], d[1], max_distance) for d in deltas])
