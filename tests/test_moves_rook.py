from color import Color
from moves import get_moves_rook
from piece import Piece
from tests.base import assert_same_move


def test_rook_free() -> None:
    """Tests the available rules of a rook with full free space"""
    piece = Piece(Color.WHITE, "R", 4, 6, False)
    result = get_moves_rook(8, piece, {piece})
    expected = ["Rd7", "Rd8", "Rd5", "Rd4", "Rd3", "Rd2", "Rd1", "Re6", "Rf6", "Rg6", "Rh6", "Rc6", "Rb6", "Ra6"]
    assert_same_move(expected, result)


def test_rook_friendly() -> None:
    """Tests the available rules of a rook with a friendly pawn that stops it"""
    piece = Piece(Color.WHITE, "R", 4, 6, False)
    friend = Piece(Color.WHITE, "P", 2, 6, False)
    result = get_moves_rook(8, piece, {piece, friend})
    expected = ["Rd7", "Rd8", "Rd5", "Rd4", "Rd3", "Rd2", "Rd1", "Re6", "Rf6", "Rg6", "Rh6", "Rc6"]
    assert_same_move(expected, result)


def test_rook_enemy() -> None:
    """Tests the available rules of a rook with an enemy pawn that stops it"""
    piece = Piece(Color.WHITE, "R", 4, 6, False)
    enemy = Piece(Color.BLACK, "P", 2, 6, False)
    result = get_moves_rook(8, piece, {piece, enemy})
    expected = ["Rd7", "Rd8", "Rd5", "Rd4", "Rd3", "Rd2", "Rd1", "Re6", "Rf6", "Rg6", "Rh6", "Rc6", "Rxb6"]
    assert_same_move(expected, result)
