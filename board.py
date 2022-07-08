from colors import colors
from piece import Piece

BOARD_SIZE = 8

PIECES = [
    Piece(colors.BLUE, "T", 0, 0),
    Piece(colors.BLUE, "N", 0, 1),
    Piece(colors.BLUE, "B", 0, 2),
    Piece(colors.BLUE, "K", 0, 3),
    Piece(colors.BLUE, "Q", 0, 4),
    Piece(colors.BLUE, "B", 0, 5),
    Piece(colors.BLUE, "N", 0, 6),
    Piece(colors.BLUE, "T", 0, 7),
    Piece(colors.BLUE, "P", 1, 0),
    Piece(colors.BLUE, "P", 1, 1),
    Piece(colors.BLUE, "P", 1, 2),
    Piece(colors.BLUE, "P", 1, 3),
    Piece(colors.BLUE, "P", 1, 4),
    Piece(colors.BLUE, "P", 1, 5),
    Piece(colors.BLUE, "P", 1, 6),
    Piece(colors.BLUE, "P", 1, 7),
    Piece(colors.GREEN, "P", 6, 0),
    Piece(colors.GREEN, "P", 6, 1),
    Piece(colors.GREEN, "P", 6, 2),
    Piece(colors.GREEN, "P", 6, 3),
    Piece(colors.GREEN, "P", 6, 4),
    Piece(colors.GREEN, "P", 6, 5),
    Piece(colors.GREEN, "P", 6, 6),
    Piece(colors.GREEN, "P", 6, 7),
    Piece(colors.GREEN, "T", 7, 0),
    Piece(colors.GREEN, "N", 7, 1),
    Piece(colors.GREEN, "B", 7, 2),
    Piece(colors.GREEN, "K", 7, 3),
    Piece(colors.GREEN, "Q", 7, 4),
    Piece(colors.GREEN, "B", 7, 5),
    Piece(colors.GREEN, "N", 7, 6),
    Piece(colors.GREEN, "T", 7, 7),
]

def search_by_indexes(i,j):
    for piece in PIECES:
        if(piece.i() == i) and (piece.j() == j):
            return piece
    return None