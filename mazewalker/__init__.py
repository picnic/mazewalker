import sys
from mazewalker.maze import Maze
from mazewalker.generator import gen_random_maze


__maze = Maze(gen_random_maze(10, 5), (0, 0))


def init_position():
    """Resets position to the initial position in the maze."""
    __maze.init_position()


def move_left():
    """ 
    Moves to the left cell when there is no wall on the left of the current cell. 

    Returns: 
        int: WALL if there is a wall on the left, else the content of the new cell (EMPTY or EXIT).
    """
    return __maze.move_left()


def move_right():
    """ 
    Moves to the right cell when there is no wall on the right of the current cell. 

    Returns: 
        int: WALL if there is a wall on the right, else the content of the new cell (EMPTY or EXIT).
    """
    return __maze.move_right()


def move_up():
    """ 
    Moves to the top cell when there is no wall on the top of the current cell. 

    Returns: 
        int: WALL if there is a wall on the top, else the content of the new cell (EMPTY or EXIT).
    """
    return __maze.move_up()


def move_down():
    """ 
    Moves to the bottom cell when there is no wall on the bottom of the current cell. 

    Returns: 
        int: WALL if there is a wall on the bottom, else the content of the new cell (EMPTY or EXIT).
    """
    return __maze.move_down()
