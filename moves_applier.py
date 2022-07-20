from typing import Set

from castling import Castling
from color import Color
from move import Move
from piece import Piece


def apply_move(pieces: Set[Piece], move: Move) -> Set[Piece]:
    """Applies the given move to the pieces and returns the new configuration"""
    remove = [(move.piece.i, move.piece.j)]
    add = []
    if move.castling == Castling.NONE:
        remove.append((move.i, move.j))
        add.append(Piece(move.piece.color, move.promotion if move.promotion != "" else move.piece.name, move.i,
                         move.j, True))
    else:
        j = 1 if move.piece.color == Color.WHITE else 8
        king_i = 1 if move.castling == Castling.QUEEN_SIDE else 8
        remove.append((king_i, j))
        king_new_i = 3 if move.castling == Castling.QUEEN_SIDE else 7
        add.append(Piece(move.piece.color, move.piece.name, king_new_i, j, True))
        rook_delta_from_king = 1 if move.castling == Castling.QUEEN_SIDE else -1
        add.append(Piece(move.piece.color, "R", king_new_i + rook_delta_from_king, j, True))

    return set([piece for piece in pieces if (piece.i, piece.j) not in remove] + add)
