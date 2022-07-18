from move import Move
from moves_applier import apply_move
from piece import Piece
from tests.base import assert_same_pieces


def test_move_with_catch():
    """Tests the board update after a catch move"""
    pieces = [
        Piece("W", "A", 0, 0, False),
        Piece("B", "B", 1, 0, False)
    ]
    move = Move(pieces[0], 1, 0, True)
    expected = [
        Piece("W", "A", 1, 0, False)
    ]
    result = apply_move(pieces, move)
    assert_same_pieces(expected, result)