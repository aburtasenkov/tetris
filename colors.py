import random

black = (0, 0, 0)
grey = (128, 128, 128)
white = (255, 255, 255)

BACKGROUND_COLOR = black
GAME_AREA_COLOR = white

red = (255, 0, 0)
green = (0, 255, 0)
blue = (0, 0, 255)

block_colors = (red, green, blue)

def random_color():
    return block_colors[random.randint(0, len(block_colors) - 1)]
