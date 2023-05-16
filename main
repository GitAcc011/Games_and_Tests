import pygame
import controls
from assault_rifle import Assault_rifle
from pygame.sprite import Group
from stats import Stats
from scores import Scores


def run():
    pygame.init()
    screen = pygame.display.set_mode((700, 800))
    pygame.display.set_caption("Star defenders")
    bg_color = (0, 0, 0)
    gun = Assault_rifle(screen)
    bullets = Group()
    alliens = Group()
    controls.create_army(screen, alliens)
    stats = Stats()
    sc = Scores(screen, stats)

    while True:
        controls.events(screen, gun, bullets)
        if stats.run_game:
            gun.update_gun()
            bullets.update()
            controls.update(bg_color, screen, stats, sc, gun, alliens, bullets)
            controls.update_bullets(screen, stats, sc, alliens, bullets)
            controls.update_alliens(stats, screen, sc, gun, alliens, bullets)

if __name__ == '__main__':
    run()
