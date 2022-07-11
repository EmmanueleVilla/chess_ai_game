from moves_global import get_moves_rook
from piece import Piece


def test_rook_free():
    """Tests the available rules of a rook with full free space"""
    piece = Piece("W", "R", 4, 6, False)
    result = get_moves_rook(8, piece, [piece])
    assert len(result) == 14
    assert "Rd7" in result
    assert "Rd8" in result
    assert "Rd5" in result
    assert "Rd4" in result
    assert "Rd3" in result
    assert "Rd2" in result
    assert "Rd1" in result
    assert "Re6" in result
    assert "Rf6" in result
    assert "Rg6" in result
    assert "Rh6" in result
    assert "Rc6" in result
    assert "Rb6" in result
    assert "Ra6" in result


def test_rook_friendly():
    """Tests the available rules of a rook with a friendly pawn that stops it"""
    piece = Piece("W", "R", 4, 6, False)
    friend = Piece("W", "P", 2, 6, False)
    result = get_moves_rook(8, piece, [piece, friend])
    assert len(result) == 12
    assert "Rd7" in result
    assert "Rd8" in result
    assert "Rd5" in result
    assert "Rd4" in result
    assert "Rd3" in result
    assert "Rd2" in result
    assert "Rd1" in result
    assert "Re6" in result
    assert "Rf6" in result
    assert "Rg6" in result
    assert "Rh6" in result
    assert "Rc6" in result


def test_rook_enemy():
    """Tests the available rules of a rook with an enemy pawn that stops it"""
    piece = Piece("W", "R", 4, 6, False)
    friend = Piece("B", "P", 2, 6, False)
    result = get_moves_rook(8, piece, [piece, friend])
    assert len(result) == 13
    assert "Rd7" in result
    assert "Rd8" in result
    assert "Rd5" in result
    assert "Rd4" in result
    assert "Rd3" in result
    assert "Rd2" in result
    assert "Rd1" in result
    assert "Re6" in result
    assert "Rf6" in result
    assert "Rg6" in result
    assert "Rh6" in result
    assert "Rc6" in result
    assert "Rxb6" in result
