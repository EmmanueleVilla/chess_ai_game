from typing import Any

from color import Color

letter_memo = {}


def to_letter(coordinate: int) -> str:
    """Returns the i coordinate as a letter"""
    if coordinate not in letter_memo:
        letters = "a b c d e f g h".split(" ")
        letter_memo[coordinate] = letters[coordinate - 1]
    return letter_memo[coordinate]


class Piece:
    """Represents a piece on the board"""

    def __init__(self, color: Color, name: str, i: int, j: int, moved: bool = False):
        self.color = color
        self.name = name
        self.i = i
        self.j = j
        self.moved = moved

    def __eq__(self, obj: Any) -> bool:
        return (
                isinstance(obj, Piece)
                and obj.i == self.i
                and obj.j == self.j
                and obj.color == self.color
                and obj.name == self.name
        )

    def __str__(self) -> str:
        return f'{self.name}{"B" if self.color == Color.BLACK else "W"}: {to_letter(self.i)}{self.j}'
