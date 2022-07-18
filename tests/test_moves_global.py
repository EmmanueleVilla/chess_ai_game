from moves_global import get_all_moves
from piece import Piece
from tests.base import assert_same_move


def test_get_all_moves_base():
    """Checks the full moves of a board with a single pawn"""
    piece = Piece("W", "P", 1, 2, True)
    result = get_all_moves(8, [piece], "W")
    expected = ["a3"]
    assert_same_move(expected, result)


def test_get_all_moves_to_check():
    """Checks that the moves that put the enemy king in check finish with the + sign"""
    piece = Piece("W", "P", 1, 2, True)
    enemy = Piece("B", "K", 2, 4, True)
    result = get_all_moves(8, [piece, enemy], "W")
    expected = ["a3+"]
    assert_same_move(expected, result)


def test_get_all_moves_causing_check():
    """Checks that the moves that put my king into check are removed from the list"""
    piece = Piece("W", "P", 2, 2, True)
    ally = Piece("W", "K", 1, 2, True)
    enemy = Piece("B", "Q", 3, 2, True)
    result = get_all_moves(8, [piece, enemy, ally], "W")
    expected = ["Ka3", "Ka1"]
    assert_same_move(expected, result)
