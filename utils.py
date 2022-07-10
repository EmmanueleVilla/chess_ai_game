from board import search_by_indexes


def print_board(pieces):
    """Prints the board"""
    board_size = 8
    gray = '\033[90m'
    white = '\033[0m'
    color_map = {
        'B': '\033[94m',
        'W': '\033[92m'
    }
    for j in reversed(range(1, board_size + 1)):
        print(f'{gray}[{j}]{white}', end="")
        for i in range(1, board_size + 1):
            piece = search_by_indexes(pieces, i, j)
            output = "["
            if piece is not None:
                output += color_map[piece.color]
                output += piece.name
                output += white
            else:
                output += " "
            output += "]"
            print(output, end="")
        print("")
    print(gray + "   [a][b][c][d][e][f][g][h]" + white)
