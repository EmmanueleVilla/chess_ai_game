from moves import get_moves_pawn
from piece import Piece
from utils import print_board


def test_pawn_start_catch_right_white():
    """Tests the available rules of a pawn that can capture an enemy"""
    piece = Piece("W", "P", 1, 2, False)
    enemy = Piece("B", "P", 2, 3, False)
    print_board(8, [piece, enemy])
    result = get_moves_pawn(8, piece, [piece, enemy])
    assert len(result) == 3
    assert "a3" in result
    assert "a4" in result
    assert "axb3" in result


def test_pawn_start_catch_right_black():
    """Tests the available rules of a pawn that can capture an enemy"""
    piece = Piece("B", "P", 3, 3, False)
    enemy = Piece("W", "P", 2, 2, False)
    print_board(8, [piece, enemy])
    result = get_moves_pawn(8, piece, [piece, enemy])
    assert len(result) == 3
    assert "c2" in result
    assert "c1" in result
    assert "cxb2" in result


def test_pawn_start_catch_left_black():
    """Tests the available rules of a pawn that can capture an enemy"""
    piece = Piece("B", "P", 3, 3, False)
    enemy = Piece("W", "P", 4, 2, False)
    print_board(8, [piece, enemy])
    result = get_moves_pawn(8, piece, [piece, enemy])
    assert len(result) == 3
    assert "c2" in result
    assert "c1" in result
    assert "cxd2" in result


def test_pawn_start_catch_left_white():
    """Tests the available rules of a pawn that can capture an enemy"""
    piece = Piece("W", "P", 2, 1, False)
    enemy = Piece("B", "P", 1, 2, False)
    print_board(8, [piece, enemy])
    result = get_moves_pawn(8, piece, [piece, enemy])
    assert len(result) == 3
    assert "b2" in result
    assert "b3" in result
    assert "bxa2" in result
