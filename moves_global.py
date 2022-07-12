from functools import reduce

from moves_applier import apply_move
from moves_single import get_moves


def get_all_moves(board_size, pieces, color):
    """Returns all the possible moves on the board for the given pieces of the given color"""
    full = reduce(lambda x, y: x + y,
                  [get_moves(board_size, piece, pieces) for piece in pieces if piece.color == color])
    applied_moves = [apply_move(board_size, pieces, move) for move in full]
    full = fix_check_info(board_size, pieces, color, full, applied_moves)
    full = fix_disambiguities(pieces, full)
    return full


def fix_disambiguities(pieces, full):
    """Adds additional information to the moves if some of them are equals"""
    print(pieces)
    print(full)
    # Todo: Implement this
    return full


def fix_check_info(board_size, pieces, enemy_color, full, applied_moves):
    """Adds a + at the end of the moves that cause a check to the opponent
        and removes the moves that cause a check to me"""
    print(board_size)
    print(pieces)
    print(enemy_color)
    print(full)
    print(applied_moves)

    # Todo: Implement this
    return full


def is_king_in_check(board_size, pieces, color):
    """Returns true if on this board the king of the given color is in check"""
    print(board_size)
    print(pieces)
    print(color)
    # Todo: Implement this
    return False
