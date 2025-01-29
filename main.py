import sys
import pygame
pygame.init()

BLOCK_LIST = []

from block import *

BLOCK_LIST.append(Block(START_POS, BLOCK_SIZE))

screen = pygame.display.set_mode(SCREEN_SIZE)

def draw_game(screen):
    game_area = Block((GAME_AREA_OFFSET, GAME_AREA_OFFSET), (380, 520), grey, white)
    game_area.draw(screen)
    return

if __name__ == "__main__":
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT: sys.exit()

        # update screen by filling it with color nad
        screen.fill(black)

        draw_game(screen)

        for block in BLOCK_LIST:
            block.draw(screen)

            block = block.move(speed)


        pygame.display.flip()

        pygame.time.wait(1000)







