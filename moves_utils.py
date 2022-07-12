from board import search_by_indexes
from move import Move
from piece import Piece


def get_moves_with_direction(board_size: int, piece: Piece, pieces: [Piece], delta_i: int, delta_j: int,
                             stop_on_count: int, stop_on_enemy=False, only_on_enemy=False):
    """Calculate the possible moves in the given direction,
    moving by the given delta and stopping at the given conditions."""
    output = []
    i = piece.i()
    j = piece.j()
    for _ in range(stop_on_count):
        i += delta_i
        j += delta_j
        if i > board_size or j > board_size or i < 1 or j < 1:
            break
        occupier = search_by_indexes(pieces, i, j)
        if occupier is not None:
            if occupier.color == piece.color or stop_on_enemy:
                break
            output.append(Move(piece, i, j, True))
            break
        if occupier is None and only_on_enemy:
            break
        output.append(Move(piece, i, j, False))
    return output
