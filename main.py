import badger2040
import random
import time

WIDTH      = 45
HEIGHT     = 12
CELL       = '+'
EMPTY_CELL = ' '
DEBUG      = False

def initialize_grid():
    return [[random.choice([EMPTY_CELL, CELL]) for _ in range(WIDTH)] for _ in range(HEIGHT)]

def print_grid(grid):
    badger.set_pen(0)
    badger.clear()
    badger.set_pen(15)
    badger.set_font("bitmap8")
    badger.set_thickness(1)
    for k, row in enumerate(grid):
        badger.text(''.join(row), 0, k*10)
        
        if DEBUG:
            print(k, row)

    badger.update()
    

def count_neighbors(grid, x, y):
    neighbors = [
        (-1, -1), (-1, 0), (-1, 1),
        (0, -1),           (0, 1),
        (1, -1),   (1, 0), (1, 1)
    ]
    
    count = 0
    for dx, dy in neighbors:
        nx, ny = x + dx, y + dy
        if 0 <= nx < HEIGHT and 0 <= ny < WIDTH:
            if grid[nx][ny] == CELL:
                count += 1
    return count

def update_grid(grid):
    new_grid = [[EMPTY_CELL for _ in range(WIDTH)] for _ in range(HEIGHT)]
    
    for x in range(HEIGHT):
        for y in range(WIDTH):
            
            neighbors = count_neighbors(grid, x, y)
            
            if grid[x][y] == CELL:
                if neighbors in [2, 3]:
                    new_grid[x][y] = CELL
                else:
                    new_grid[x][y] = EMPTY_CELL
            else:
                if neighbors == 3:
                    new_grid[x][y] = CELL
    return new_grid
                        

# Execute
badger = badger2040.Badger2040()
badger.set_update_speed(2)
grid = initialize_grid()

while True:
    print_grid(grid)
    grid = update_grid(grid)
    time.sleep(0.5)
