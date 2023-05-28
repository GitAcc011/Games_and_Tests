import time
import pygame
import sys
import main_menu
from blocks import Block
import blocks


def events(screen, main_menu, block):
    """events processes"""
    # left-right move
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            quit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                main_menu.switch(-1)
            elif event.key == pygame.K_DOWN:
                main_menu.switch(1)
            elif event.key == pygame.K_SPACE:
                if not main_menu.start_clicked():
                    main_menu.select()
            elif event.key == pygame.K_w:
                block.rotate_block()
            elif event.key == pygame.K_s:
                block.anim_limit = 100
            elif event.key == pygame.K_a:
                block.update_x_y(-1)
            elif event.key == pygame.K_d:
                block.update_x_y(1)


def update(background, game_bg, screen, main_menu, tetris_title):
    """"screen update"""
    screen.blit(background, (0, 0))
    screen.blit(game_bg, (0, 0))
    main_menu.draw(screen, 220, 300, 75)
    screen.blit(tetris_title, (500, 20))


def update_blocks(screen, grid, block):
    """"blocks update"""
    block.create_block()
    [pygame.draw.rect(screen, (40, 40, 40), i_rect, 1) for i_rect in grid]
    block.update()


def write_score(score):
    """write or create .txt with score"""
    try:
        with open('assets/data/high_score.txt', 'r') as f:
            current_score = int(f.readline())
        if score > current_score:
            with open('assets/data/high_score.txt', 'w') as f:
                f.write(str(score))
    except FileNotFoundError:
        with open('assets/data/high_score.txt', 'w') as f:
            f.write(score)


def show_highscore(screen, font, tetris_score_title):
    """create .txt with score or write record"""
    current_score = 0
    try:
        with open('assets/data/high_score.txt', 'r') as f:
            current_score = int(f.readline())
    except FileNotFoundError:
        with open('assets/data/high_score.txt', 'w') as f:
            f.write("0")
        with open('assets/data/high_score.txt', 'r') as f:
            current_score = int(f.readline())
    screen.blit(tetris_score_title, (500, 200))
    title = font.render(str(current_score), True, pygame.Color('white'))
    screen.blit(title, (550, 280))

