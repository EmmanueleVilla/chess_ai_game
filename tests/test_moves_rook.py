from moves_global import get_moves_rook
from piece import Piece


def test_rook_free():
    """Tests the available rules of a rook with full free space"""
    piece = Piece("W", "R", 4, 6, False)
    result = get_moves_rook(8, piece, [piece])
    assert len(result) == 14
    assert "Rd6d7" in result
    assert "Rd6d8" in result
    assert "Rd6d5" in result
    assert "Rd6d4" in result
    assert "Rd6d3" in result
    assert "Rd6d2" in result
    assert "Rd6d1" in result
    assert "Rd6e6" in result
    assert "Rd6f6" in result
    assert "Rd6g6" in result
    assert "Rd6h6" in result
    assert "Rd6c6" in result
    assert "Rd6b6" in result
    assert "Rd6a6" in result


def test_rook_friendly():
    """Tests the available rules of a rook with a friendly pawn that stops it"""
    piece = Piece("W", "R", 4, 6, False)
    friend = Piece("W", "P", 2, 6, False)
    result = get_moves_rook(8, piece, [piece, friend])
    assert len(result) == 12
    assert "Rd6d7" in result
    assert "Rd6d8" in result
    assert "Rd6d5" in result
    assert "Rd6d4" in result
    assert "Rd6d3" in result
    assert "Rd6d2" in result
    assert "Rd6d1" in result
    assert "Rd6e6" in result
    assert "Rd6f6" in result
    assert "Rd6g6" in result
    assert "Rd6h6" in result
    assert "Rd6c6" in result


def test_rook_enemy():
    """Tests the available rules of a rook with an enemy pawn that stops it"""
    piece = Piece("W", "R", 4, 6, False)
    friend = Piece("B", "P", 2, 6, False)
    result = get_moves_rook(8, piece, [piece, friend])
    assert len(result) == 13
    assert "Rd6d7" in result
    assert "Rd6d8" in result
    assert "Rd6d5" in result
    assert "Rd6d4" in result
    assert "Rd6d3" in result
    assert "Rd6d2" in result
    assert "Rd6d1" in result
    assert "Rd6e6" in result
    assert "Rd6f6" in result
    assert "Rd6g6" in result
    assert "Rd6h6" in result
    assert "Rd6c6" in result
    assert "Rd6b6" in result
