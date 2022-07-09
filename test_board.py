from board import build_pieces, search_by_indexes
from piece import Piece


def test_build_pieces():
    """Tests the board pieces creation"""
    pieces = build_pieces(8)
    assert pieces[0] == Piece("W", "T", 1, 1)
    assert pieces[1] == Piece("W", "N", 1, 2)
    assert pieces[2] == Piece("W", "B", 1, 3)
    assert pieces[3] == Piece("W", "Q", 1, 4)
    assert pieces[4] == Piece("W", "K", 1, 5)
    assert pieces[5] == Piece("W", "B", 1, 6)
    assert pieces[6] == Piece("W", "N", 1, 7)
    assert pieces[7] == Piece("W", "T", 1, 8)
    assert pieces[8] == Piece("W", "P", 2, 1)
    assert pieces[9] == Piece("W", "P", 2, 2)
    assert pieces[10] == Piece("W", "P", 2, 3)
    assert pieces[11] == Piece("W", "P", 2, 4)
    assert pieces[12] == Piece("W", "P", 2, 5)
    assert pieces[13] == Piece("W", "P", 2, 6)
    assert pieces[14] == Piece("W", "P", 2, 7)
    assert pieces[15] == Piece("W", "P", 2, 8)
    assert pieces[16] == Piece("B", "P", 7, 1)
    assert pieces[17] == Piece("B", "P", 7, 2)
    assert pieces[18] == Piece("B", "P", 7, 3)
    assert pieces[19] == Piece("B", "P", 7, 4)
    assert pieces[20] == Piece("B", "P", 7, 5)
    assert pieces[21] == Piece("B", "P", 7, 6)
    assert pieces[22] == Piece("B", "P", 7, 7)
    assert pieces[23] == Piece("B", "P", 7, 8)
    assert pieces[24] == Piece("B", "T", 8, 1)
    assert pieces[25] == Piece("B", "N", 8, 2)
    assert pieces[26] == Piece("B", "B", 8, 3)
    assert pieces[27] == Piece("B", "Q", 8, 4)
    assert pieces[28] == Piece("B", "K", 8, 5)
    assert pieces[29] == Piece("B", "B", 8, 6)
    assert pieces[30] == Piece("B", "N", 8, 7)
    assert pieces[31] == Piece("B", "T", 8, 8)


def test_search_by_indexes_match():
    """Tests the search by indexes finding something"""
    pieces = [Piece("", "", 0, 0)]
    assert search_by_indexes(pieces, 0, 0) == pieces[0]


def test_search_by_indexes_empty_pieces():
    """Tests the search by indexes finding nothing because array is empty"""
    pieces = []
    assert search_by_indexes(pieces, 0, 0) is None


def test_search_by_indexes_not_match():
    """Tests the search by indexes finding nothing because no matches are present"""
    pieces = [Piece("", "", 0, 0)]
    assert search_by_indexes(pieces, 0, 1) is None
