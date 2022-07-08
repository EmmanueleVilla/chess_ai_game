from board import build_pieces
from colors import COLOR_BLUE
from piece import Piece


def test_build_pieces():
    pieces = build_pieces()
    assert pieces[0] == Piece(COLOR_BLUE, "T", 0, 0)
