from typing import List

from move import Move
from piece import Piece


def assert_same_move(strings: List[str], moves: List[Move]):
    """Verifies that the two given array represents the same moves"""
    assert len(moves) == len(strings)
    for move in moves:
        assert move.to_an() in strings


def assert_same_pieces(expected: List[Piece], result: List[Piece]):
    """Verifies that the two given array represents the same moves"""
    assert len(result) == len(expected)
    for piece in result:
        assert piece in expected
