from typing import Set

import pygame

from board import search_by_indexes
from color import Color
from piece import Piece


def show_board(screen: pygame.surface.Surface, board_size: int, pieces: Set[Piece], log_path: str) -> None:
    """Shows the board in the pygame window"""
    screen.fill((0, 0, 0))
    red = (200, 97, 120)
    gray = (144, 144, 144)
    cell_size = 90
    count = 0
    for j in range(1, board_size + 1):
        for i in range(1, board_size + 1):
            rect = pygame.Rect((i - 1) * cell_size, cell_size * 7 - cell_size * (j - 1), cell_size, cell_size)
            pygame.draw.rect(screen, red if count % 2 == 0 else gray, rect)
            piece = search_by_indexes(pieces, i, j)
            if piece is not None:
                image = pygame.image.load(f'images/{piece.name}{"B" if piece.color == Color.BLACK else "W"}.svg')
                image = pygame.transform.scale(image, (cell_size, cell_size))
                screen.blit(image, rect)
            count += 1
        count += 1

    with open(log_path, encoding="utf-8") as logs_game:
        font = pygame.font.SysFont(None, 24)  # type: ignore
        lines = logs_game.read().split("\n")
        height = 10
        for line in lines:
            img = font.render(line, True, (255, 255, 255))
            screen.blit(img, (800, height))
            height += 20

    pygame.display.flip()
    pygame.event.pump()


def print_board(board_size: int, pieces: Set[Piece]) -> None:
    """Prints the board"""
    print(board_to_string(board_size, pieces))


def board_to_string(board_size: int, pieces: Set[Piece]) -> str:
    """Returns a string representation of the board"""
    result: str = ""
    gray = '\033[90m'
    white = '\033[0m'
    color_map = {
        Color.BLACK: '\033[94m',
        Color.WHITE: '\033[92m'
    }
    for j in reversed(range(1, board_size + 1)):
        result += f'{gray}[{j}]{white}'
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
            result += output
        result += "\n"
    result += gray + "   [a][b][c][d][e][f][g][h]" + white
    return result + "\n"
