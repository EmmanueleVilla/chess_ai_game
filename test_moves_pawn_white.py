from moves_global import get_moves_pawn
from piece import Piece


def test_pawn_start_moves_white():
    """Tests the available rules of a pawn that never moved before"""
    piece = Piece("W", "P", 1, 2, False)
    result = get_moves_pawn(8, piece, [piece])
    assert len(result) == 2
    assert "Pa2a3" in result
    assert "Pa2a4" in result


def test_pawn_start_moves_blocked_path_2_white_ally():
    """Tests the available rules of a pawn that never moved before but has a blocked path 2 blocks ahead by an ally"""
    piece = Piece("W", "P", 1, 2, False)
    blocker = Piece("W", "P", 1, 4)
    result = get_moves_pawn(8, piece, [piece, blocker])
    assert len(result) == 1
    assert "Pa2a3" in result


def test_pawn_start_moves_blocked_path_1_white_ally():
    """Tests the available rules of a pawn that never moved before but has a blocked path 1 block ahead by an ally"""
    piece = Piece("W", "P", 1, 2, False)
    blocker = Piece("W", "P", 1, 3)
    result = get_moves_pawn(8, piece, [piece, blocker])
    assert len(result) == 0


def test_pawn_start_moves_blocked_path_2_white_enemy():
    """Tests the available rules of a pawn that never moved before but has a blocked path 2 blocks ahead by an enemy"""
    piece = Piece("W", "P", 1, 2, False)
    blocker = Piece("B", "P", 1, 4)
    result = get_moves_pawn(8, piece, [piece, blocker])
    assert len(result) == 1
    assert "Pa2a3" in result


def test_pawn_start_moves_blocked_path_1_white_enemy():
    """Tests the available rules of a pawn that never moved before but has a blocked path 1 block ahead by an enemy"""
    piece = Piece("W", "P", 1, 2, False)
    blocker = Piece("B", "P", 1, 3)
    result = get_moves_pawn(8, piece, [piece, blocker])
    assert len(result) == 0


def test_pawn_already_moved_white():
    """Tests the available rules of a pawn that already moved before"""
    piece = Piece("W", "P", 1, 2, True)
    result = get_moves_pawn(8, piece, [piece])
    assert len(result) == 1
    assert "Pa2a3" in result


def test_pawn_already_moved_blocked_path_white():
    """Tests the available rules of a pawn that already moved before but has a blocked path 1 block ahead"""
    piece = Piece("W", "P", 1, 2, True)
    blocker = Piece("W", "P", 1, 3)
    result = get_moves_pawn(8, piece, [piece, blocker])
    assert len(result) == 0


def test_pawn_end_reached_white():
    """Tests the available rules of a pawn that already reached the last cell.
    This can't happen tho, because a Pawn must be promoted"""
    piece = Piece("W", "P", 1, 8, True)
    result = get_moves_pawn(8, piece, [piece])
    assert len(result) == 0
