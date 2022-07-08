from colors import COLOR_BLUE, COLOR_GREEN
from piece import Piece

BOARD_SIZE = 8

def buildPieces():
    """Builds the starting game pieces"""
    return [
    Piece(COLOR_BLUE, "T", 0, 0),
    Piece(COLOR_BLUE, "N", 0, 1),
    Piece(COLOR_BLUE, "B", 0, 2),
    Piece(COLOR_BLUE, "K", 0, 3),
    Piece(COLOR_BLUE, "Q", 0, 4),
    Piece(COLOR_BLUE, "B", 0, 5),
    Piece(COLOR_BLUE, "N", 0, 6),
    Piece(COLOR_BLUE, "T", 0, 7),
    Piece(COLOR_BLUE, "P", 1, 0),
    Piece(COLOR_BLUE, "P", 1, 1),
    Piece(COLOR_BLUE, "P", 1, 2),
    Piece(COLOR_BLUE, "P", 1, 3),
    Piece(COLOR_BLUE, "P", 1, 4),
    Piece(COLOR_BLUE, "P", 1, 5),
    Piece(COLOR_BLUE, "P", 1, 6),
    Piece(COLOR_BLUE, "P", 1, 7),
    Piece(COLOR_GREEN, "P", 6, 0),
    Piece(COLOR_GREEN, "P", 6, 1),
    Piece(COLOR_GREEN, "P", 6, 2),
    Piece(COLOR_GREEN, "P", 6, 3),
    Piece(COLOR_GREEN, "P", 6, 4),
    Piece(COLOR_GREEN, "P", 6, 5),
    Piece(COLOR_GREEN, "P", 6, 6),
    Piece(COLOR_GREEN, "P", 6, 7),
    Piece(COLOR_GREEN, "T", 7, 0),
    Piece(COLOR_GREEN, "N", 7, 1),
    Piece(COLOR_GREEN, "B", 7, 2),
    Piece(COLOR_GREEN, "K", 7, 3),
    Piece(COLOR_GREEN, "Q", 7, 4),
    Piece(COLOR_GREEN, "B", 7, 5),
    Piece(COLOR_GREEN, "N", 7, 6),
    Piece(COLOR_GREEN, "T", 7, 7),
]

def search_by_indexes(pieces, i,j):
    """Searches for the piece at the given coordinates"""
    for piece in pieces:
        if(piece.i() == i) and (piece.j() == j):
            return piece
    return None
