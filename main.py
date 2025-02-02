import sys
import pygame
from block import *

def get_fps(clock: pygame.time.Clock) -> int:
    clock.tick()
    return int(clock.get_fps())

def make_game_area(screen: pygame.Surface) -> Stationary_Block:
    game_area = Stationary_Block(GAME_AREA_POS, GAME_AREA_SIZE, grey, white)
    return game_area

def pos_within_rect(rect: pygame.Rect, pos: tuple[int, int]) -> bool:
    """return true coordinate pos is within rects edges"""
    return ((rect.topleft[0] <= pos[0] and pos[0] <= rect.topright[0]) and 
            (rect.topleft[1] <= pos[1] and pos[1] <= rect.bottomright[1]))

def move_in_rect(rect: pygame.Rect, block: Moving_Block, offset: tuple[int, int]) -> Moving_Block:
    """
    move block if its center coordinate stays within rects edges

    do it by pre-moving and checking if block.rect.center coordinate is within rect
        if True - return block
        else move block back
    """

    block = block.move(offset)
    if not pos_within_rect(rect, block.outline.center):
        block = block.move((-offset[0], -offset[1]))

    return block

def make_moving_timer():
    """Make a function that returns in time has passed"""
    last_timepoint = pygame.time.get_ticks()

    def time_passed(time_in_ms: int) -> bool:
        nonlocal last_timepoint

        if pygame.time.get_ticks() - last_timepoint >= time_in_ms:
            last_timepoint = pygame.time.get_ticks()
            return True
        return False

    return time_passed

stationary_blocks = []

def main():
    pygame.init()
    screen: pygame.Surface = pygame.display.set_mode(SCREEN_SIZE)
    pygame.display.set_caption("Tetris Game - aburtasenkov")
    clock = pygame.time.Clock()

    time_passed = make_moving_timer()
    game_area = make_game_area(screen)

    current_block = Moving_Block(START_POS, BLOCK_SIZE)

    time_passed = make_moving_timer()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT: sys.exit()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    continue
                elif event.key == pygame.K_DOWN:
                    current_block = move_in_rect(game_area.outline, current_block, (0, MOVE_OFFSET))
                elif event.key == pygame.K_LEFT:
                    current_block = move_in_rect(game_area.outline, current_block, (-MOVE_OFFSET, 0))
                elif event.key == pygame.K_RIGHT:
                    current_block = move_in_rect(game_area.outline, current_block, (MOVE_OFFSET, 0))
                
        screen.fill(black)

        if (time_passed(TIME_UNTIL_DECREASE)):
            last_pos = current_block.outline.center
            block = move_in_rect(game_area.outline, current_block, (0, MOVE_OFFSET))
            # Block has not moved -> make it stationary (base class)
            if (current_block.outline.center == last_pos):
                print(current_block.outline.center, last_pos)

                block.__class__ = block.__class__.__base__
                stationary_blocks.append(stationary_blocks)

                current_block = Moving_Block(START_POS, BLOCK_SIZE)

        for block in stationary_blocks:
            print("Is within blocks from block_list", pos_within_rect(block.outline, current_block.outline.center))

        game_area.draw(screen)
        current_block.draw(screen)
        for block in stationary_blocks:
            block.draw(screen)
            
        pygame.display.flip()


if __name__ == "__main__":
    main()
