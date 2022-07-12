from moves_single import get_moves_pawn
from piece import Piece
from tests.base import assert_same_move
from utils import print_board


def test_pawn_start_catch_right_white():
    """Tests the available rules of a pawn that can capture an enemy"""
    piece = Piece("W", "P", 1, 2, False)
    enemy = Piece("B", "P", 2, 3, False)
    print_board(8, [piece, enemy])
    result = get_moves_pawn(8, piece, [piece, enemy])
    expected = ["a3", "a4", "axb3"]
    assert_same_move(expected, result)


def test_pawn_start_catch_right_black():
    """Tests the available rules of a pawn that can capture an enemy"""
    piece = Piece("B", "P", 3, 3, False)
    enemy = Piece("W", "P", 2, 2, False)
    print_board(8, [piece, enemy])
    result = get_moves_pawn(8, piece, [piece, enemy])
    expected = ["c2", "c1", "cxb2"]
    assert_same_move(expected, result)


def test_pawn_start_catch_left_black():
    """Tests the available rules of a pawn that can capture an enemy"""
    piece = Piece("B", "P", 3, 3, False)
    enemy = Piece("W", "P", 4, 2, False)
    print_board(8, [piece, enemy])
    result = get_moves_pawn(8, piece, [piece, enemy])
    expected = ["c2", "c1", "cxd2"]
    assert_same_move(expected, result)


def test_pawn_start_catch_left_white():
    """Tests the available rules of a pawn that can capture an enemy"""
    piece = Piece("W", "P", 2, 1, False)
    enemy = Piece("B", "P", 1, 2, False)
    print_board(8, [piece, enemy])
    result = get_moves_pawn(8, piece, [piece, enemy])
    expected = ["b2", "b3", "bxa2"]
    assert_same_move(expected, result)
