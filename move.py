from castling import Castling
from check import Check
from piece import to_letter, Piece


class Move:
    """Represents a move on the board"""

    def __init__(self, piece: Piece, i: int, j: int, is_capture: bool, check: Check = Check.NONE, promotion: str = "",
                 castling: Castling = Castling.NONE):
        self.piece = piece
        self.i = i
        self.j = j
        self.is_capture = is_capture
        self.check = check
        self.print_i = False
        self.print_j = False
        self.promotion = promotion
        self.castling = castling
        self.an_string = self.__to_an()

    def set_print_i(self, print_i: bool) -> None:
        """Set the print i value"""
        self.print_i = print_i
        self.an_string = self.__to_an()

    def set_print_j(self, print_j: bool) -> None:
        """Set the print i value"""
        self.print_j = print_j
        self.an_string = self.__to_an()

    def __to_an(self) -> str:
        """Returns the "an" representation of this move"""
        if self.castling == Castling.KING_SIDE:
            return "O-O"
        if self.castling == Castling.QUEEN_SIDE:
            return "O-O-0"
        output = self.piece.name if self.piece.name != "P" else ""
        output += to_letter(self.piece.i) if self.print_i or (self.piece.name == "P" and self.is_capture) else ""
        output += f'{self.piece.j}' if self.print_j else ""
        output += "x" if self.is_capture else ""
        output += to_letter(self.i)
        output += f'{self.j}'
        output += f'={self.promotion}' if self.promotion != "" else ""
        output += "+" if self.check == Check.CHECK else ""
        output += "#" if self.check == Check.CHECKMATE else ""
        return output


def copy_move_edit_check(original: Move, check: Check) -> Move:
    """Copy the given move modifying the check value"""
    return Move(original.piece, original.i, original.j, original.is_capture, check, original.promotion)


def copy_move_edit_promotion(original: Move, promotion: str) -> Move:
    """Copy the given move modifying the check value"""
    return Move(original.piece, original.i, original.j, original.is_capture, original.check, promotion)
