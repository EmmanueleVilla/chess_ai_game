from moves_single import get_moves_pawn
from piece import Piece
from tests.base import assert_same_move


def test_pawn_start_moves_black():
    """Tests the available rules of a pawn that never moved before"""
    piece = Piece("B", "P", 1, 7, False)
    result = get_moves_pawn(8, piece, [piece])
    expected = ["a5", "a6"]
    assert_same_move(expected, result)


def test_pawn_start_moves_blocked_path_2_black_enemy():
    """Tests the available rules of a pawn that never moved before but has a blocked path 2 blocks ahead by an enemy"""
    piece = Piece("B", "P", 1, 7, False)
    blocker = Piece("W", "P", 1, 5)
    result = get_moves_pawn(8, piece, [piece, blocker])
    expected = ["a6"]
    assert_same_move(expected, result)


def test_pawn_start_moves_blocked_path_1_black_enemy():
    """Tests the available rules of a pawn that never moved before but has a blocked path 1 block ahead by an enemy"""
    piece = Piece("B", "P", 1, 7, False)
    blocker = Piece("W", "P", 1, 6)
    result = get_moves_pawn(8, piece, [piece, blocker])
    assert len(result) == 0


def test_pawn_start_moves_blocked_path_2_black_ally():
    """Tests the available rules of a pawn that never moved before but has a blocked path 2 blocks ahead by an ally"""
    piece = Piece("B", "P", 1, 7, False)
    blocker = Piece("B", "P", 1, 5)
    result = get_moves_pawn(8, piece, [piece, blocker])
    expected = ["a6"]
    assert_same_move(expected, result)


def test_pawn_start_moves_blocked_path_1_black_ally():
    """Tests the available rules of a pawn that never moved before but has a blocked path 1 block ahead by an ally"""
    piece = Piece("B", "P", 1, 7, False)
    blocker = Piece("B", "P", 1, 6)
    result = get_moves_pawn(8, piece, [piece, blocker])
    assert len(result) == 0


def test_pawn_already_moved_black():
    """Tests the available rules of a pawn that already moved before"""
    piece = Piece("B", "P", 1, 7, True)
    result = get_moves_pawn(8, piece, [piece])
    expected = ["a6"]
    assert_same_move(expected, result)


def test_pawn_already_moved_blocked_path_black():
    """Tests the available rules of a pawn that already moved before but has a blocked path 1 block ahead"""
    piece = Piece("B", "P", 1, 7, True)
    blocker = Piece("W", "P", 1, 6)
    result = get_moves_pawn(8, piece, [piece, blocker])
    assert len(result) == 0


def test_pawn_end_reached_black():
    """Tests the available rules of a pawn that already reached the last cell.
    This can't happen tho, because a Pawn must be promoted"""
    piece = Piece("B", "P", 1, 0, True)
    result = get_moves_pawn(8, piece, [piece])
    assert len(result) == 0
