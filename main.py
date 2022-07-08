from ast import For
import subprocess
import sys

from board import BOARD_SIZE, search_by_indexes
from colors import colors

first_ia = ""
second_ia = ""

def print_help():
    print("Usage: main.py {first_ia_path} {second_ia_path}")

def play_turn(cmd):
    with subprocess.Popen(cmd, stdout=subprocess.PIPE, bufsize=1, universal_newlines=True, shell = True) as p:
        for line in p.stdout:
            print(line)

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
        second_ia = args[1]
        print_board();
        play_turn(args[0]);
        print_board();

main()