from moves_global import get_moves_rook
from piece import Piece


def test_rook_free():
    """Tests the available rules of a rook with full free space"""
    piece = Piece("W", "R", 4, 6, False)
    result = get_moves_rook(8, piece, [piece])
    assert len(result) == 14
    assert result[0] == "Rd6d7"
    assert result[1] == "Rd6d8"
    assert result[2] == "Rd6d5"
    assert result[3] == "Rd6d4"
    assert result[4] == "Rd6d3"
    assert result[5] == "Rd6d2"
    assert result[6] == "Rd6d1"
    assert result[7] == "Rd6e6"
    assert result[8] == "Rd6f6"
    assert result[9] == "Rd6g6"
    assert result[10] == "Rd6h6"
    assert result[11] == "Rd6c6"
    assert result[12] == "Rd6b6"
    assert result[13] == "Rd6a6"


def test_rook_friendly():
    """Tests the available rules of a rook with a friendly pawn that stops it"""
    piece = Piece("W", "R", 4, 6, False)
    friend = Piece("W", "P", 2, 6, False)
    result = get_moves_rook(8, piece, [piece, friend])
    assert len(result) == 12
    assert result[0] == "Rd6d7"
    assert result[1] == "Rd6d8"
    assert result[2] == "Rd6d5"
    assert result[3] == "Rd6d4"
    assert result[4] == "Rd6d3"
    assert result[5] == "Rd6d2"
    assert result[6] == "Rd6d1"
    assert result[7] == "Rd6e6"
    assert result[8] == "Rd6f6"
    assert result[9] == "Rd6g6"
    assert result[10] == "Rd6h6"
    assert result[11] == "Rd6c6"


def test_rook_enemy():
    """Tests the available rules of a rook with an enemy pawn that stops it"""
    piece = Piece("W", "R", 4, 6, False)
    friend = Piece("B", "P", 2, 6, False)
    result = get_moves_rook(8, piece, [piece, friend])
    assert len(result) == 13
    assert result[0] == "Rd6d7"
    assert result[1] == "Rd6d8"
    assert result[2] == "Rd6d5"
    assert result[3] == "Rd6d4"
    assert result[4] == "Rd6d3"
    assert result[5] == "Rd6d2"
    assert result[6] == "Rd6d1"
    assert result[7] == "Rd6e6"
    assert result[8] == "Rd6f6"
    assert result[9] == "Rd6g6"
    assert result[10] == "Rd6h6"
    assert result[11] == "Rd6c6"
    assert result[12] == "Rd6b6"
