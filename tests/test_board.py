from board import build_pieces, search_by_indexes
from piece import Piece


def test_build_pieces():
    """Tests the board pieces creation"""
    pieces = build_pieces(8)
    assert pieces[0] == Piece("W", "R", 1, 1)
    assert pieces[1] == Piece("W", "N", 2, 1)
    assert pieces[2] == Piece("W", "B", 3, 1)
    assert pieces[3] == Piece("W", "Q", 4, 1)
    assert pieces[4] == Piece("W", "K", 5, 1)
    assert pieces[5] == Piece("W", "B", 6, 1)
    assert pieces[6] == Piece("W", "N", 7, 1)
    assert pieces[7] == Piece("W", "R", 8, 1)
    assert pieces[8] == Piece("W", "P", 1, 2)
    assert pieces[9] == Piece("W", "P", 2, 2)
    assert pieces[10] == Piece("W", "P", 3, 2)
    assert pieces[11] == Piece("W", "P", 4, 2)
    assert pieces[12] == Piece("W", "P", 5, 2)
    assert pieces[13] == Piece("W", "P", 6, 2)
    assert pieces[14] == Piece("W", "P", 7, 2)
    assert pieces[15] == Piece("W", "P", 8, 2)
    assert pieces[16] == Piece("B", "P", 1, 7)
    assert pieces[17] == Piece("B", "P", 2, 7)
    assert pieces[18] == Piece("B", "P", 3, 7)
    assert pieces[19] == Piece("B", "P", 4, 7)
    assert pieces[20] == Piece("B", "P", 5, 7)
    assert pieces[21] == Piece("B", "P", 6, 7)
    assert pieces[22] == Piece("B", "P", 7, 7)
    assert pieces[23] == Piece("B", "P", 8, 7)
    assert pieces[24] == Piece("B", "R", 1, 8)
    assert pieces[25] == Piece("B", "N", 2, 8)
    assert pieces[26] == Piece("B", "B", 3, 8)
    assert pieces[27] == Piece("B", "Q", 4, 8)
    assert pieces[28] == Piece("B", "K", 5, 8)
    assert pieces[29] == Piece("B", "B", 6, 8)
    assert pieces[30] == Piece("B", "N", 7, 8)
    assert pieces[31] == Piece("B", "R", 8, 8)


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
