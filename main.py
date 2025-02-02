import sys
import pygame
from block import *

def make_game_area(screen: pygame.Surface) -> Stationary_Block:
    game_area = Stationary_Block(GAME_AREA_POS, GAME_AREA_SIZE, grey, white)
    return game_area

last_decrease_timepoint: pygame.time = pygame.time.get_ticks()

def move_down_auto(block: Moving_Block) -> Moving_Block:
    global last_decrease_timepoint

    # move if 1 second has passed since last decrease
    if (pygame.time.get_ticks() - last_decrease_timepoint >= 1000):
        block = block.move((0, MOVE_OFFSET))
        last_decrease_timepoint = pygame.time.get_ticks()

    return block

def is_pos_within_rect(rect: pygame.Rect, pos: tuple[int, int]) -> bool:
    return ((rect.topleft[0] <= pos[0] and pos[0] <= rect.topright[0]) and 
            (rect.topleft[1] <= pos[1] and pos[1] <= rect.bottomright[1]))

def get_fps(clock: pygame.time.Clock) -> int:
    clock.tick()
    return int(clock.get_fps())

if __name__ == "__main__":

    pygame.init()
    screen: pygame.Surface = pygame.display.set_mode(SCREEN_SIZE)
    pygame.display.set_caption("Tetris Game - aburtasenkov")

    clock = pygame.time.Clock()

    current_block: Moving_Block = Moving_Block(START_POS, BLOCK_SIZE)

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

        print("Block within game area -", is_pos_within_rect(game_area.outline, current_block.outline.center))

        game_area.draw(screen)
        current_block.draw(screen)
            
        pygame.display.flip()







