from color import Color
from moves_single import get_moves_pawn
from piece import Piece
from tests.base import assert_same_move


def test_pawn_start_catch_right_white() -> None:
    """Tests the available rules of a pawn that can capture an enemy"""
    piece = Piece(Color.WHITE, "P", 1, 2, False)
    enemy = Piece(Color.BLACK, "P", 2, 3, False)
    result = get_moves_pawn(8, piece, {piece, enemy})
    expected = ["a3", "a4", "axb3"]
    assert_same_move(expected, result)


def test_pawn_start_catch_right_black() -> None:
    """Tests the available rules of a pawn that can capture an enemy"""
    piece = Piece(Color.BLACK, "P", 3, 3, True)
    enemy = Piece(Color.WHITE, "P", 2, 2, True)
    result = get_moves_pawn(8, piece, {piece, enemy})
    expected = ["c2", "cxb2"]
    assert_same_move(expected, result)


def test_pawn_start_catch_left_black() -> None:
    """Tests the available rules of a pawn that can capture an enemy"""
    piece = Piece(Color.BLACK, "P", 3, 3, True)
    enemy = Piece(Color.WHITE, "P", 4, 2, True)
    result = get_moves_pawn(8, piece, {piece, enemy})
    expected = ["c2", "cxd2"]
    assert_same_move(expected, result)


def test_pawn_start_catch_left_white() -> None:
    """Tests the available rules of a pawn that can capture an enemy"""
    piece = Piece(Color.WHITE, "P", 2, 1, False)
    enemy = Piece(Color.BLACK, "P", 1, 2, False)
    result = get_moves_pawn(8, piece, {piece, enemy})
    expected = ["b2", "b3", "bxa2"]
    assert_same_move(expected, result)
