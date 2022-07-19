from color import Color
from moves_global import get_all_moves
from piece import Piece


def test_ambiguous_move_same_i() -> None:
    """Tests the moves ambiguities"""
    pieces = [
        Piece(Color.WHITE, "R", 4, 8),
        Piece(Color.WHITE, "R", 8, 8)
    ]

    result = get_all_moves(8, pieces, Color.WHITE)
    assert "Rde8" in [move.an_string for move in result]
    assert "Rhe8" in [move.an_string for move in result]


def test_ambiguous_move_same_j() -> None:
    """Tests the moves ambiguities"""
    pieces = [
        Piece(Color.WHITE, "R", 1, 1),
        Piece(Color.WHITE, "R", 1, 5)
    ]

    result = get_all_moves(8, pieces, Color.WHITE)
    assert "R1a2" in [move.an_string for move in result]
    assert "R5a2" in [move.an_string for move in result]


def test_ambiguous_move_same_i_j() -> None:
    """Tests the moves ambiguities"""
    pieces = [
        Piece(Color.WHITE, "Q", 5, 4),
        Piece(Color.WHITE, "Q", 8, 1),
        Piece(Color.WHITE, "Q", 8, 4)
    ]

    result = get_all_moves(8, pieces, Color.WHITE)
    ans = [move.an_string for move in result]
    assert "Qh4e1" in ans
    assert "Qh1e1" in ans
    assert "Qe4e1" in ans
