import time
import pygame
import sys
import main_menu


def events(screen, main_menu):
    """events processes"""
    # left-right move
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            screen.is_running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_w:
                main_menu.switch(-1)
            elif event.key == pygame.K_s:
                main_menu.switch(1)
            elif event.key == pygame.K_SPACE:
                main_menu.select()


def update(bg_color, screen, stats, score, gun, alliens, bullets):
    """"screen update"""
    screen.fill(bg_color)
    score.show_score()
    for bullet in bullets.sprites():
        bullet.draw_bullet()
    gun.output()
    alliens.draw(screen)
    pygame.display.flip()