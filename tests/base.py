import string

from move import Move
from piece import Piece


def assert_same_move(expected: [string], result: [Move]):
    """Verifies that the two given array represents the same moves"""
    assert len(result) == len(expected)
    for move in result:
        assert move.to_an() in expected


def assert_same_pieces(expected: [Piece], result: [Piece]):
    """Verifies that the two given array represents the same moves"""
    assert len(result) == len(expected)
    for piece in result:
        assert piece in expected
