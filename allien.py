import pygame

class Allien(pygame.sprite.Sprite):
    """allien actions"""
    def __init__(self, screen):
        """start position"""
        super(Allien, self).__init__()
        self.screen = screen
        self.image = pygame.image.load('assets/pictures/allien2.png')
        self.rect = self.image.get_rect()
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height
        self.x = float(self.rect.x)
        self.y = float(self.rect.y)

    def draw(self):
        """show alien"""
        self.screen.blit(self.image, self.rect)

    def update(self):
        """allies move"""
        self.y += 0.1
        self.rect.y = self.y
