import sys
import pygame
import controls
from blocks import Block
from pygame.sprite import Group
from main_menu import Menu
import numpy as np


def run():
    """game run"""
    pygame.init()
    width, height = 10, 20
    block_size = 45
    main_res = 750, 900
    window_w, window_h = block_size * width, block_size * height

    pygame.display.set_caption("Tetris")
    screen = pygame.display.set_mode(main_res)
    game_screen = pygame.Surface((window_w, window_h))
    background_img = pygame.image.load('assets/images/space_bg1.jpg').convert()
    game_bg_img = pygame.image.load('assets/images/space_bg2.jpg').convert()
    font = pygame.font.Font('assets/fonts/appetite.ttf', 70)
    score_font = pygame.font.Font('assets/fonts/appetite.ttf', 50)
    tetris_title = font.render("Tetris", True, pygame.Color('cyan'))
    tetris_score_title = font.render("Record:", True, pygame.Color('white'))

    field = np.zeros((height, width))
    grid = [pygame.Rect(x * block_size, y * block_size, block_size, block_size) for x in range(width) for y in range(height)]
    blocks_positions = [[(-1, 0), (-2, 0), (0, 0), (1, 0)],
                             [(0, -1), (-1, -1), (-1, 0), (0, 0)],
                             [(-1, 0), (-1, 1), (0, 0), (0, -1)],
                             [(0, 0), (-1, 0), (0, 1), (-1, -1)],
                             [(0, 0), (0, -1), (0, 1), (-1, -1)],
                             [(0, 0), (0, -1), (0, 1), (1, -1)],
                             [(0, 0), (0, -1), (0, 1), (-1, 0)]]
    block = Block(screen, height, width, block_size, grid, blocks_positions, field, font)
    blocks = Group()

    main_menu = Menu(screen)
    main_menu.append_option("Start", lambda: game_start(main_menu))
    # main_menu.append_option("Leadearboard", lambda: show_leadears(main_menu))
    main_menu.append_option("Quit", lambda: quit())

    while True:
        start = main_menu.start_clicked()
        controls.events(screen, main_menu, block)
        controls.update(background_img, game_bg_img, screen, main_menu, tetris_title)
        if start:
            controls.update_blocks(screen, grid, block)
            controls.show_highscore(screen, font, tetris_score_title)

        pygame.display.flip()
        pygame.time.Clock().tick(60)


def game_start(main_menu):
    main_menu.delete_options()


def show_menu(main_menu):
    """show menu"""
    main_menu.delete_options()
    main_menu.append_option("Start", lambda: game_start(main_menu))
    main_menu.append_option("Quit", lambda: quit())


if __name__ == '__main__':
    """starts point"""
    run()