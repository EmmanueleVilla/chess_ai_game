from moves_global import get_moves_pawn
from piece import Piece
from utils import print_board


def test_pawn_start_catch_right_white():
    """Tests the available rules of a pawn that never moved before"""
    piece = Piece("W", "P", 1, 2, False)
    enemy = Piece("B", "P", 2, 3, False)
    print_board(8, [piece, enemy])
    result = get_moves_pawn(8, piece, [piece, enemy])
    assert len(result) == 3
    assert "Pa2a3" in result
    assert "Pa2a4" in result
    assert "Pa2b3" in result
