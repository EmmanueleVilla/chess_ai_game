from functools import reduce

from move import Move
from moves_applier import apply_move
from moves_single import get_moves
from utils import print_board


def get_all_moves(board_size, pieces, color):
    """Returns all the possible moves on the board for the given pieces of the given color"""
    full = reduce(lambda x, y: x + y,
                  [get_moves(board_size, piece, pieces) for piece in pieces if piece.color == color])
    applied_moves = [(move, apply_move(pieces, move)) for move in full]
    full = fix_check_info(board_size, color, applied_moves)
    full = fix_ambiguities(pieces, full)
    return full


def fix_ambiguities(pieces, full):
    """Adds additional information to the moves if some of them are equals"""
    print(pieces)
    print(full)
    # Todo: Implement this
    return full


def fix_check_info(board_size, color, applied_moves):
    """Adds a + at the end of the moves that cause a check to the opponent
        and removes the moves that cause a check to me"""
    print(board_size)
    print(color)
    print(applied_moves)
    enemy_color = "B" if color == "W" else "W"
    # Remove applied moves where my king is in check
    full = [board[0] for board in applied_moves if not is_king_in_check(board_size, board[1], color)]
    # Todo: Implement this
    return full


def enhance_move_if_king_is_in_check(board_size, move, pieces, color):
    """Adds information about checking the king with the given color"""
    return Move(move.piece, move.coord.i, move.coord.j, True, is_king_in_check(board_size, pieces, color))


def is_king_in_check(board_size, pieces, color):
    """Returns true if on this board the king of the given color is in check"""
    print_board(board_size, pieces)
    full = [get_moves(board_size, piece, pieces) for piece in pieces if piece.color != color]
    if len(full) > 0:
        full = reduce(lambda x, y: x + y, full)
    my_king = [piece for piece in pieces if piece.color == color and piece.name == "K"]
    if len(my_king) == 1:
        return [move for move in full if move.coord == my_king[0].coord]
    return full
