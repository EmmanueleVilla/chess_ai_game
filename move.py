from coord import Coord
from piece import to_letter


class Move:
    """Represents a move on the board"""

    def __init__(self, piece, i, j, is_capture):
        self.piece = piece
        self.coord = Coord(i, j)
        self.is_capture = is_capture

    def to_an(self):
        """Returns the "an" representation of this move"""
        output = self.piece.name if self.piece.name != "P" else ""
        output += to_letter(self.piece.i()) if self.piece.name == "P" and self.is_capture else ""
        output += "x" if self.is_capture else ""
        output += to_letter(self.coord.i)
        output += f'{self.coord.j}'
        return output
