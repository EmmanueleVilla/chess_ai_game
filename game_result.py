from typing import Set

from piece import Piece


class GameResult:
    """Represents the game result"""

    def __init__(self, white: float, black: float, message: str, pieces: Set[Piece]):
        self.white = white
        self.black = black
        self.message = message
        self.pieces = pieces

    def get_white(self) -> str:
        """Return the string representation of the points"""
        if self.white == 0.5:
            return "1/2"

        return f'{self.white}'

    def get_black(self) -> str:
        """Return the string representation of the points"""
        if self.black == 0.5:
            return "1/2"

        return f'{self.black}'
