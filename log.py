import os
from datetime import datetime

AN_FILENAME = "/an.txt"
BOARD_FILENAME = "/board.txt"
MESSAGE_FILENAME = "/message.txt"
GAMES_FILENAME = "/game.txt"


def get_session_id() -> str:
    """Initialize a new session, creates the logs and returns its id"""
    date = datetime.now()
    session_id = f'{date.year}_{date.month:02d}_{date.day:02d}' \
                 f'_{date.hour:02d}_{date.minute:02d}_{date.second:02d}_{date.microsecond:02d}'
    print(session_id)
    path = f'logs/{session_id}'
    return path


def init_game_log_file(base_path: str) -> None:
    """Initialize the game log file at the given path"""
    os.makedirs(base_path)
    with open(base_path + GAMES_FILENAME, "x", encoding="utf-8") as logs_game:
        logs_game.close()


def init_files(base_path: str, game_id: int) -> str:
    """Initialize the log files at the given path"""
    path = os.path.join(base_path, f'{game_id}')
    os.makedirs(path)
    with open(path + AN_FILENAME, "x", encoding="utf-8") as logs_an:
        logs_an.close()
    with open(path + BOARD_FILENAME, "x", encoding="utf-8") as logs_board:
        logs_board.close()
    with open(path + MESSAGE_FILENAME, "x", encoding="utf-8") as message_game:
        message_game.close()
    return path


def write_board(path: str, board: str) -> None:
    """Appends the board to the given file"""
    with open(path + BOARD_FILENAME, "a", encoding="utf-8") as logs_board:
        logs_board.write(board)


def write_an(path: str, turn: str) -> None:
    """Appends the an_log to the given file on the same line"""
    with open(path + AN_FILENAME, "a", encoding="utf-8") as logs_an:
        logs_an.write(turn)


def write_message(path: str, message: str) -> None:
    """Replace the message in the given file"""
    with open(path, "w", encoding="utf-8") as message_game:
        message_game.write(message)


def write_game(path: str, message: str) -> None:
    """Replace the message in the given file"""
    with open(path + GAMES_FILENAME, "a", encoding="utf-8") as logs_game:
        logs_game.write(message + "\n")
