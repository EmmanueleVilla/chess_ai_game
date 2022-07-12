from moves_single import get_moves_king
from piece import Piece
from tests.base import assert_same_array


def test_king_free():
    """Tests the available rules of a king with full free space"""
    piece = Piece("W", "K", 3, 4, False)
    result = get_moves_king(8, piece, [piece])
    expected = ["Kb3", "Kb4", "Kb5", "Kc3", "Kc5", "Kd3", "Kd4", "Kd5"]
    assert_same_array(expected, result)


def test_king_friendly():
    """Tests the available rules of a king with a friendly pawn that stops it"""
    piece = Piece("W", "K", 3, 4, False)
    friend = Piece("W", "P", 4, 5, False)
    result = get_moves_king(8, piece, [piece, friend])
    expected = ["Kb3", "Kb4", "Kb5", "Kc3", "Kc5", "Kd3", "Kd4"]
    assert_same_array(expected, result)


def test_king_enemy():
    """Tests the available rules of a king with an enemy pawn that stops it"""
    piece = Piece("W", "K", 3, 4, False)
    enemy = Piece("B", "P", 4, 5, False)
    result = get_moves_king(8, piece, [piece, enemy])
    expected = ["Kb3", "Kb4", "Kb5", "Kc3", "Kc5", "Kd3", "Kd4", "Kxd5"]
    assert_same_array(expected, result)
