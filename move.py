from castling import Castling
from check import Check
from color import Color
from piece import to_letter, Piece


class Move:
    """Represents a move on the board"""

    # pylint: disable=too-many-instance-attributes
    # I may refactor this one day, but all those attributes are needed for a move description

    def __init__(self, piece: Piece, i: int, j: int, is_capture: bool, check: Check, promotion: str,
                 castling: Castling, en_passant: Piece):
        self.piece = piece
        self.i = i
        self.j = j
        self.is_capture = is_capture or en_passant.name != ""
        self.check = check
        self.print_i = False
        self.print_j = False
        self.promotion = promotion
        self.castling = castling
        self.en_passant = en_passant
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
        output += " e.p." if self.en_passant.name != "" else ""
        output += f'={self.promotion}' if self.promotion != "" else ""
        output += "+" if self.check == Check.CHECK else ""
        output += "#" if self.check == Check.CHECKMATE else ""
        return output


def build_move(piece: Piece, i: int, j: int, is_capture: bool) -> Move:
    """Creates a Move object with some default parameters"""
    return Move(piece, i, j, is_capture, Check.NONE, "", Castling.NONE, Piece(Color.WHITE, "", -1, -1))


def copy_move_edit_check(original: Move, check: Check) -> Move:
    """Copy the given move modifying the check value"""
    return Move(original.piece, original.i, original.j, original.is_capture, check, original.promotion,
                original.castling, original.en_passant)


def copy_move_edit_promotion(original: Move, promotion: str) -> Move:
    """Copy the given move modifying the promotion value"""
    return Move(original.piece, original.i, original.j, original.is_capture, original.check, promotion,
                original.castling, original.en_passant)


def copy_move_edit_castling(original: Move, castling: Castling) -> Move:
    """Copy the given move modifying the castling value"""
    return Move(original.piece, original.i, original.j, original.is_capture, original.check, original.promotion,
                castling, original.en_passant)


def copy_move_edit_en_passant(original: Move, en_passant: Piece) -> Move:
    """Copy the given move modifying the en_passant value"""
    return Move(original.piece, original.i, original.j, original.is_capture, original.check, original.promotion,
                original.castling, en_passant)
