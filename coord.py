from typing import Any


class Coord:
    """Represents a coordinate on the board"""

    def __init__(self, i: int, j: int):
        self.i = i
        self.j = j

    def __eq__(self, obj: Any) -> bool:
        return isinstance(obj, Coord) and obj.i == self.i and obj.j == self.j

    def __str__(self) -> str:
        return f'{self.i}{self.j}'
