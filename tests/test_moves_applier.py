from color import Color
from move import Move
from moves_applier import apply_move
from piece import Piece
from tests.base import assert_same_pieces


def test_move_with_catch() -> None:
    """Tests the board update after a catch move"""
    piece = Piece(Color.WHITE, "A", 0, 0, False)
    pieces = {
        piece,
        Piece(Color.BLACK, "B", 1, 0, False)
    }
    move = Move(piece, 1, 0, True)
    expected = {
        Piece(Color.WHITE, "A", 1, 0, False)
    }
    result = apply_move(pieces, move)
    assert_same_pieces(expected, result)
