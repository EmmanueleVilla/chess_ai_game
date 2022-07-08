from colors import COLOR_BLUE, COLOR_GREEN
from piece import Piece

def build_pieces(BOARD_SIZE):
    """Builds the starting game pieces"""
    assert BOARD_SIZE == 8
    letters = ["T","N","B","K","Q","B","N","T"]
    output = []
    for i in range(BOARD_SIZE):
        output.append(Piece(COLOR_BLUE, letters[i], 0, i))
    for i in range(BOARD_SIZE):
        output.append(Piece(COLOR_BLUE, "P", 1, i))
    for i in range(BOARD_SIZE):
        output.append(Piece(COLOR_GREEN, "P", BOARD_SIZE - 2, i))
    for i in range(BOARD_SIZE):
        output.append(Piece(COLOR_GREEN, letters[i], BOARD_SIZE - 1, i))
    return output

def search_by_indexes(pieces, i,j):
    """Searches for the piece at the given coordinates"""
    for piece in pieces:
        if(piece.i() == i) and (piece.j() == j):
            return piece
    return None
