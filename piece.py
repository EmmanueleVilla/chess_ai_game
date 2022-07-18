from typing import Any

from color import Color
from coord import Coord


def to_letter(coordinate: int) -> str:
    """Returns the i coordinate as a letter"""
    assert 0 < coordinate < 9
    letters = "a b c d e f g h".split(" ")
    return letters[coordinate - 1]


class Piece:
    """Represents a piece on the board"""

    def i(self) -> int:
        """Returns the i coordinate"""
        return self.coord.i

    def j(self) -> int:
        """Returns the j coordinate"""
        return self.coord.j

    def __init__(self, color: Color, name: str, i: int, j: int, moved: bool = False):
        self.color = color
        self.name = name
        self.coord = Coord(i, j)
        self.moved = moved

    def __eq__(self, obj: Any) -> bool:
        return (
                isinstance(obj, Piece)
                and obj.coord == self.coord
                and obj.color == self.color
                and obj.name == self.name
        )

    def __str__(self) -> str:
        return f'{self.name}{self.color}: {to_letter(self.i())}{self.j()}'
