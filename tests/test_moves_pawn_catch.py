from moves_global import get_moves_pawn
from piece import Piece
from utils import print_board


def test_pawn_start_catch_right_white():
    """Tests the available rules of a pawn that can capture an enemy"""
    piece = Piece("W", "P", 1, 2, False)
    enemy = Piece("B", "P", 2, 3, False)
    print_board(8, [piece, enemy])
    result = get_moves_pawn(8, piece, [piece, enemy])
    assert len(result) == 3
    assert "Pa2a3" in result
    assert "Pa2a4" in result
    assert "Pa2b3" in result


def test_pawn_start_catch_right_black():
    """Tests the available rules of a pawn that can capture an enemy"""
    piece = Piece("B", "P", 3, 3, False)
    enemy = Piece("W", "P", 2, 2, False)
    print_board(8, [piece, enemy])
    result = get_moves_pawn(8, piece, [piece, enemy])
    assert len(result) == 3
    assert "Pc3c2" in result
    assert "Pc3c1" in result
    assert "Pc3b2" in result


def test_pawn_start_catch_left_black():
    """Tests the available rules of a pawn that can capture an enemy"""
    piece = Piece("B", "P", 3, 3, False)
    enemy = Piece("W", "P", 4, 2, False)
    print_board(8, [piece, enemy])
    result = get_moves_pawn(8, piece, [piece, enemy])
    assert len(result) == 3
    assert "Pc3c2" in result
    assert "Pc3c1" in result
    assert "Pc3d2" in result


def test_pawn_start_catch_left_white():
    """Tests the available rules of a pawn that can capture an enemy"""
    piece = Piece("W", "P", 2, 1, False)
    enemy = Piece("B", "P", 1, 2, False)
    print_board(8, [piece, enemy])
    result = get_moves_pawn(8, piece, [piece, enemy])
    assert len(result) == 3
    assert "Pb1b2" in result
    assert "Pb1b3" in result
    assert "Pb1a2" in result
