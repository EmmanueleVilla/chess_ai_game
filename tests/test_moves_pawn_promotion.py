from color import Color
from moves_applier import apply_move
from moves import get_moves_pawn
from piece import Piece
from tests.base import assert_same_move


def test_pawn_promotion_white_move() -> None:
    """Tests the available rules of a pawn that can be promoted"""
    piece = Piece(Color.WHITE, "P", 1, 7, False)
    pieces = set()
    pieces.add(piece)
    result = get_moves_pawn(8, piece, pieces)
    expected = ["a8=Q", "a8=N", "a8=R", "a8=B"]
    assert_same_move(expected, result)


def test_pawn_promotion_white_applied() -> None:
    """Tests the application of the pawn promotion"""
    piece = Piece(Color.WHITE, "P", 1, 7, False)
    pieces = set()
    pieces.add(piece)
    result = get_moves_pawn(8, piece, pieces)
    pieces = apply_move(pieces, result[0])
    assert len(pieces) == 1
    assert next(iter(pieces)).name == "Q"


def test_pawn_promotion_black() -> None:
    """Tests the available rules of a pawn that can be promoted"""
    piece = Piece(Color.BLACK, "P", 1, 2, False)
    pieces = set()
    pieces.add(piece)
    result = get_moves_pawn(8, piece, pieces)
    expected = ["a1=Q", "a1=N", "a1=R", "a1=B"]
    assert_same_move(expected, result)
