from board import build_pieces
from color import Color
from moves import get_all_moves
from moves_applier import apply_move


def test_king_in_checkmate() -> None:
    """Plays a fixed match to check the king checkmate at the end"""
    pieces = build_pieces(8)

    # Turn 1
    moves = get_all_moves(8, pieces, Color.WHITE)
    pieces = apply_move(pieces, [move for move in moves if move.an_string == "g3"][0])

    moves = get_all_moves(8, pieces, Color.BLACK)
    pieces = apply_move(pieces, [move for move in moves if move.an_string == "Nc6"][0])

    # Turn 2
    moves = get_all_moves(8, pieces, Color.WHITE)
    pieces = apply_move(pieces, [move for move in moves if move.an_string == "h3"][0])

    moves = get_all_moves(8, pieces, Color.BLACK)
    pieces = apply_move(pieces, [move for move in moves if move.an_string == "a5"][0])

    # Turn 3
    moves = get_all_moves(8, pieces, Color.WHITE)
    pieces = apply_move(pieces, [move for move in moves if move.an_string == "f4"][0])

    moves = get_all_moves(8, pieces, Color.BLACK)
    pieces = apply_move(pieces, [move for move in moves if move.an_string == "e6"][0])

    # Turn 4
    moves = get_all_moves(8, pieces, Color.WHITE)
    pieces = apply_move(pieces, [move for move in moves if move.an_string == "g4"][0])

    moves = get_all_moves(8, pieces, Color.BLACK)
    pieces = apply_move(pieces, [move for move in moves if move.an_string == "Qh4#"][0])
