from board import search_by_indexes


def print_board(pieces):
    """Prints the board"""
    board_size = 8
    color_map = {
        'B': '\033[94m',
        'W': '\033[92m'
    }
    for i in range(board_size):
        for j in range(board_size):
            piece = search_by_indexes(pieces, i, j)
            output = "["
            if piece is not None:
                output += color_map[piece.color]
                output += piece.name
                output += '\033[0m'
            else:
                output += " "
            output += "]"
            print(output, end="")
        print("")
