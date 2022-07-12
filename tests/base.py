import string

from move import Move


def assert_same_array(expected: [string], result: [Move]):
    """Verifies that the two given arrays are the same"""
    assert len(result) == len(expected)
    for move in result:
        assert move.to_an() in expected
