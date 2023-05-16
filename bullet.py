import pygame

#gun properties
class Bullet(pygame.sprite.Sprite):

    def __init__(self, screen, gun):
        """create bullet in gun position"""
        super(Bullet, self).__init__()
        self.screen = screen
        self.rect = pygame.Rect(0, 0, 50, 12)
        self.color = 255, 0, 0
        self.speed = 1
        self.rect.centerx = gun.rect.centerx
        self.rect.top = gun.rect.top
        self.y = float(self.rect.y)

    def update(self):
        """up byllet move"""
        self.y -= self.speed
        self.rect.y = self.y

    def draw_bullet(self):
        """draw bullet on the screen"""
        pygame.draw.rect(self.screen, self.color, self.rect)
