from board import search_by_indexes


def get_moves(piece, pieces):
    """Returns the available moves of the given piece in the given board"""
    switcher = {
        "P": get_moves_pawn,
        "R": get_moves_rook,
        "N": get_moves_knight,
        "B": get_moves_bishop,
        "Q": get_moves_queen,
        "K": get_moves_king
    }

    return switcher[piece.name](piece, pieces)


def check_args(piece, pieces, name):
    """Checks if the arguments are legal"""
    assert piece in pieces
    assert piece.name == name


def get_moves_pawn(piece, pieces):
    """Returns the available moves of the given pawn in the given board"""
    check_args(piece, pieces, "P")

    # Forward direction
    direction = 1
    if piece.color == "B":
        direction = -1
    delta = [direction]
    if not piece.moved:
        delta.append(direction * 2)
    result = [d for d in delta if search_by_indexes(pieces, piece.i(), d) is not None]

    # Todo: check diagonal piece capture
    # Todo: check en-passant capture
    return (append_piece(piece, r) for r in result)


def append_piece(piece, cell_j):
    """Joins the piece information and the arrival cell"""
    return f'{piece.name}{piece.i_as_letter()}{piece.j()}{piece.i_as_letter()}{cell_j}'


def get_moves_rook(piece, pieces):
    """Returns the available moves of the given rook in the given board"""
    check_args(piece, pieces, "R")
    return []


def get_moves_knight(piece, pieces):
    """Returns the available moves of the given knight in the given board"""
    check_args(piece, pieces, "N")
    return []


def get_moves_bishop(piece, pieces):
    """Returns the available moves of the given bishop in the given board"""
    check_args(piece, pieces, "B")
    return []


def get_moves_queen(piece, pieces):
    """Returns the available moves of the given queen in the given board"""
    check_args(piece, pieces, "Q")
    return []


def get_moves_king(piece, pieces):
    """Returns the available moves of the given king in the given board"""
    check_args(piece, pieces, "K")
    return []
