import sys
import pygame
import controls

from pygame.sprite import Group
from main_menu import Menu


def run():
    pygame.init()
    screen = pygame.display.set_mode((900, 840)) # 600, 840
    pygame.display.set_caption("Tetris")
    is_running = True
    bg_color = "grey"
    white = (255, 255, 255)
    main_menu = Menu(screen)
    main_menu.append_option("Start", lambda: print("Game Started"))
    main_menu.append_option("Quit", lambda: quit())

    while is_running:
        controls.events(screen, main_menu)
        screen.fill(bg_color)
        pygame.draw.rect(screen, white, (0, 0, 440, 840), 40)
        pygame.draw.rect(screen, bg_color, (40, 0, 360, 40), 40)
        main_menu.draw(screen, 100, 100, 75)
        pygame.display.flip()

if __name__ == '__main__':
    run()