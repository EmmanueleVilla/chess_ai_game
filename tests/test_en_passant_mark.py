from color import Color
from moves import get_all_moves
from moves_applier import apply_move
from piece import Piece


def test_base_en_passant_no_mark() -> None:
    """Tests that en_passant is not marked in the one-step move"""
    piece = Piece(Color.WHITE, "P", 1, 1, False)
    moves = get_all_moves(8, {piece}, Color.WHITE)
    single_step = [move for move in moves if abs(move.j - move.piece.j) == 1][0]
    pieces = apply_move({piece}, single_step)
    new_piece = [piece for piece in pieces if piece.name == "P"][0]
    assert not new_piece.en_passant


def test_base_en_passant_mark() -> None:
    """Tests that en_passant is marked in the two-step move"""
    piece = Piece(Color.WHITE, "P", 1, 1, False)
    moves = get_all_moves(8, {piece}, Color.WHITE)
    double_step = [move for move in moves if abs(move.j - move.piece.j) > 1][0]
    pieces = apply_move({piece}, double_step)
    new_piece = [piece for piece in pieces if piece.name == "P"][0]
    assert new_piece.en_passant


def test_en_passant_reset_mark() -> None:
    """Tests that en_passant is reset after my next turn"""
    piece = Piece(Color.WHITE, "P", 1, 1, False)
    enemy = Piece(Color.BLACK, "P", 8, 8, False)
    pieces = {piece, enemy}
    # Turn 1, white, marked as en_passant
    moves = get_all_moves(8, pieces, Color.WHITE)
    move = [move for move in moves if abs(move.j - move.piece.j) > 1][0]
    pieces = apply_move(pieces, move)
    new_piece = [piece for piece in pieces if piece.color == Color.WHITE][0]
    assert new_piece.en_passant
    new_piece = [piece for piece in pieces if piece.color == Color.BLACK][0]
    assert not new_piece.en_passant

    # Turn 1, black, both marked en_passant
    moves = get_all_moves(8, pieces, Color.BLACK)
    move = [move for move in moves if abs(move.j - move.piece.j) > 1][0]
    pieces = apply_move(pieces, move)
    new_piece = [piece for piece in pieces if piece.color == Color.WHITE][0]
    assert new_piece.en_passant
    new_piece = [piece for piece in pieces if piece.color == Color.BLACK][0]
    assert new_piece.en_passant

    # Turn 2, white, only black marked en_passant
    moves = get_all_moves(8, pieces, Color.WHITE)
    move = moves[0]
    pieces = apply_move(pieces, move)
    new_piece = [piece for piece in pieces if piece.color == Color.WHITE][0]
    assert not new_piece.en_passant
    new_piece = [piece for piece in pieces if piece.color == Color.BLACK][0]
    assert new_piece.en_passant
