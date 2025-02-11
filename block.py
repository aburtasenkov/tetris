import pygame
import typing
import numpy

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

    # move in position
    def move_ip(self, pos: tuple[int, int]) -> typing.Self:
        self.outline.move_ip(pos[0], pos[1])
        self.area.move_ip(pos[0] + OUTLINE_SIZE, pos[1] + OUTLINE_SIZE)
        return self

class Shape(Moving_Block):
    def __init__(self, pos: tuple[int, int], size: tuple[int, int], outline_color = black, area_color = None):
        super().__init__(pos, size, outline_color, area_color)

        self.matrix = numpy.array(
            [[None] * 5] * 5, dtype=bool
        )
    
    def draw(self, screen: pygame.Surface) -> None:
        # TODO
        return

class I_Shape(Shape):
    def __init__(self, pos: tuple[int, int], size: tuple[int, int], outline_color = black, area_color = None):
        super().__init__(pos, size, outline_color, area_color)

        self.matrix = I_SHAPE_MATRIX

        for array in self.matrix:
            for b in array:
                if b:
                    print(1, end=" ")
                else:
                    print(0, end=" ")
            print()

def copy_block(block: Stationary_Block) -> Stationary_Block:
    new_block = Stationary_Block(block.outline.topleft,
                                 (block.outline.topright[0] - block.outline.topleft[0], block.outline.bottomleft[1] - block.outline.topleft[1]), 
                                 block.outline_color,
                                 block.area_color
                                )
    return new_block