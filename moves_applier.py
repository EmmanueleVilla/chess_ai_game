from move import Move
from piece import Piece


def apply_move(pieces: [Piece], move: Move):
    """Applies the given move to the pieces and returns the new configuration"""
    remove = [move.piece.coord, move.coord]
    add = Piece(move.piece.color, move.piece.name, move.coord.i, move.coord.j, True)
    return [piece for piece in pieces if piece.coord not in remove] + [add]
