from moves_global import get_moves_pawn
from piece import Piece


def test_pawn_start_moves_white():
    """Tests the available rules of a pawn that never moved before"""
    piece = Piece("W", "P", 1, 2, False)
    result = get_moves_pawn(8, piece, [piece])
    assert len(result) == 2
    assert result[0] == "Pa2a3"
    assert result[1] == "Pa2a4"


def test_pawn_start_moves_blocked_path_2_white():
    """Tests the available rules of a pawn that never moved before but has a blocked path 2 blocks ahead"""
    piece = Piece("W", "P", 1, 2, False)
    blocker = Piece("W", "P", 1, 4)
    result = get_moves_pawn(8, piece, [piece, blocker])
    assert len(result) == 1
    assert result[0] == "Pa2a3"


def test_pawn_start_moves_blocked_path_1_white():
    """Tests the available rules of a pawn that never moved before but has a blocked path 1 block ahead"""
    piece = Piece("W", "P", 1, 2, False)
    blocker = Piece("W", "P", 1, 3)
    result = get_moves_pawn(8, piece, [piece, blocker])
    assert len(result) == 0


def test_pawn_already_moved_white():
    """Tests the available rules of a pawn that already moved before"""
    piece = Piece("W", "P", 1, 2, True)
    result = get_moves_pawn(8, piece, [piece])
    assert len(result) == 1
    assert result[0] == "Pa2a3"


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
