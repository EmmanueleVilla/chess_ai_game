from typing import List, Set

from move import Move
from piece import Piece


def assert_same_move(strings: List[str], moves: List[Move]) -> None:
    """Verifies that the two given array represents the same moves"""
    assert len(moves) == len(strings)
    for move in moves:
        print(move.an_string)
        assert move.an_string in strings


def assert_same_pieces(expected: Set[Piece], result: Set[Piece]) -> None:
    """Verifies that the two given array represents the same moves"""
    assert len(result) == len(expected)
    for piece in result:
        assert piece in expected
