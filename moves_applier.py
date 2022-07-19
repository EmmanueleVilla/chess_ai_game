from typing import Set

from move import Move
from piece import Piece


def apply_move(pieces: Set[Piece], move: Move) -> Set[Piece]:
    """Applies the given move to the pieces and returns the new configuration"""
    remove = [(move.piece.i, move.piece.j), (move.i, move.j)]
    add = Piece(move.piece.color, move.promotion if move.promotion != "" else move.piece.name, move.i,
                move.j, True)
    return set([piece for piece in pieces if (piece.i, piece.j) not in remove] + [add])
