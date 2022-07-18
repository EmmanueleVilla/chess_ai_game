from functools import reduce

from moves_applier import apply_move
from moves_single import get_moves


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
        or a # if it's a checkmate
        and removes the moves that cause a check to me"""
    result = []
    enemy_color = "B" if color == "W" else "W"
    for move in applied_moves:
        # Skip if my king is in check
        if is_king_in_check(board_size, move[1], color):
            continue
        if is_king_in_check(board_size, move[1], enemy_color):
            king = [piece for piece in move[1] if piece.color == enemy_color and piece.name == "K"]
            king_moves = get_moves(board_size, king, move[1])
            if len(king_moves) == 0:
                # checkmate -> add #
                result.append(move[1])
            else:
                # check -> add +
                result.append(move[1])
        else:
            result.append(move[1])
    return applied_moves


def is_king_in_check(board_size, pieces, color):
    """Returns true if on this board the king of the given color is in check"""
    full = [get_moves(board_size, piece, pieces) for piece in pieces if piece.color != color]
    if len(full) > 0:
        full = reduce(lambda x, y: x + y, full)
    my_king = [piece for piece in pieces if piece.color == color and piece.name == "K"]
    if len(my_king) == 1:
        return len([move for move in full if move.coord == my_king[0].coord]) > 0
    return False
