from color import Color
from moves import get_moves_queen
from piece import Piece
from tests.base import assert_same_move


def test_queen_free() -> None:
    """Tests the available rules of a queen with full free space"""
    piece = Piece(Color.WHITE, "Q", 3, 4, False)
    result = get_moves_queen(8, piece, {piece})
    expected = [
        "Qd5", "Qe6", "Qf7", "Qg8", "Qd3", "Qe2", "Qf1", "Qb5", "Qa6", "Qb3", "Qa2", "Qa4", "Qb4", "Qd4", "Qe4",
        "Qf4", "Qg4", "Qh4", "Qc1", "Qc2", "Qc3", "Qc5", "Qc6", "Qc7", "Qc8"]
    assert_same_move(expected, result)


def test_queen_friendly() -> None:
    """Tests the available rules of a queen with a friendly pawn that stops it"""
    piece = Piece(Color.WHITE, "Q", 3, 4, False)
    friend = Piece(Color.WHITE, "P", 5, 6, False)
    result = get_moves_queen(8, piece, {piece, friend})
    expected = [
        "Qd5", "Qd3", "Qe2", "Qf1", "Qb5", "Qa6", "Qb3", "Qa2", "Qa4", "Qb4", "Qd4", "Qe4",
        "Qf4", "Qg4", "Qh4", "Qc1", "Qc2", "Qc3", "Qc5", "Qc6", "Qc7", "Qc8"]
    assert_same_move(expected, result)


def test_queen_enemy() -> None:
    """Tests the available rules of a queen with an enemy pawn that stops it"""
    piece = Piece(Color.WHITE, "Q", 3, 4, False)
    enemy = Piece(Color.BLACK, "P", 5, 6, False)
    result = get_moves_queen(8, piece, {piece, enemy})
    expected = [
        "Qd5", "Qxe6", "Qd3", "Qe2", "Qf1", "Qb5", "Qa6", "Qb3", "Qa2", "Qa4", "Qb4", "Qd4", "Qe4",
        "Qf4", "Qg4", "Qh4", "Qc1", "Qc2", "Qc3", "Qc5", "Qc6", "Qc7", "Qc8"]
    assert_same_move(expected, result)
