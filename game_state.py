from typing import List, Set

from color import Color
from move import Move
from piece import Piece


class GameState:
    """Represents the game state"""

    def __init__(self, board_size: int, turn_number: int, turn_color: Color, pieces: Set[Piece], moves: List[Move]):
        self.board_size = board_size
        self.turn_number = turn_number
        self.turn_color = turn_color
        self.pieces = pieces
        self.moves = moves

    def __str__(self) -> str:
        """output format"""
        output = ""
        output += "board_size\n"
        output += f'{self.board_size}\n'
        output += "turn_number\n"
        output += f'{self.turn_number}\n'
        output += "turn_color\n"
        output += f'{self.turn_color}\n'
        output += "pieces\n"
        for piece in self.pieces:
            output += f'{piece.__str__()}\n'
        output += "moves\n"
        for move in self.moves:
            output += f'{move.an_string}\n'
        return output
