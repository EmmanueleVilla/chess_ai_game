from check import Check
from coord import Coord
from piece import to_letter, Piece


class Move:
    """Represents a move on the board"""

    def __init__(self, piece: Piece, i: int, j: int, is_capture: bool, check: Check = Check.NONE, promotion: str = ""):
        self.piece = piece
        self.coord = Coord(i, j)
        self.is_capture = is_capture
        self.check = check
        self.print_i = False
        self.print_j = False
        self.promotion = promotion

    def to_an(self) -> str:
        """Returns the "an" representation of this move"""
        output = self.piece.name if self.piece.name != "P" else ""
        output += to_letter(self.piece.i()) if self.print_i or (self.piece.name == "P" and self.is_capture) else ""
        output += f'{self.piece.coord.j}' if self.print_j else ""
        output += "x" if self.is_capture else ""
        output += to_letter(self.coord.i)
        output += f'{self.coord.j}'
        output += f'={self.promotion}' if self.promotion != "" else ""
        output += "+" if self.check == Check.CHECK else ""
        output += "#" if self.check == Check.CHECKMATE else ""
        return output


def copy_move_edit_check(original: Move, check: Check) -> Move:
    """Copy the given move modifying the check value"""
    return Move(original.piece, original.coord.i, original.coord.j, original.is_capture, check, original.promotion)


def copy_move_edit_promotion(original: Move, promotion: str) -> Move:
    """Copy the given move modifying the check value"""
    return Move(original.piece, original.coord.i, original.coord.j, original.is_capture, original.check, promotion)
