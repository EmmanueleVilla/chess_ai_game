import sys
from random import choice

import jsonpickle

from game_state import GameState


def main() -> None:
    """Main method"""
    args = sys.argv[1:]
    message = open(args[0]).read()
    state: GameState = jsonpickle.decode(message, classes=GameState)
    print(choice(state.moves).to_an())


main()
sys.exit()
