import sys
import pygame
from block import *

def make_game_area(screen):
    game_area = Stationary_Block(GAME_AREA_POS, GAME_AREA_SIZE, grey, white)
    return game_area

def move_down_auto(block):
    global last_decrease_timepoint

    # move if 1 second has passed since last decrease
    if (pygame.time.get_ticks() - last_decrease_timepoint >= 1000):
        block = block.move((0, MOVE_OFFSET))
        last_decrease_timepoint = pygame.time.get_ticks()

    return block

def pos_within_rect(rect, pos):
    return ((rect.topleft[0] <= pos[0] and pos[0] <= rect.topright[0]) and 
            (rect.topleft[1] <= pos[1] and pos[1] <= rect.bottomright[1]))

pygame.init()
screen = pygame.display.set_mode(SCREEN_SIZE)
pygame.display.set_caption("Tetris Game - aburtasenkov")

last_decrease_timepoint = pygame.time.get_ticks()
current_block = Moving_Block(START_POS, BLOCK_SIZE)

if __name__ == "__main__":
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT: sys.exit()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    continue
                elif event.key == pygame.K_DOWN:
                    current_block = current_block.move((0, MOVE_OFFSET))
                elif event.key == pygame.K_LEFT:
                    current_block = current_block.move((-MOVE_OFFSET, 0))
                elif event.key == pygame.K_RIGHT:
                    current_block = current_block.move((MOVE_OFFSET, 0))
                
        screen.fill(black)

        game_area = make_game_area(screen)

        print(pos_within_rect(game_area.outline, current_block.outline.center))

        game_area.draw(screen)
        current_block.draw(screen)
            
        pygame.display.flip()







