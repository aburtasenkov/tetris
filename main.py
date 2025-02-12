import sys
import pygame
import typing
import copy
from block import *

def get_fps(clock: pygame.time.Clock) -> int:
    clock.tick()
    return int(clock.get_fps())

def make_game_area(screen: pygame.Surface) -> Stationary_Block:
    game_area = Stationary_Block(GAME_AREA_POS, GAME_AREA_SIZE, grey, white)
    return game_area

def pos_within_rect(rect: pygame.Rect, pos: tuple[int, int]) -> bool:
    """return true coordinate pos is within rect's edges"""
    return ((rect.topleft[0] <= pos[0] and pos[0] <= rect.topright[0]) and 
            (rect.topleft[1] <= pos[1] and pos[1] <= rect.bottomright[1]))

def check_collisions(game_area: pygame.Rect, stationary_blocks: typing.Iterable[list["Stationary_Block"]], pos: tuple[int,int]) -> bool:
    """
    check for collisions with game_area and all stationary blocks from block_list

    requirements:   
    1. collision with game_area must be true -> within game_area
    2. all collisions with block_list objects must be false -> center position is not within any existing blocks

    return value:
        true if both requirements are true
        false if at least one of requirements is not met
    """

    if (not pos_within_rect(game_area, pos)):
        return False
    
    for row in stationary_blocks:
        for block in row:
            if block:
                if (pos_within_rect(block.outline, pos)):
                    return False
    return True

def move_block(game_area: pygame.Rect, stationary_blocks: typing.Iterable[list["Stationary_Block"]], block: "Moving_Block", offset: tuple[int, int]) -> "Moving_Block":
    """
    move block if check_collisions is valid

    do it by pre-moving and checking if block.outline.center coordinate is within game_area and outside of blocks in stationary_blocks 
        if True - return block
        else move block back
    """

    block = block.move(offset)

    if not check_collisions(game_area, stationary_blocks, block.outline.center):
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

screen: pygame.Surface = pygame.display.set_mode(SCREEN_SIZE)
game_area = make_game_area(screen)
stationary_blocks: list[list[Stationary_Block]] = [[None for _ in range(10)] for _ in range(20)] 

def main():
    pygame.init()
    pygame.display.set_caption(GAME_TITLE)
    clock = pygame.time.Clock()

    time_passed = make_moving_timer()

    current_block = Moving_Block(START_POS, BLOCK_SIZE)

    test = Shape(START_POS, BLOCK_SIZE)

    while True:

        # move logic
        for event in pygame.event.get():
            
            if event.type == pygame.QUIT: sys.exit()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    continue
                elif event.key == pygame.K_DOWN:
                    current_block = move_block(game_area.outline, stationary_blocks, current_block, (0, MOVE_OFFSET))
                elif event.key == pygame.K_LEFT:
                    current_block = move_block(game_area.outline, stationary_blocks, current_block, (-MOVE_OFFSET, 0))
                elif event.key == pygame.K_RIGHT:
                    current_block = move_block(game_area.outline, stationary_blocks, current_block, (MOVE_OFFSET, 0))
                
        # auto move down
        if (time_passed(TIME_UNTIL_DECREASE)):

            test.move((0, MOVE_OFFSET))

            last_pos = current_block.outline.topleft

            current_block = move_block(game_area.outline, stationary_blocks, current_block, (0, MOVE_OFFSET))

            # Block has not moved -> make it stationary (base class)
            if (current_block.outline.topleft == last_pos):
                row_index = int((last_pos[1] - GAME_AREA_POS[1]) / MOVE_OFFSET)
                obj_index = int((last_pos[0] - GAME_AREA_POS[0]) / MOVE_OFFSET)

                current_block.__class__ = current_block.__class__.__base__
                stationary_blocks[row_index][obj_index] = copy.deepcopy(current_block)

        # create new block for moving if it is stationary
        if (type(current_block) == Stationary_Block):
            current_block = Moving_Block(START_POS, BLOCK_SIZE)

        # draw logic
        game_area.draw(screen)
        current_block.draw(screen)
        test.draw(screen)
        
        for row in stationary_blocks:
            for block in row:
                if block != None:
                    block.draw(screen)

        pygame.display.flip()

        screen.fill(black)


if __name__ == "__main__":
    main()
