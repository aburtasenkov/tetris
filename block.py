import pygame
import typing

from colors import *
from constants import *

class Stationary_Block:
    def __init__(self, pos: tuple[int, int], size: tuple[int, int], outline_color = black, area_color = None):
        if (not area_color):
            area_color = random_color()

        self.outline_color = outline_color
        self.area_color = area_color

        self.outline = pygame.Rect(pos, size)
        self.area = pygame.Rect((pos[0] + OUTLINE_SIZE, pos[1] + OUTLINE_SIZE), (size[0] - OUTLINE_SIZE * 2, size[1] - OUTLINE_SIZE * 2))

    def draw(self, screen: pygame.Surface) -> None:
        pygame.draw.rect(screen, self.outline_color, self.outline, border_radius=OUTLINE_BORDER_RADIUS)      # draw outline of piece
        pygame.draw.rect(screen, self.area_color, self.area, border_radius=INNER_BORDER_RADIUS)    # draw inner color

class Moving_Block(Stationary_Block):
    def move(self, offset: tuple[int, int]) -> typing.Self:
        self.outline = self.outline.move(offset[0], offset[1])
        self.area = self.area.move(offset[0], offset[1])
        return self

    def move_ip(self, pos: tuple[int, int]) -> typing.Self:
        self.outline.move_ip(pos[0], pos[1])
        self.area.move_ip(pos[0] + OUTLINE_SIZE, pos[1] + OUTLINE_SIZE)
        return self
