from board import search_by_indexes
from castling import Castling
from color import Color
from moves import get_moves_king
from moves_applier import apply_move
from piece import Piece


def test_white_castling_queen_apply() -> None:
    """Apply castling on queen side"""
    king = Piece(Color.WHITE, "K", 5, 1, False)
    rook = Piece(Color.WHITE, "R", 1, 1, False)
    moves = get_moves_king(8, king, {king, rook}, True)
    pieces = apply_move({king, rook}, [move for move in moves if move.castling == Castling.QUEEN_SIDE][0])
    assert len(pieces) == 2
    new_king = search_by_indexes(pieces, 3, 1)
    assert new_king is not None and new_king.name == "K"
    new_rook = search_by_indexes(pieces, 4, 1)
    assert new_rook is not None and new_rook.name == "R"


def test_white_castling_king_apply() -> None:
    """Apply castling on queen side"""
    king = Piece(Color.WHITE, "K", 5, 1, False)
    rook = Piece(Color.WHITE, "R", 8, 1, False)
    moves = get_moves_king(8, king, {king, rook}, True)
    pieces = apply_move({king, rook}, [move for move in moves if move.castling == Castling.KING_SIDE][0])
    assert len(pieces) == 2
    new_king = search_by_indexes(pieces, 7, 1)
    assert new_king is not None and new_king.name == "K"
    new_rook = search_by_indexes(pieces, 6, 1)
    assert new_rook is not None and new_rook.name == "R"


def test_black_castling_queen_apply() -> None:
    """Apply castling on queen side"""
    king = Piece(Color.BLACK, "K", 5, 8, False)
    rook = Piece(Color.BLACK, "R", 1, 8, False)
    moves = get_moves_king(8, king, {king, rook}, True)
    pieces = apply_move({king, rook}, [move for move in moves if move.castling == Castling.QUEEN_SIDE][0])
    assert len(pieces) == 2
    new_king = search_by_indexes(pieces, 3, 8)
    assert new_king is not None and new_king.name == "K"
    new_rook = search_by_indexes(pieces, 4, 8)
    assert new_rook is not None and new_rook.name == "R"


def test_black_castling_king_apply() -> None:
    """Apply castling on queen side"""
    king = Piece(Color.BLACK, "K", 5, 8, False)
    rook = Piece(Color.BLACK, "R", 8, 8, False)
    moves = get_moves_king(8, king, {king, rook}, True)
    pieces = apply_move({king, rook}, [move for move in moves if move.castling == Castling.KING_SIDE][0])
    assert len(pieces) == 2
    new_king = search_by_indexes(pieces, 7, 8)
    assert new_king is not None and new_king.name == "K"
    new_rook = search_by_indexes(pieces, 6, 8)
    assert new_rook is not None and new_rook.name == "R"
