from ast import For
import sys

from board import BOARD_SIZE, search_by_indexes
from colors import colors


def print_help():
    print("Usage: main.py {first_ia_path} {second_ia_path}")

def print_board():
    for i in range(BOARD_SIZE):
        for j in range(BOARD_SIZE):
            piece = search_by_indexes(i,j)
            output = "["
            if(piece != None):
                output += piece.color
                output += piece.type[0]
                output += colors.ENDC
            else:
                output += " "
            output += "]"
            print(output, end = "")
        print("")

def main():
    args = sys.argv[1:]

    if(args[0] == "-h") or (args[0] == "--help"):
        print_help();
    else:
        print_board();

main()