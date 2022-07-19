from color import Color
from moves import get_moves_king
from piece import Piece
from tests.base import assert_same_move


def test_king_free() -> None:
    """Tests the available rules of a king with full free space"""
    piece = Piece(Color.WHITE, "K", 3, 4, False)
    result = get_moves_king(8, piece, {piece}, False)
    expected = ["Kb3", "Kb4", "Kb5", "Kc3", "Kc5", "Kd3", "Kd4", "Kd5"]
    assert_same_move(expected, result)


def test_king_friendly() -> None:
    """Tests the available rules of a king with a friendly pawn that stops it"""
    piece = Piece(Color.WHITE, "K", 3, 4, False)
    friend = Piece(Color.WHITE, "P", 4, 5, False)
    result = get_moves_king(8, piece, {piece, friend}, False)
    expected = ["Kb3", "Kb4", "Kb5", "Kc3", "Kc5", "Kd3", "Kd4"]
    assert_same_move(expected, result)


def test_king_enemy() -> None:
    """Tests the available rules of a king with an enemy pawn that stops it"""
    piece = Piece(Color.WHITE, "K", 3, 4, False)
    enemy = Piece(Color.BLACK, "P", 4, 5, False)
    result = get_moves_king(8, piece, {piece, enemy}, False)
    expected = ["Kb3", "Kb4", "Kb5", "Kc3", "Kc5", "Kd3", "Kd4", "Kxd5"]
    assert_same_move(expected, result)
