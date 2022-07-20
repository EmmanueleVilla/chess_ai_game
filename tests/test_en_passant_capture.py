from color import Color
from moves import get_all_moves
from moves_applier import apply_move
from piece import Piece
from tests.base import assert_same_move


def test_en_passant_capture() -> None:
    """Test the en passant capture moves"""
    piece = Piece(Color.WHITE, "P", 1, 4, True, True)
    enemy = Piece(Color.BLACK, "P", 2, 4, True, False)
    pieces = {piece, enemy}

    result = get_all_moves(8, pieces, Color.BLACK)
    expected = ["b3", "bxa3 e.p."]
    assert_same_move(expected, result)


def test_en_passant_apply() -> None:
    """Test the en passant capture application"""
    piece = Piece(Color.WHITE, "P", 1, 4, True, True)
    enemy = Piece(Color.BLACK, "P", 2, 4, True, False)
    pieces = {piece, enemy}

    result = get_all_moves(8, pieces, Color.BLACK)
    en_passant = [move for move in result if move.en_passant][0]
    board = apply_move(pieces, en_passant)
    print(board)
