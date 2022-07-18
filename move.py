from typing import TypeVar

from check import Check
from coord import Coord
from piece import to_letter, Piece

SelfMove = TypeVar("SelfMove", bound="Move")


class Move:
    """Represents a move on the board"""

    def __init__(self, piece: Piece, i: int, j: int, is_capture: bool, check: Check = Check.NONE):
        self.piece = piece
        self.coord = Coord(i, j)
        self.is_capture = is_capture
        self.check = check

    def to_an(self):
        """Returns the "an" representation of this move"""
        output = self.piece.name if self.piece.name != "P" else ""
        output += to_letter(self.piece.i()) if self.piece.name == "P" and self.is_capture else ""
        output += "x" if self.is_capture else ""
        output += to_letter(self.coord.i)
        output += f'{self.coord.j}'
        output += "+" if self.check == Check.CHECK else ""
        output += "#" if self.check == Check.CHECKMATE else ""
        return output

    def copy(self, check: Check = Check.NONE) -> SelfMove:
        """Copy the given move modifying the check value"""
        return Move(self.piece, self.coord.i, self.coord.j, self.is_capture, check)
