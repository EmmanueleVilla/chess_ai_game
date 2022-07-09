def get_moves(piece, pieces):
    """Returns the available moves of the given piece in the given board"""
    switcher = {
        "P": get_moves_pawn(piece, pieces),
        "T": get_moves_tower(piece, pieces),
        "N": get_moves_knight(piece, pieces),
        "B": get_moves_bishop(piece, pieces),
        "Q": get_moves_queen(piece, pieces),
        "K": get_moves_king(piece, pieces)
    }

    return switcher[piece.name]


def check_args(piece, pieces, name):
    """Checks if the arguments are legal"""
    assert piece in pieces
    assert piece.name == name


def get_moves_pawn(piece, pieces):
    """Returns the available moves of the given pawn in the given board"""
    check_args(piece, pieces, "P")
    return []


def get_moves_tower(piece, pieces):
    """Returns the available moves of the given tower in the given board"""
    check_args(piece, pieces, "T")
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
