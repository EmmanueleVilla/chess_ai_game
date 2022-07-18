from enum import Enum


class Check(Enum):
    """Enum representing the check states"""
    NONE = 1
    CHECK = 2
    CHECKMATE = 3
