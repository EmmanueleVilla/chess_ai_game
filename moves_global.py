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
    enemy_color = "B" if color == "W" else "W"
    # Remove applied moves where my king is in check
    applied_moves = [enhance_move_if_king_is_in_check(board_size, move, applied_moves, enemy_color) for move in
                     applied_moves
                     if not will_my_king_be_in_check(board_size, move[1], color)]
    return [move for move in applied_moves]


def enhance_move_if_king_is_in_check(board_size: int, move: Move, applied_moves, color: str):
    """Adds information about checking the king with the given color"""
    return move


def will_my_king_be_in_check(board_size, pieces, color):
    """Returns true if on this board the king of the given color is in check"""
    print_board(board_size, pieces)
    full = [get_moves(board_size, piece, pieces) for piece in pieces if piece.color != color]
    if len(full) > 0:
        full = reduce(lambda x, y: x + y, full)
    my_king = [piece for piece in pieces if piece.color == color and piece.name == "K"]
    if len(my_king) == 1:
        return len([move for move in full if move.coord == my_king[0].coord]) > 0
    return False
