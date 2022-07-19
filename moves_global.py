from functools import reduce
from typing import List, Tuple

from check import Check
from color import Color
from move import Move, copy_move_edit_check
from moves_applier import apply_move
from moves_single import get_moves
from piece import Piece


def get_all_moves(board_size: int, pieces: List[Piece], color: Color, fix_enemy_check_info: bool = True) -> List[Move]:
    """Returns all the possible moves on the board for the given pieces of the given color"""
    full = reduce(lambda x, y: x + y,
                  [get_moves(board_size, piece, pieces) for piece in pieces if piece.color == color])
    applied_moves = [(move, apply_move(pieces, move)) for move in full]
    full = fix_check_info(board_size, color, applied_moves, fix_enemy_check_info)
    full = fix_ambiguities(full)
    return full


def fix_ambiguities(full: List[Move]) -> List[Move]:
    """Adds additional information to the moves if some of them are equals"""
    # Todo: Refactor this to avoid modifying the move. Create a new one instead
    for move in full:
        duplicates = [m for m in full if m.piece.name == move.piece.name and m.i == move.i and m.j == move.j]
        if len(duplicates) > 1:
            same_i = all(x.piece.i == duplicates[0].piece.i for x in duplicates)
            same_j = all(x.piece.j == duplicates[0].piece.j for x in duplicates)
            for duplicate in duplicates:
                duplicate.set_print_i(len(duplicates) > 2 or not same_i or (same_i and same_j))
                duplicate.set_print_j(len(duplicates) > 2 or same_i)
    return full


def fix_check_info(board_size: int, color: Color, applied_moves: List[Tuple[Move, List[Piece]]],
                   fix_enemy_check_info: bool) -> List[Move]:
    """Adds a + at the end of the moves that cause a check to the opponent
        or a # if it's a checkmate
        and removes the moves that cause a check to me"""
    result: List[Move] = []
    enemy_color = Color.BLACK if color == Color.WHITE else Color.WHITE
    for move in applied_moves:
        # Skip if my king is in check
        if is_king_in_check(board_size, move[1], color):
            continue
        if fix_enemy_check_info and is_king_in_check(board_size, move[1], enemy_color):
            enemy_moves = get_all_moves(board_size, move[1], enemy_color, False)
            if len(enemy_moves) == 0:
                # checkmate -> add #
                result.append(copy_move_edit_check(move[0], Check.CHECKMATE))
            else:
                # check -> add +
                result.append(copy_move_edit_check(move[0], Check.CHECK))
        else:
            result.append(move[0])
    return result


def is_king_in_check(board_size: int, pieces: List[Piece], color: Color) -> bool:
    """Returns true if on this board the king of the given color is in check"""
    full: List[Move] = reduce(lambda x, y: x + y,
                              [get_moves(board_size, piece, pieces) for piece in pieces if piece.color != color], [])
    my_king: List[Piece] = [piece for piece in pieces if piece.color == color and piece.name == "K"]
    if len(my_king) == 1:
        return len([move for move in full if move.i == my_king[0].i and move.j == my_king[0].j]) > 0
    return False
