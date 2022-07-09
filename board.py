from piece import Piece


def build_pieces(board_size):
    """Builds the starting game pieces"""
    assert board_size == 8
    letters = ["T", "N", "B", "K", "Q", "B", "N", "T"]
    output = []
    for i in range(board_size):
        output.append(Piece("B", letters[i], 0, i))
    for i in range(board_size):
        output.append(Piece("B", "P", 1, i))
    for i in range(board_size):
        output.append(Piece("W", "P", board_size - 2, i))
    for i in range(board_size):
        output.append(Piece("W", letters[i], board_size - 1, i))
    return output


def search_by_indexes(pieces, i, j):
    """Searches for the piece at the given coordinates"""
    for piece in pieces:
        if (piece.i() == i) and (piece.j() == j):
            return piece
    return None
