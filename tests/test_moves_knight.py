from color import Color
from moves_single import get_moves_knight
from piece import Piece
from tests.base import assert_same_move


def test_knight_free() -> None:
    """Tests the available rules of a knight with full free space"""
    piece = Piece(Color.WHITE, "N", 3, 4, False)
    result = get_moves_knight(8, piece, [piece])
    expected = ["Na3", "Na5", "Nb2", "Nb6", "Nd2", "Nd6", "Ne3", "Ne5"]
    assert_same_move(expected, result)


def test_knight_friendly() -> None:
    """Tests the available rules of a knight with a friendly pawn that stops it"""
    piece = Piece(Color.WHITE, "N", 3, 4, False)
    friend = Piece(Color.WHITE, "P", 4, 6, False)
    result = get_moves_knight(8, piece, [piece, friend])
    expected = ["Na3", "Na5", "Nb2", "Nb6", "Nd2", "Ne3", "Ne5"]
    assert_same_move(expected, result)


def test_knight_enemy() -> None:
    """Tests the available rules of a knight with an enemy pawn that stops it"""
    piece = Piece(Color.WHITE, "N", 3, 4, False)
    enemy = Piece(Color.BLACK, "P", 4, 6, False)
    result = get_moves_knight(8, piece, [piece, enemy])
    expected = ["Na3", "Na5", "Nb2", "Nb6", "Nd2", "Nxd6", "Ne3", "Ne5"]
    assert_same_move(expected, result)
