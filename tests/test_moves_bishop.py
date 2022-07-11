from moves import get_moves_bishop
from piece import Piece
from tests.base import assert_same_array


def test_bishop_free():
    """Tests the available rules of a bishop with full free space"""
    piece = Piece("W", "B", 3, 4, False)
    result = get_moves_bishop(8, piece, [piece])
    expected = ["Bd5", "Be6", "Bf7", "Bg8", "Bd3", "Be2", "Bf1", "Bb5", "Ba6", "Bb3", "Ba2"]
    assert_same_array(result, expected)


def test_bishop_friendly():
    """Tests the available rules of a bishop with a friendly pawn that stops it"""
    piece = Piece("W", "B", 3, 4, False)
    friend = Piece("W", "P", 5, 6, False)
    result = get_moves_bishop(8, piece, [piece, friend])
    expected = ["Bd5", "Bd3", "Be2", "Bf1", "Bb5", "Ba6", "Bb3", "Ba2"]
    assert_same_array(result, expected)


def test_bishop_enemy():
    """Tests the available rules of a bishop with an enemy pawn that stops it"""
    piece = Piece("W", "B", 3, 4, False)
    enemy = Piece("B", "P", 5, 6, False)
    result = get_moves_bishop(8, piece, [piece, enemy])
    expected = ["Bd5", "Bxe6", "Bd3", "Be2", "Bf1", "Bb5", "Ba6", "Bb3", "Ba2"]
    assert_same_array(result, expected)
