from enum import Enum


class Castling(Enum):
    """Enum representing the castling states"""
    NONE = 1
    KING_SIDE = 2
    QUEEN_SIDE = 3
