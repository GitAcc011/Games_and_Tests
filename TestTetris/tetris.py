import sys
import pygame
import controls
import blocks
from pygame.sprite import Group
from main_menu import Menu


def run():
    pygame.init()
    width = 420
    height = 820
    screen = pygame.display.set_mode((width, height)) # 420, 820
    pygame.display.set_caption("Tetris")
    is_running = True
    bg_color = "grey"
    white = (255, 255, 255)
    main_menu = Menu(screen)
    main_menu.append_option("Start", lambda: game_start(main_menu))
    main_menu.append_option("Quit", lambda: quit())

    while is_running:
        controls.events(screen, main_menu)
        screen.fill(bg_color)
        pygame.draw.rect(screen, white, (0, 0, width, height), 20)
        main_menu.draw(screen, 100, 100, 75)
        pygame.display.flip()

def game_start(main_menu):
    main_menu.delete_options()
    print("Game Started")

if __name__ == '__main__':
    run()