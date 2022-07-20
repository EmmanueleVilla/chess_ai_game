from functools import reduce
from typing import List, Tuple, Set, Union

from board import search_by_indexes
from castling import Castling
from check import Check
from color import Color
from move import Move, copy_move_edit_promotion, copy_move_edit_check
from moves_applier import apply_move
from moves_utils import get_moves_with_direction
from piece import Piece


def get_moves(board_size: int, piece: Piece, pieces: Set[Piece], should_check_castling: bool) -> List[Move]:
    """Returns the available moves of the given piece in the given board"""
    if piece.name == "P":
        return get_moves_pawn(board_size, piece, pieces)

    if piece.name == "R":
        return get_moves_rook(board_size, piece, pieces)

    if piece.name == "N":
        return get_moves_knight(board_size, piece, pieces)

    if piece.name == "B":
        return get_moves_bishop(board_size, piece, pieces)

    if piece.name == "Q":
        return get_moves_queen(board_size, piece, pieces)

    if piece.name == "K":
        return get_moves_king(board_size, piece, pieces, should_check_castling)

    return []


def get_moves_pawn(board_size: int, piece: Piece, pieces: Set[Piece]) -> List[Move]:
    """Returns the available moves of the given pawn in the given board"""
    direction = -1 if piece.color == Color.BLACK else 1

    forward: List[Move] = get_moves_with_direction(board_size, piece, pieces, 0, direction, 1 if piece.moved else 2,
                                                   stop_on_enemy=True)
    right: List[Move] = get_moves_with_direction(board_size, piece, pieces, 1, direction, 1,
                                                 only_on_enemy=True)
    left: List[Move] = get_moves_with_direction(board_size, piece, pieces, -1,
                                                direction, 1,
                                                only_on_enemy=True)
    result: List[Move] = []
    for move in forward + right + left:
        if (piece.color == Color.WHITE and move.j == 8) or (piece.color == Color.BLACK and move.j == 1):
            result.append(copy_move_edit_promotion(move, "Q"))
            result.append(copy_move_edit_promotion(move, "N"))
            result.append(copy_move_edit_promotion(move, "R"))
            result.append(copy_move_edit_promotion(move, "B"))
        else:
            result.append(move)

    # Todo: add en-passant capture
    return result


def get_moves_rook(board_size: int, piece: Piece, pieces: Set[Piece]) -> List[Move]:
    """Returns the available moves of the given rook in the given board"""
    deltas = [(0, 1), (0, -1), (1, 0), (-1, 0)]
    return get_moves_from_deltas(board_size, piece, pieces, deltas)


def get_moves_bishop(board_size: int, piece: Piece, pieces: Set[Piece]) -> List[Move]:
    """Returns the available moves of the given bishop in the given board"""
    deltas = [(1, 1), (1, -1), (-1, 1), (-1, -1)]
    return get_moves_from_deltas(board_size, piece, pieces, deltas)


def get_moves_knight(board_size: int, piece: Piece, pieces: Set[Piece]) -> List[Move]:
    """Returns the available moves of the given knight in the given board"""
    deltas = [(2, 1), (2, -1), (-2, 1), (-2, -1), (1, 2), (1, -2), (-1, 2), (-1, -2)]
    return get_moves_from_deltas_with_max_distance(board_size, piece, pieces, deltas, 1)


def get_moves_queen(board_size: int, piece: Piece, pieces: Set[Piece]) -> List[Move]:
    """Returns the available moves of the given queen in the given board"""
    deltas = [(0, 1), (0, -1), (1, 0), (-1, 0), (1, 1), (1, -1), (-1, 1), (-1, -1)]
    return get_moves_from_deltas(board_size, piece, pieces, deltas)


def get_moves_king(board_size: int, piece: Piece, pieces: Set[Piece], should_check_castling: bool) -> List[Move]:
    """Returns the available moves of the given king in the given board"""
    deltas = [(0, 1), (0, -1), (1, 0), (-1, 0), (1, 1), (1, -1), (-1, 1), (-1, -1)]
    moves = get_moves_from_deltas_with_max_distance(board_size, piece, pieces, deltas, 1)
    castling: List[Move] = []
    if should_check_castling and not piece.moved:
        available_rooks = [rook for rook in pieces if rook.name == "R" and rook.color == piece.color and not rook.moved]
        if len(available_rooks) > 0:
            enemy_moves = get_all_moves(board_size, pieces, Color.WHITE if piece.color == Color.BLACK else Color.BLACK,
                                        False)
            for rook in available_rooks:
                castle = check_castling(board_size, piece, rook, pieces, enemy_moves)
                if castle is not None:
                    castling.append(castle)
    # Todo: Add castling
    return moves + castling


def check_castling(board_size: int, piece: Piece, rook: Piece, pieces: Set[Piece], enemy_moves: List[Move]) \
        -> Union[Move, None]:
    """Returns the castling move, if available"""
    j = 1 if piece.color == Color.WHITE else 8
    is_to_be_searched = [2, 3, 4] if rook.i == 1 else [7, 6]
    for i_to_be_searched in is_to_be_searched:
        if search_by_indexes(pieces, i_to_be_searched, j) is not None:
            return None
    if is_king_in_check(board_size, pieces, piece.color):
        return None
    is_to_be_checked = [1, 2, 3, 4] if rook.i == 1 else [8, 7, 6]
    for i_to_be_checked in is_to_be_checked:
        if len([move for move in enemy_moves if move.i == i_to_be_checked and move.j == j]) > 0:
            return None
    return Move(piece, 0, 0, False, Check.NONE, "", Castling.QUEEN_SIDE if rook.i == 1 else Castling.KING_SIDE)


def get_moves_from_deltas(board_size: int, piece: Piece, pieces: Set[Piece], deltas: List[Tuple[int, int]]) \
        -> List[Move]:
    """Returns the available moves of the given piece in the given directions with standard breaks"""
    return reduce(lambda x, y: x + y,
                  [get_moves_with_direction(board_size, piece, pieces, d[0], d[1], board_size) for d in deltas])


def get_moves_from_deltas_with_max_distance(board_size: int, piece: Piece, pieces: Set[Piece],
                                            deltas: List[Tuple[int, int]], max_distance: int) -> List[Move]:
    """Returns the available moves of the given piece in the given directions with standard breaks"""
    return reduce(lambda x, y: x + y,
                  [get_moves_with_direction(board_size, piece, pieces, d[0], d[1], max_distance) for d in deltas])


def get_all_moves(board_size: int, pieces: Set[Piece], color: Color, deep_check: bool = True) -> List[Move]:
    """Returns all the possible moves on the board for the given pieces of the given color"""
    full: List[Move] = reduce(lambda x, y: x + y,
                              [get_moves(board_size, piece, pieces, deep_check) for piece in pieces if
                               piece.color == color], [])
    applied_moves = [(move, apply_move(pieces, move)) for move in full]
    full = fix_check_info(board_size, color, applied_moves, deep_check)
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


def fix_check_info(board_size: int, color: Color, applied_moves: List[Tuple[Move, Set[Piece]]],
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


def is_king_in_check(board_size: int, pieces: Set[Piece], color: Color) -> bool:
    """Returns true if on this board the king of the given color is in check"""
    full: List[Move] = reduce(lambda x, y: x + y,
                              [get_moves(board_size, piece, pieces, False) for piece in pieces if piece.color != color],
                              [])
    my_king: List[Piece] = [piece for piece in pieces if piece.color == color and piece.name == "K"]
    if len(my_king) == 1:
        return len([move for move in full if move.i == my_king[0].i and move.j == my_king[0].j]) > 0
    return False
