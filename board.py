from typing import List, Union

from color import Color
from piece import Piece


def build_pieces(board_size: int) -> List[Piece]:
    """Builds the starting game pieces"""
    assert board_size == 8
    letters = ["R", "N", "B", "Q", "K", "B", "N", "R"]
    output = []
    for i in range(1, board_size + 1):
        output.append(Piece(Color.WHITE, letters[i - 1], i, 1))
    for i in range(1, board_size + 1):
        output.append(Piece(Color.WHITE, "P", i, 2))
    for i in range(1, board_size + 1):
        output.append(Piece(Color.BLACK, "P", i, board_size - 1))
    for i in range(1, board_size + 1):
        output.append(Piece(Color.BLACK, letters[i - 1], i, board_size))
    return output


def search_by_indexes(pieces: List[Piece], i: int, j: int) -> Union[Piece, None]:
    """Searches for the piece at the given coordinates"""
    for piece in pieces:
        if (piece.i == i) and (piece.j == j):
            return piece
    return None
