def assert_same_array(result: [], expected: []):
    """Verifies that the two given arrays are the same"""
    assert len(result) == len(expected)
    for move in expected:
        assert move in result
