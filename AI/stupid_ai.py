import sys
from random import choice
from typing import List


class MoveString:
    """Move from the main program"""

    def __init__(self, an_string: str):
        self.an_string = an_string


class Message:
    """Message from the main program"""

    def __init__(self, moves: List[MoveString]):
        self.moves = moves


def main() -> None:
    """Main method"""
    args = sys.argv[1:]
    msg = ""
    with open(args[0], encoding="utf-8") as message:
        msg = message.read()

    moves = msg.split("moves")[1].split("\n")
    moves = [move for move in moves if move != ""]
    # Try to checkmate
    move = [move for move in moves if "#" in move]
    if len(move) > 0:
        print(move[0])
        sys.exit()

    # Try to check
    move = [move for move in moves if "+" in move]
    if len(move) > 0:
        print(move[0])
        sys.exit()

    # Try to capture
    move = [move for move in moves if "x" in move]
    if len(move) > 0:
        print(move[0])
        sys.exit()

    # Random fallback
    print(choice(moves))
    sys.exit()


main()
