from typing import List

from board import build_pieces, search_by_indexes
from color import Color
from piece import Piece


def test_build_pieces() -> None:
    """Tests the board pieces creation"""
    pieces = build_pieces(8)
    assert pieces[0] == Piece(Color.WHITE, "R", 1, 1)
    assert pieces[1] == Piece(Color.WHITE, "N", 2, 1)
    assert pieces[2] == Piece(Color.WHITE, "B", 3, 1)
    assert pieces[3] == Piece(Color.WHITE, "Q", 4, 1)
    assert pieces[4] == Piece(Color.WHITE, "K", 5, 1)
    assert pieces[5] == Piece(Color.WHITE, "B", 6, 1)
    assert pieces[6] == Piece(Color.WHITE, "N", 7, 1)
    assert pieces[7] == Piece(Color.WHITE, "R", 8, 1)
    assert pieces[8] == Piece(Color.WHITE, "P", 1, 2)
    assert pieces[9] == Piece(Color.WHITE, "P", 2, 2)
    assert pieces[10] == Piece(Color.WHITE, "P", 3, 2)
    assert pieces[11] == Piece(Color.WHITE, "P", 4, 2)
    assert pieces[12] == Piece(Color.WHITE, "P", 5, 2)
    assert pieces[13] == Piece(Color.WHITE, "P", 6, 2)
    assert pieces[14] == Piece(Color.WHITE, "P", 7, 2)
    assert pieces[15] == Piece(Color.WHITE, "P", 8, 2)
    assert pieces[16] == Piece(Color.BLACK, "P", 1, 7)
    assert pieces[17] == Piece(Color.BLACK, "P", 2, 7)
    assert pieces[18] == Piece(Color.BLACK, "P", 3, 7)
    assert pieces[19] == Piece(Color.BLACK, "P", 4, 7)
    assert pieces[20] == Piece(Color.BLACK, "P", 5, 7)
    assert pieces[21] == Piece(Color.BLACK, "P", 6, 7)
    assert pieces[22] == Piece(Color.BLACK, "P", 7, 7)
    assert pieces[23] == Piece(Color.BLACK, "P", 8, 7)
    assert pieces[24] == Piece(Color.BLACK, "R", 1, 8)
    assert pieces[25] == Piece(Color.BLACK, "N", 2, 8)
    assert pieces[26] == Piece(Color.BLACK, "B", 3, 8)
    assert pieces[27] == Piece(Color.BLACK, "Q", 4, 8)
    assert pieces[28] == Piece(Color.BLACK, "K", 5, 8)
    assert pieces[29] == Piece(Color.BLACK, "B", 6, 8)
    assert pieces[30] == Piece(Color.BLACK, "N", 7, 8)
    assert pieces[31] == Piece(Color.BLACK, "R", 8, 8)


def test_search_by_indexes_match() -> None:
    """Tests the search by indexes finding something"""
    pieces = [Piece(Color.BLACK, "", 0, 0)]
    assert search_by_indexes(pieces, 0, 0) == pieces[0]


def test_search_by_indexes_empty_pieces() -> None:
    """Tests the search by indexes finding nothing because array is empty"""
    pieces: List[Piece] = []
    assert search_by_indexes(pieces, 0, 0) is None


def test_search_by_indexes_not_match() -> None:
    """Tests the search by indexes finding nothing because no matches are present"""
    pieces = [Piece(Color.BLACK, "", 0, 0)]
    assert search_by_indexes(pieces, 0, 1) is None
