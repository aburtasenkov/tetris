import pygame

from colors import *
from constants import *

class Block:
    def __init__(self, pos_tuple, size_tuple, outline_color = black, area_color = random_color()):
        self.outline_color = outline_color
        self.area_color = area_color

        self.outline = pygame.Rect(pos_tuple, size_tuple)
        self.area = pygame.Rect((pos_tuple[0] + OUTLINE_SIZE, pos_tuple[1] + OUTLINE_SIZE), (size_tuple[0] - OUTLINE_SIZE * 2, size_tuple[1] - OUTLINE_SIZE * 2))

    def move(self, speed_tuple):
        self.outline = self.outline.move(speed_tuple[0], speed_tuple[1])
        self.area = self.area.move(speed_tuple[0], speed_tuple[1])
        return self

    def draw(self, screen):
        pygame.draw.rect(screen, self.outline_color, self.outline, border_radius=OUTLINE_BORDER_RADIUS)      # draw outline of piece
        pygame.draw.rect(screen, self.area_color, self.area, border_radius=INNER_BORDER_RADIUS)    # draw inner color
        return

