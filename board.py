from piece import Piece


def build_pieces(board_size):
    """Builds the starting game pieces"""
    assert board_size == 8
    letters = ["", "T", "N", "B", "Q", "K", "B", "N", "T"]
    output = []
    for i in range(1, board_size + 1):
        output.append(Piece("W", letters[i], 1, i))
    for i in range(1, board_size + 1):
        output.append(Piece("W", "P", 2, i))
    for i in range(1, board_size + 1):
        output.append(Piece("B", "P", board_size - 1, i))
    for i in range(1, board_size + 1):
        output.append(Piece("B", letters[i], board_size, i))
    return output


def search_by_indexes(pieces, i, j):
    """Searches for the piece at the given coordinates"""
    for piece in pieces:
        if (piece.i() == i) and (piece.j() == j):
            return piece
    return None
