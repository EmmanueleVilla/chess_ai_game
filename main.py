import sys

from game import start_game


def print_help() -> None:
    """Prints the usage of this main"""
    print("Usage: main.py {first_ia_path} {second_ia_path}")


def main() -> None:
    """Main function"""
    args = sys.argv[1:]

    if (args[0] == "-h") or (args[0] == "--help"):
        print_help()
    else:
        start_game(args)


main()
