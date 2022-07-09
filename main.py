import subprocess
import sys

from board import build_pieces, search_by_indexes

FIRST_IA = ""
SECOND_IA = ""

def print_help():
    """Prints the usage of this main"""
    print("Usage: main.py {first_ia_path} {second_ia_path}")

def play_turn(pieces, cmd):
    """Plays the turn with the given executable command"""
    with subprocess.Popen(
        cmd,
        stdout=subprocess.PIPE,
        bufsize=1,
        universal_newlines=True,
        shell = True
        ) as process:
        for line in process.stdout:
            print(line)
    return pieces

def play(board_size, args):
    """Starts the game"""
    pieces = build_pieces(board_size)
    print_board(pieces)
    pieces = play_turn(pieces, args[0])
    print_board(pieces)

def print_board(pieces):
    """Prints the board"""
    board_size = 8
    color_map = {
        'B':'\033[94m',
        'W':'\033[92m'
    }
    for i in range(board_size):
        for j in range(board_size):
            piece = search_by_indexes(pieces, i,j)
            output = "["
            if piece is not None:
                output += color_map[piece.color]
                output += piece.name
                output += '\033[0m'
            else:
                output += " "
            output += "]"
            print(output, end = "")
        print("")

def main():
    """Main function"""
    args = sys.argv[1:]

    if(args[0] == "-h") or (args[0] == "--help"):
        print_help()
    else:
        play(8, args)

main()
