from board import search_by_indexes
from piece import to_letter


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


def check_moves_args(board_size, piece, pieces, name):
    """Checks if the arguments are legal"""
    assert board_size == 8
    assert piece in pieces
    assert piece.name == name


def append_piece(piece, i, j):
    """Joins the piece information and the arrival cell"""
    return f'{piece.name}{to_letter(piece.i())}{piece.j()}{to_letter(i)}{j}'


def get_moves_with_direction(board_size, piece, pieces, delta_i, delta_j, stop_on_count, stop_on_enemy):
    """Calculate the possible moves in the given direction,
    moving by the given delta and stopping at the given conditions"""
    output = []
    i = piece.i()
    j = piece.j()
    for _ in range(stop_on_count):
        i += delta_i
        j += delta_j
        if i > board_size or j > board_size:
            break
        occupier = search_by_indexes(pieces, i, j)
        if occupier is not None and (occupier.color == piece.color or stop_on_enemy):
            break
        output.append(append_piece(piece, i, j))
    return output


def get_moves_pawn(board_size, piece, pieces):
    """Returns the available moves of the given pawn in the given board"""
    check_moves_args(board_size, piece, pieces, "P")

    # Forward direction
    direction = -1 if piece.color == "B" else 1

    forward = get_moves_with_direction(board_size, piece, pieces, 0, direction, 1 if piece.moved else 2, True)

    # Diagonal capture
    delta_i = [-1, 1]
    delta_j = [piece.j() + direction]
    capture = [d for d in delta_i if search_by_indexes(pieces, piece.i() + d, delta_j[0]) is not None]
    # add diagonal piece capture
    # add en-passant capture
    return forward + list(append_piece(piece, r, delta_j[0]) for r in capture)


def get_moves_rook(board_size, piece, pieces):
    """Returns the available moves of the given rook in the given board"""
    check_moves_args(board_size, piece, pieces, "R")
    return []


def get_moves_knight(board_size, piece, pieces):
    """Returns the available moves of the given knight in the given board"""
    check_moves_args(board_size, piece, pieces, "N")
    return []


def get_moves_bishop(board_size, piece, pieces):
    """Returns the available moves of the given bishop in the given board"""
    check_moves_args(board_size, piece, pieces, "B")
    return []


def get_moves_queen(board_size, piece, pieces):
    """Returns the available moves of the given queen in the given board"""
    check_moves_args(board_size, piece, pieces, "Q")
    return []


def get_moves_king(board_size, piece, pieces):
    """Returns the available moves of the given king in the given board"""
    check_moves_args(board_size, piece, pieces, "K")
    return []
