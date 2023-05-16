import time
import pygame
import sys
from bullet import Bullet
from allien import Allien


def events(screen, gun, bullets):
    """events processes"""
    # left-right move
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_d:
                gun.mright = True
            elif event.key == pygame.K_a:
                gun.mleft = True
            elif event.key == pygame.K_SPACE:
                new_bullet = Bullet(screen, gun)
                bullets.add(new_bullet)
        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_d:
                gun.mright = False
            elif event.key == pygame.K_a:
                gun.mleft = False


def update(bg_color, screen, stats, sc, gun, alliens, bullets):
    """"screen update"""
    screen.fill(bg_color)
    sc.show_score()
    for bullet in bullets.sprites():
        bullet.draw_bullet()
    gun.output()
    alliens.draw(screen)
    pygame.display.flip()


def update_bullets(screen, stats, sc, alliens, bullets):
    """update bullets poitions"""
    bullets.update()
    for bullet in bullets.copy():
        if bullet.rect.bottom <= 0:
            bullets.remove(bullet)
    collisions = pygame.sprite.groupcollide(bullets, alliens, True, True)
    if collisions:
        for alliens in collisions.values():
            stats.score += 10 * len(alliens)
        sc.image_score()
        check_high_score(stats, sc)
        sc.image_guns()
    if len(alliens) == 0:
        bullets.empty()
        create_army(screen, alliens)


def gun_kill(stats, screen, sc, gun, alliens, bullets):
    """gun-alliens contact"""
    if stats.guns_left > 0:
        stats.guns_left -= 1
        sc.image_guns()
        alliens.empty()
        bullets.empty()
        create_army(screen, alliens)
        gun.create_gun()
        time.sleep(1)
    else:
        stats.run_game = False
        sys.exit()


def update_alliens(stats, screen, sc, gun, alliens, bullets):
    """update allliens positions"""
    alliens.update()
    if pygame.sprite.spritecollideany(gun, alliens):
        gun_kill(stats, screen, sc, gun, alliens, bullets)
    alliens_check(stats, screen, sc, gun, alliens, bullets)


def alliens_check(stats, screen, sc, gun, alliens, bullets):
    """alliens check"""
    screen_rect = screen.get_rect()
    for allien in alliens.sprites():
        if allien.rect.bottom >= screen_rect.bottom:
            gun_kill(stats, screen, sc, gun, alliens, bullets)
            break


def create_army(screnn, alliens):
    """create all alliens"""
    allien = Allien(screnn)
    allien_width = allien.rect.width
    number_allien_x = int((700 - 2 *allien_width) / allien_width)
    allien_height = allien.rect.height
    number_allien_y = int((800 - 100 - 2 * allien_height) / allien_height)

    for row_number in range(number_allien_y - 1):
        for allien_number in range(number_allien_x):
            allien = Allien(screnn)
            allien.x = allien_width + (allien_width * allien_number)
            allien.y = allien_height + (allien_height * row_number)
            allien.rect.x = allien.x
            allien.rect.y = allien.rect.height + allien.rect.height * row_number
            alliens.add(allien)

def check_high_score(stats, sc):
    """record check"""
    if stats.score > stats.high_score:
        stats.high_score = stats.score
        sc.image_high_score()
        with open('highscore.txt', 'w') as f:
            f.write(str(stats.high_score))