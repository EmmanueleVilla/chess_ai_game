from colors import colors


class Piece:
    color = colors.BLUE
    type = ""
    i = 0
    j = 0

    def __init__(self, color, type, i, j):
        self.color = color
        self.type = type
        self.i = i
        self.j = j