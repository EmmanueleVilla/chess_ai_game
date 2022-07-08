from board import build_pieces
from colors import COLOR_BLUE, COLOR_GREEN
from piece import Piece


def test_build_pieces():
    pieces = build_pieces()
    assert pieces[0] == Piece(COLOR_BLUE, "T", 0, 0)
    assert pieces[1] == Piece(COLOR_BLUE, "N", 0, 1)
    assert pieces[2] == Piece(COLOR_BLUE, "B", 0, 2)
    assert pieces[3] == Piece(COLOR_BLUE, "K", 0, 3)
    assert pieces[4] == Piece(COLOR_BLUE, "Q", 0, 4)
    assert pieces[5] == Piece(COLOR_BLUE, "B", 0, 5)
    assert pieces[6] == Piece(COLOR_BLUE, "N", 0, 6)
    assert pieces[7] == Piece(COLOR_BLUE, "T", 0, 7)
    assert pieces[8] == Piece(COLOR_BLUE, "P", 1, 0)
    assert pieces[9] == Piece(COLOR_BLUE, "P", 1, 1)
    assert pieces[10] == Piece(COLOR_BLUE, "P", 1, 2)
    assert pieces[11] == Piece(COLOR_BLUE, "P", 1, 3)
    assert pieces[12] == Piece(COLOR_BLUE, "P", 1, 4)
    assert pieces[13] == Piece(COLOR_BLUE, "P", 1, 5)
    assert pieces[14] == Piece(COLOR_BLUE, "P", 1, 6)
    assert pieces[15] == Piece(COLOR_BLUE, "P", 1, 7)
    assert pieces[16] ==  Piece(COLOR_GREEN, "P", 6, 0)
    assert pieces[17] == Piece(COLOR_GREEN, "P", 6, 1)
    assert pieces[18] == Piece(COLOR_GREEN, "P", 6, 2)
    assert pieces[19] == Piece(COLOR_GREEN, "P", 6, 3)
    assert pieces[20] == Piece(COLOR_GREEN, "P", 6, 4)
    assert pieces[21] == Piece(COLOR_GREEN, "P", 6, 5)
    assert pieces[22] == Piece(COLOR_GREEN, "P", 6, 6)
    assert pieces[23] == Piece(COLOR_GREEN, "P", 6, 7)
    assert pieces[24] == Piece(COLOR_GREEN, "T", 7, 0)
    assert pieces[25] == Piece(COLOR_GREEN, "N", 7, 1)
    assert pieces[26] == Piece(COLOR_GREEN, "B", 7, 2)
    assert pieces[27] == Piece(COLOR_GREEN, "K", 7, 3)
    assert pieces[28] == Piece(COLOR_GREEN, "Q", 7, 4)
    assert pieces[29] == Piece(COLOR_GREEN, "B", 7, 5)
    assert pieces[30] == Piece(COLOR_GREEN, "N", 7, 6)
    assert pieces[31] == Piece(COLOR_GREEN, "T", 7, 7)
