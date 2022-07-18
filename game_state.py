from typing import List

from color import Color
from move import Move
from piece import Piece


class GameState:
    """Represents the game state"""

    def __init__(self, board_size: int, turn_number: int, turn_color: Color, pieces: List[Piece], moves: List[Move]):
        self.board_size = board_size
        self.turn_number = turn_number
        self.turn_color = turn_color
        self.pieces = pieces
        self.moves = moves
