from functools import reduce
from typing import List, Tuple

from check import Check
from color import Color
from move import Move, copy_move
from moves_applier import apply_move
from moves_single import get_moves
from piece import Piece


def get_all_moves(board_size: int, pieces: List[Piece], color: Color) -> List[Move]:
    """Returns all the possible moves on the board for the given pieces of the given color"""
    full = reduce(lambda x, y: x + y,
                  [get_moves(board_size, piece, pieces) for piece in pieces if piece.color == color])
    applied_moves = [(move, apply_move(pieces, move)) for move in full]
    full = fix_check_info(board_size, color, applied_moves)
    full = fix_ambiguities(pieces, full)
    return full


def fix_ambiguities(pieces: List[Piece], full: List[Move]) -> List[Move]:
    """Adds additional information to the moves if some of them are equals"""
    print(pieces)
    print(full)
    # Todo: Implement this
    return full


def fix_check_info(board_size: int, color: Color, applied_moves: List[Tuple[Move, List[Piece]]]) -> List[Move]:
    """Adds a + at the end of the moves that cause a check to the opponent
        or a # if it's a checkmate
        and removes the moves that cause a check to me"""
    result: List[Move] = []
    enemy_color = Color.BLACK if color == Color.WHITE else Color.WHITE
    for move in applied_moves:
        # Skip if my king is in check
        if is_king_in_check(board_size, move[1], color):
            continue
        if is_king_in_check(board_size, move[1], enemy_color):
            king = [piece for piece in move[1] if piece.color == enemy_color and piece.name == "K"]
            king_moves = get_moves(board_size, king[0], move[1])
            if len(king_moves) == 0:
                # checkmate -> add #
                result.append(copy_move(move[0], Check.CHECKMATE))
            else:
                # check -> add +
                result.append(copy_move(move[0], Check.CHECK))
        else:
            result.append(move[0])
    return result


def is_king_in_check(board_size: int, pieces: List[Piece], color: Color) -> bool:
    """Returns true if on this board the king of the given color is in check"""
    full: List[Move] = reduce(lambda x, y: x + y,
                              [get_moves(board_size, piece, pieces) for piece in pieces if piece.color != color], [])
    my_king: List[Piece] = [piece for piece in pieces if piece.color == color and piece.name == "K"]
    if len(my_king) == 1:
        return len([move for move in full if move.coord == my_king[0].coord]) > 0
    return False
