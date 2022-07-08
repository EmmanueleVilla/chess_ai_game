from coord import Coord


class Move:
    start = Coord()
    end = Coord()

    def __init__(self, start, end):
        self.start = start
        self.end = end
