
GAME_TITLE = "Tetris Game - aburtasenkov"

SCREEN_SIZE = WIDTH, HEIGHT = 480, 800

# Blocks cosmetics
OUTLINE_SIZE = 2
OUTLINE_BORDER_RADIUS = 5
INNER_BORDER_RADIUS = 2

# number of blocks on horizontal and vertical axis
GAME_AREA_BLOCKS_HORIZONTAL = 10
GAME_AREA_BLOCKS_VERTICAL = 20

# size of block and game area
BLOCK_SIZE = BLOCK_WIDTH, BLOCK_HEIGHT = 35, 35
GAME_AREA_SIZE = (GAME_AREA_BLOCKS_HORIZONTAL * BLOCK_WIDTH, 
                   GAME_AREA_BLOCKS_VERTICAL * BLOCK_HEIGHT)
MOVE_OFFSET = BLOCK_SIZE[0]

# top left corners of game area and starting position for each block
GAME_AREA_POS = (50, 50)
START_POS = (GAME_AREA_POS[0] + (GAME_AREA_BLOCKS_HORIZONTAL / 2 * BLOCK_WIDTH), GAME_AREA_POS[1] + BLOCK_SIZE[1])  # middle of game_area and top coordinate

# time in ms that it takes a block to move 1 square down
TIME_UNTIL_DECREASE = 1000