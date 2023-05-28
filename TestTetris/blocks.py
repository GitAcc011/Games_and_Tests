import pygame
from copy import deepcopy
from random import choice, randrange
import controls


class Block(pygame.sprite.Sprite):
    """create bullet in gun position"""
    def __init__(self, screen, height, width, block_size, grid, blocks_positions, field, font):
        super(Block, self).__init__()
        self.height = height
        self.width = width
        self.block_size = block_size
        self.screen = screen
        self.grid = grid
        self.field = field
        self.blocks_positions = blocks_positions
        self.rect = pygame.Rect(0, 0, 40, 40)
        self.anim_count, self.anim_speed, self.anim_limit = 0, 60, 2000
        self.line = self.height - 1
        self.score = 0
        self.font = font

        self.figures = [[pygame.Rect(x + width // 2, y + 1, 1, 1) for x, y in fig_pos]
                        for fig_pos in self.blocks_positions]
        self.figure_rect = pygame.Rect(0, 0, block_size - 2, block_size - 2)

        self.get_color = lambda: (randrange(30, 256), randrange(30, 256), randrange(30, 256))
        self.figure = deepcopy(choice(self.figures))
        self.color = self.get_color()


    def update_x_y(self, dx):
        """borders check"""
        figure_old = deepcopy(self.figure)
        for i in range(4):
            self.figure[i].x += dx
            if not self.check_borders():
                self.figure = deepcopy(figure_old)
                break


    def update(self):
        """update screen"""
        self.anim_count += self.anim_speed
        if self.anim_count > self.anim_limit:
            self.anim_count = 0
            figure_old = deepcopy(self.figure)
            for i in range(4):
                self.figure[i].y += 1
                if not self.check_borders():
                    for i in range(4):
                        self.field[figure_old[i].y][figure_old[i].x] = pygame.Color(self.color)
                    self.color = self.get_color()
                    self.figure = deepcopy(choice(self.figures))
                    self.anim_limit = 2000
                    break
        self.draw_figure_on_field()
        self.delete_line()
        for i in range(self.width):
            if self.field[0][i]:
                self.game_over()
                self.score = 0


    def delete_line(self):
        """check lines"""
        line = self.height - 1
        for row in range(self.height - 1, -1, -1):
            count = 0
            for i in range(self.width):
                if self.field[row][i]:
                    count += 1
                self.field[line][i] = self.field[row][i]
            if count < self.width:
                line -= 1
            else:
                self.anim_speed += 3
                self.score += 100
        # current score
        score = self.font.render("Score:", True, pygame.Color('white'))
        self.screen.blit(score, (500, 400))
        title = self.font.render(str(self.score), True, pygame.Color('white'))
        self.screen.blit(title, (550, 480))


    def check_borders(self):
        """borders check again"""
        for i in range(len(self.figure)):
            if self.figure[i].x < 0 or self.figure[i].x > self.width - 1:
                return False
            elif self.figure[i].y > self.height - 1 or \
                    self.field[self.figure[i].y][self.figure[i].x]:
                return False
        return True


    def create_block(self):
        """create block on center"""
        for i in range(4):
            self.figure_rect.x = self.figure[i].x * self.block_size
            self.figure_rect.y = self.figure[i].y * self.block_size
            pygame.draw.rect(self.screen, pygame.Color(self.color), self.figure_rect)


    def rotate_block(self):
        """block rotation"""
        center = self.figure[0]
        figure_old = deepcopy(self.figure)
        for i in range(4):
            x = self.figure[i].y - center.y
            y = self.figure[i].x - center.x
            self.figure[i].x = center.x - x
            self.figure[i].y = center.y + y
            if not self.check_borders():
                self.figure = deepcopy(figure_old)
                break


    def draw_figure_on_field(self):
        """draw figure on field"""
        for y, raw in enumerate(self.field):
            for x, col in enumerate(raw):
                if col:
                    self.figure_rect.x = x * self.block_size
                    self.figure_rect.y = y * self.block_size
                    pygame.draw.rect(self.screen, pygame.Color("blue"), self.figure_rect)


    def game_over(self):
        """game ended"""
        controls.write_score(self.score)
        self.field = [[0 for i in range(self.width)] for i in range(self.height)]
        self.anim_count, self.anim_speed, self.anim_limit = 0, 60, 2000
        score = 0

