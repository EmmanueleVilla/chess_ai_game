import sys
from random import choice

import jsonpickle  # type: ignore

from game_state import GameState


def main() -> None:
    """Main method"""
    args = sys.argv[1:]
    msg = ""
    with open(args[0], encoding="utf-8") as message:
        msg = message.read()
    state: GameState = jsonpickle.decode(msg, classes=GameState)

    # Try to checkmate
    move = [move for move in state.moves if "#" in move.to_an()]
    if len(move) > 0:
        print(move[0].to_an())
        sys.exit()

    # Try to check
    move = [move for move in state.moves if "+" in move.to_an()]
    if len(move) > 0:
        print(move[0].to_an())
        sys.exit()

    # Try to capture
    move = [move for move in state.moves if "x" in move.to_an()]
    if len(move) > 0:
        print(move[0].to_an())
        sys.exit()

    # Random fallback
    print(choice(state.moves).to_an())
    sys.exit()


main()
