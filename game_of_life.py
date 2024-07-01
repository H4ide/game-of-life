import pygame

DELAY_MS = 250 # grid update frequency (int>0)
# grid and screen setup
# left to right, up to down. Could be more, but I think this is one of the optimal sizes 
WIDTH, HEIGHT = 80, 80
COLOR_ALIVE_NOT_STATIC = (255,255,255)
COLOR_DEAD_NOT_STATIC = (0,0,0)
COLOR_ALIVE_STATIC = (0,255,0)
COLOR_DEAD_STATIC = (255,0,0)

MIN_NEIGHBOURS_FOR_ALIVE = 2
MAX_NEIGHBOURS_FOR_ALIVE = 3
MIN_NEIGHBOURS_FOR_DEAD = 3
MAX_NEIGHBOURS_FOR_DEAD = 3


# this is background color, but dead and alive cells 1 layer higer 
COLOR_GRID = (40, 90, 0) 

CELL_SIZE = 10 # int >0

class Cell:
    def __init__(self, id_height:int, id_width:int, state:bool = False, static:bool = False) -> None:
        self.id_height = id_height
        self.id_width = id_width
        self.state = state
        self.static = static
    def changeState(self) -> None:
        self.state = not self.state
    def changeStatic(self) -> None:
        self.static = not self.static
    def setState(self, flag) -> None:
        self.state = flag
    
    def getState(self) -> bool:
        return self.state
    def getStatic(self) -> bool:
        return self.static
    def get_color(self):
        if not self.state and not self.static:
            color = COLOR_DEAD_NOT_STATIC
        elif not self.state and  self.static:
            color = COLOR_DEAD_STATIC
        elif self.state and  not self.static:
            color = COLOR_ALIVE_NOT_STATIC
        else: # state and static
            color = COLOR_ALIVE_STATIC
        return color
    
def update(screen, grid, cell_size=CELL_SIZE):
    #iterate every cell
    for  col in range(HEIGHT):
        for row in range(WIDTH):
            cell = grid[col][row]
            color = cell.get_color()
            #cell_size-1, to see the grid (background)
            pygame.draw.rect(screen, color, (row*cell_size, col*cell_size, cell_size-1, cell_size-1))


def live_or_die(is_alive:bool, alive_neighbours:int)->bool:
        if is_alive  and alive_neighbours >= MIN_NEIGHBOURS_FOR_ALIVE and alive_neighbours <= MAX_NEIGHBOURS_FOR_ALIVE:
            return True
        if not is_alive and alive_neighbours >= MIN_NEIGHBOURS_FOR_DEAD and alive_neighbours <= MAX_NEIGHBOURS_FOR_DEAD:
            return True
        return False    

def game_of_life(grid) -> list(list()):

    HEIGHT= len(grid)
    WIDTH = len(grid[0])
    new_grid = [[None] * WIDTH  for _ in range(HEIGHT)] # 1 on [row][col] if we change state of the cell
    for row in range(HEIGHT):
        for col in range(WIDTH):
            if not grid[row][col].getStatic():
                count_alive = 0
                for move_x in range(-1, 2): 
                    for move_y in range(-1, 2): 
                        #do not count the state of the cell itself
                        if move_x == 0 and move_y == 0: 
                            continue
                        #we divide by HEIGTH or WIDTH because the game is on a torus
                        count_alive += grid[(row-move_x) % HEIGHT][(col-move_y) % WIDTH].getState()

                alive = live_or_die(grid[row][col].getState() ,count_alive)
                new_grid[row][col] = alive
    return new_grid


def main():
    print("""   This is a "Game of life by John Conway" 

LMB (hold or press)  - change the state of the cell
RMB (hold or press)  - make cell static (unstatic), 
    so it doesn't change over time

Space  - to pause/UNpause the game
To quit - press close button on the window

    The grid of the game is on a torus (like a snake game on nokia 3310)
that is, the cells at the very top "see" the cells at the bottom, 
the cells on the left see the cells on the right, 
and all the corners see each other.
    There is no goal in the game, the game plays itself, 
you only determine the status of the cell. 
Is the cell alive or dead 
By pressing or holding the LMB over the cell, 
you either kill it or revive it.


    Rules of cell life:
1. Any live cell with two or three live neighbours survives.
2. Any dead cell with three live neighbours becomes a live cell.
3. All other live cells die in the next generation. 
Similarly, all other dead cells stay dead.

PRESS ENTER TO START THE GAME""")
    input()
    
    # Initialize pygame
    pygame.init()
    
    #setting screen
    screen = pygame.display.set_mode(size=(WIDTH * CELL_SIZE, HEIGHT * CELL_SIZE))
    pygame.display.set_caption("Game of Life   (paused)")

    grid = list()
    for i in range(HEIGHT):
        rows = list()
        for j in range(WIDTH):
            rows.append(Cell(i,j))
        grid.append(rows)

    #grid color
    screen.fill(COLOR_GRID)
    
    #set empty cells over the background
    update(screen, grid, CELL_SIZE)

    
    last_col_lmb = last_row_lmb  = -1
    last_col_rmb = last_row_rmb = -1
    
    # game is paused in default
    pause = True
    while True:
        for event in pygame.event.get():
            #Close the app if "X" on the window is pressed
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    pause = not pause
                    if pause:
                        pygame.display.set_caption("Game of Life   (paused)")
                    else: 
                        timer = pygame.time.get_ticks()
                        pygame.display.set_caption("Game of Life")
            #"forget" last cell changed after unpressing the button
            if event.type == pygame.MOUSEBUTTONUP and event.button == 1: # LEFT MB
                last_col_lmb = -1
                last_row_lmb = -1
            if event.type == pygame.MOUSEBUTTONUP and event.button == 3: # RIGHT MB
                last_col_rmb = -1
                last_row_rmb = -1


            col, row = pygame.mouse.get_pos()[0]//CELL_SIZE, \
                pygame.mouse.get_pos()[1]//CELL_SIZE
            if pygame.mouse.get_pressed()[0] == 1: #LEFT MB
                if col != last_col_lmb or row != last_row_lmb:
                    grid[row][col].changeState()
                    last_col_lmb, last_row_lmb = col, row

            if pygame.mouse.get_pressed()[2] == 1: #RIGHT MB
                if col != last_col_rmb or row != last_row_rmb:
                        grid[row][col].changeStatic()
                        last_col_rmb, last_row_rmb = col, row

            update(screen, grid, CELL_SIZE)
            pygame.display.update()
            
        if pause == False and pygame.time.get_ticks() - timer >= DELAY_MS:
            pygame.display.set_caption("Game of Life") # so user can see if game is paused or not
            new_grid = game_of_life(grid)
            for col in range(HEIGHT):
                for row in range(WIDTH):
                    if new_grid[col][row] is not None:
                        grid[col][row].setState(new_grid[col][row])
            update(screen, grid, CELL_SIZE)
            pygame.display.update()
            # next iteration time
            timer = pygame.time.get_ticks()

if __name__ == "__main__":
    main()
