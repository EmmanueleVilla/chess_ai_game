from typing import List

from board import search_by_indexes
from color import Color
from piece import Piece


def print_board(board_size: int, pieces: List[Piece]) -> None:
    """Prints the board"""
    print(board_to_string(board_size, pieces))


def board_to_string(board_size: int, pieces: List[Piece]) -> str:
    """Returns a string representation of the board"""
    result: str = ""
    gray = '\033[90m'
    white = '\033[0m'
    color_map = {
        Color.BLACK: '\033[94m',
        Color.WHITE: '\033[92m'
    }
    for j in reversed(range(1, board_size + 1)):
        result += f'{gray}[{j}]{white}'
        for i in range(1, board_size + 1):
            piece = search_by_indexes(pieces, i, j)
            output = "["
            if piece is not None:
                output += color_map[piece.color]
                output += piece.name
                output += white
            else:
                output += " "
            output += "]"
            result += output
        result += "\n"
    result += gray + "   [a][b][c][d][e][f][g][h]" + white
    return result
