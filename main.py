import subprocess
import sys

from board import BOARD_SIZE, search_by_indexes
from colors import Colors

FIRST_IA = ""
SECOND_IA = ""

def print_help():
    """Prints the usage of this main"""
    print("Usage: main.py {first_ia_path} {second_ia_path}")

def play_turn(cmd):
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

def print_board():
    """Prints the board"""
    for i in range(BOARD_SIZE):
        for j in range(BOARD_SIZE):
            piece = search_by_indexes(i,j)
            output = "["
            if piece is not None:
                output += piece.color
                output += piece.name
                output += Colors.ENDC
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
        print_board()
        play_turn(args[0])
        print_board()

main()
