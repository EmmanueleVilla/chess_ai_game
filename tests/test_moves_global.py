from color import Color
from moves_global import get_all_moves
from piece import Piece
from tests.base import assert_same_move


def test_get_all_moves_base() -> None:
    """Checks the full moves of a board with a single pawn"""
    piece = Piece(Color.WHITE, "P", 1, 2, True)
    result = get_all_moves(8, {piece}, Color.WHITE)
    expected = ["a3"]
    assert_same_move(expected, result)


def test_get_all_moves_to_check() -> None:
    """Checks that the moves that put the enemy king in check finish with the + sign"""
    piece = Piece(Color.WHITE, "P", 1, 2, True)
    enemy = Piece(Color.BLACK, "K", 2, 4, True)
    result = get_all_moves(8, {piece, enemy}, Color.WHITE)
    expected = ["a3+"]
    assert_same_move(expected, result)


def test_get_all_moves_causing_check() -> None:
    """Checks that the moves that put my king into check are removed from the list"""
    piece = Piece(Color.WHITE, "P", 2, 2, True)
    ally = Piece(Color.WHITE, "K", 1, 2, True)
    enemy = Piece(Color.BLACK, "Q", 3, 2, True)
    result = get_all_moves(8, {piece, enemy, ally}, Color.WHITE)
    expected = ["Ka3", "Ka1"]
    assert_same_move(expected, result)
