import os
from datetime import datetime

an_filename = "/an.txt"
board_filename = "/board.txt"
message_filename = "/message.txt"


def get_session_id() -> str:
    """Initialize a new session, creates the logs and returns its id"""
    date = datetime.now()
    session_id = f'{date.year}_{date.month:02d}_{date.day:02d}' \
                 f'_{date.hour:02d}_{date.minute:02d}_{date.second:02d}_{date.microsecond:02d}'
    path = f'logs/{session_id}'
    return path


def init_files(path: str) -> None:
    """Initialize the log files at the given path"""
    os.makedirs(path)
    logs_an = open(path + an_filename, "x")
    logs_an.close()
    logs_board = open(path + board_filename, "x")
    logs_board.close()
    message_game = open(path + message_filename, "x")
    message_game.close()


def write_board(path: str, board: str) -> None:
    """Appends the board to the given file"""
    logs_board = open(path + board_filename, "a")
    logs_board.write(board)
    logs_board.close()


def write_an(path: str, turn: str) -> None:
    """Appends the an_log to the given file"""
    logs_an = open(path + an_filename, "a")
    logs_an.write(turn)
    logs_an.close()


def write_message(path: str, message: str) -> None:
    """Replace the message in the given file"""
    message_game = open(path, "w")
    message_game.write(message)
    message_game.close()
