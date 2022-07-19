from typing import List

from move import Move
from piece import Piece


def apply_move(pieces: List[Piece], move: Move) -> List[Piece]:
    """Applies the given move to the pieces and returns the new configuration"""
    remove = [move.piece.coord, move.coord]
    add = Piece(move.piece.color, move.promotion if move.promotion != "" else move.piece.name, move.coord.i,
                move.coord.j, True)
    return [piece for piece in pieces if piece.coord not in remove] + [add]
