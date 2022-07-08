from colors import COLOR_BLUE, COLOR_GREEN
from piece import Piece

BOARD_SIZE = 8

def build_pieces():
    """Builds the starting game pieces"""
    letters = ["T","N","B","K","Q","B","N","T"]
    output = []
    for i in range(8):
        output.append(Piece(COLOR_BLUE, letters[i], 0, i))
    for i in range(8):
        output.append(Piece(COLOR_BLUE, "P", 1, i))
    for i in range(8):
        output.append(Piece(COLOR_GREEN, "P", 6, i))
    for i in range(8):
        output.append(Piece(COLOR_GREEN, letters[i], 7, i))
    return output

def search_by_indexes(pieces, i,j):
    """Searches for the piece at the given coordinates"""
    for piece in pieces:
        if(piece.i() == i) and (piece.j() == j):
            return piece
    return None
