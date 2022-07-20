class GameResult:
    """Represents the game result"""

    def __init__(self, white: float, black: float, message: str):
        self.white = white
        self.black = black
        self.message = message

    def get_white(self) -> str:
        """Return the string representation of the points"""
        if self.white == 0.5:
            return "1/2"

        return f'{self.white}'

    def get_black(self) -> str:
        """Return the string representation of the points"""
        if self.black == 0.5:
            return "1/2"

        return f'{self.black}'
