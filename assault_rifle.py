import pygame
from pygame.sprite import Sprite

#gun properties
class Assault_rifle(Sprite):

    def __init__(self, screen):
        """init"""
        super(Assault_rifle, self).__init__()
        self.screen = screen
        self.image = pygame.image.load('assets/pictures/tetris_brick.png')
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()
        self.rect.centerx = self.screen_rect.centerx
        self.center = float(self.rect.centerx)
        self.rect.bottom = self.screen_rect.bottom
        self.mright = False
        self.mleft = False

    def output(self):
        """"drew gun"""
        self.screen.blit(self.image, self.rect)

    def update_gun(self):
        """update gun position"""
        if self.mright and self.rect.right < self.screen_rect.right:
            self.center += 1.5
        if self.mleft and self.rect.left > 0:
            self.center -= 1.5

        self.rect.centerx = self.center

    def create_gun(self):
        """create gun on center"""
        self.center = self.screen_rect.centerx