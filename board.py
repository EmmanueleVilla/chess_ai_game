from colors import Colors
from piece import Piece

BOARD_SIZE = 8

PIECES = [
    Piece(Colors.BLUE, "T", 0, 0),
    Piece(Colors.BLUE, "N", 0, 1),
    Piece(Colors.BLUE, "B", 0, 2),
    Piece(Colors.BLUE, "K", 0, 3),
    Piece(Colors.BLUE, "Q", 0, 4),
    Piece(Colors.BLUE, "B", 0, 5),
    Piece(Colors.BLUE, "N", 0, 6),
    Piece(Colors.BLUE, "T", 0, 7),
    Piece(Colors.BLUE, "P", 1, 0),
    Piece(Colors.BLUE, "P", 1, 1),
    Piece(Colors.BLUE, "P", 1, 2),
    Piece(Colors.BLUE, "P", 1, 3),
    Piece(Colors.BLUE, "P", 1, 4),
    Piece(Colors.BLUE, "P", 1, 5),
    Piece(Colors.BLUE, "P", 1, 6),
    Piece(Colors.BLUE, "P", 1, 7),
    Piece(Colors.GREEN, "P", 6, 0),
    Piece(Colors.GREEN, "P", 6, 1),
    Piece(Colors.GREEN, "P", 6, 2),
    Piece(Colors.GREEN, "P", 6, 3),
    Piece(Colors.GREEN, "P", 6, 4),
    Piece(Colors.GREEN, "P", 6, 5),
    Piece(Colors.GREEN, "P", 6, 6),
    Piece(Colors.GREEN, "P", 6, 7),
    Piece(Colors.GREEN, "T", 7, 0),
    Piece(Colors.GREEN, "N", 7, 1),
    Piece(Colors.GREEN, "B", 7, 2),
    Piece(Colors.GREEN, "K", 7, 3),
    Piece(Colors.GREEN, "Q", 7, 4),
    Piece(Colors.GREEN, "B", 7, 5),
    Piece(Colors.GREEN, "N", 7, 6),
    Piece(Colors.GREEN, "T", 7, 7),
]

def search_by_indexes(i,j):
    """Searches for the piece at the given coordinates"""
    for piece in PIECES:
        if(piece.i() == i) and (piece.j() == j):
            return piece
    return None
