from mazewalker.maze import Cell, EXIT
import random

def _find_unvisited_neighbours(maze, position, visited_cells):
    unvisited_neighbours = []
    if position[0] > 0 and (position[0] - 1, position[1]) not in visited_cells:
        unvisited_neighbours.append((position[0] - 1, position[1]))
    if position[0] < len(maze[0]) - 1 and (position[0] + 1, position[1]) not in visited_cells:
        unvisited_neighbours.append((position[0] + 1, position[1]))
    if position[1] > 0 and (position[0], position[1] - 1) not in visited_cells:
        unvisited_neighbours.append((position[0], position[1] - 1))
    if position[1] < len(maze) - 1 and (position[0], position[1] + 1) not in visited_cells:
        unvisited_neighbours.append((position[0], position[1] + 1))
    return unvisited_neighbours

def _remove_walls(maze, position1, position2):
    if position1[0] == position2[0]:
        if position1[1] > position2[1]:
            position1, position2 = position2, position1
        maze[position1[1]][position1[0]].bottom_wall = False
        maze[position2[1]][position2[0]].top_wall = False
    else:
        if position1[0] > position2[0]:
            position1, position2 = position2, position1
        maze[position1[1]][position1[0]].right_wall = False
        maze[position2[1]][position2[0]].left_wall = False

def gen_random_maze(width, height):
    """
    Moves the player to the right cell when there is no wall on the right of the current cell. 

    Parameters: 
        width (int): number of columns (> 0)
        height (int): number of rows (> 0)

    Returns: 
        list[list[Cell]]: Perfect maze generated with width rows and height columns.
    """
    random.seed()
    maze = [[Cell() for j in range(width)] for i in range(height)]
    visited_cells = set()
    cell_stack = []
    current_cell = (0, 0)
    visited_cells.add(current_cell)
    while len(visited_cells) < width * height:
        unvisited_neighbours = _find_unvisited_neighbours(maze, current_cell, visited_cells)
        if unvisited_neighbours:
            next_cell = random.choice(unvisited_neighbours)
            cell_stack.append(current_cell)
            _remove_walls(maze, current_cell, next_cell)
            current_cell = next_cell
            visited_cells.add(current_cell)
        elif cell_stack:
            current_cell = cell_stack.pop()
    maze[random.randrange(0, height)][random.randrange(0, width)].content = EXIT
    return maze
