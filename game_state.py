class GameState:
    """Represents the game state"""

    def __init__(self, board_size, turn_number, turn_color, pieces):
        self.board_size = board_size
        self.turn_number = turn_number
        self.turn_color = turn_color
        self.pieces = pieces
