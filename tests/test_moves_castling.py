from castling import Castling
from color import Color
from moves import get_moves_king
from piece import Piece


def test_white_castling_queen_ok() -> None:
    """Confirm that castling is possible on queen side"""
    king = Piece(Color.WHITE, "K", 5, 1, False)
    rook = Piece(Color.WHITE, "R", 1, 1, False)
    expected = get_moves_king(8, king, {king, rook}, True)
    assert len([move for move in expected if move.castling == Castling.QUEEN_SIDE]) == 1


def test_white_castling_queen_ko_check() -> None:
    """Confirm that castling is not possible on queen side"""
    king = Piece(Color.WHITE, "K", 5, 1, False)
    rook = Piece(Color.WHITE, "R", 1, 1, False)
    enemy = Piece(Color.BLACK, "Q", 5, 3, True)
    expected = get_moves_king(8, king, {king, rook, enemy}, True)
    assert len([move for move in expected if move.castling == Castling.QUEEN_SIDE]) == 0


def test_white_castling_queen_ko_check_during_movement_4() -> None:
    """Confirm that castling is not possible on queen side"""
    king = Piece(Color.WHITE, "K", 5, 1, False)
    rook = Piece(Color.WHITE, "R", 1, 1, False)
    enemy = Piece(Color.BLACK, "Q", 4, 3, True)
    expected = get_moves_king(8, king, {king, rook, enemy}, True)
    assert len([move for move in expected if move.castling == Castling.QUEEN_SIDE]) == 0


def test_white_castling_queen_ko_check_during_movement_3() -> None:
    """Confirm that castling is not possible on queen side"""
    king = Piece(Color.WHITE, "K", 5, 1, False)
    rook = Piece(Color.WHITE, "R", 1, 1, False)
    enemy = Piece(Color.BLACK, "Q", 3, 3, True)
    expected = get_moves_king(8, king, {king, rook, enemy}, True)
    assert len([move for move in expected if move.castling == Castling.QUEEN_SIDE]) == 0


def test_white_castling_queen_ko_check_during_movement_2() -> None:
    """Confirm that castling is not possible on queen side"""
    king = Piece(Color.WHITE, "K", 5, 1, False)
    rook = Piece(Color.WHITE, "R", 1, 1, False)
    enemy = Piece(Color.BLACK, "Q", 2, 3, True)
    expected = get_moves_king(8, king, {king, rook, enemy}, True)
    assert len([move for move in expected if move.castling == Castling.QUEEN_SIDE]) == 0


def test_white_castling_queen_ko_check_during_movement_1() -> None:
    """Confirm that castling is not possible on queen side"""
    king = Piece(Color.WHITE, "K", 5, 1, False)
    rook = Piece(Color.WHITE, "R", 1, 1, False)
    enemy = Piece(Color.BLACK, "Q", 1, 3, True)
    expected = get_moves_king(8, king, {king, rook, enemy}, True)
    assert len([move for move in expected if move.castling == Castling.QUEEN_SIDE]) == 0
