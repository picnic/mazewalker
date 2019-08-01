import unittest
from mazewalker.generator import gen_random_maze
from mazewalker.maze import Cell, EXIT

class TestGenerator(unittest.TestCase):
    def test_gen_random_maze_11(self):
        maze = gen_random_maze(1, 1)
        self.assertTrue(maze[0][0].left_wall)
        self.assertTrue(maze[0][0].right_wall)
        self.assertTrue(maze[0][0].top_wall)
        self.assertTrue(maze[0][0].bottom_wall)
        self.assertEqual(maze[0][0].content, EXIT)

    def _find_cells_to_visit(self, maze, position):
        cells_to_visit = []
        if not maze[position[1]][position[0]].left_wall:
            cells_to_visit.append((position[0] - 1, position[1]))
        if not maze[position[1]][position[0]].right_wall:
            cells_to_visit.append((position[0] + 1, position[1]))
        if not maze[position[1]][position[0]].top_wall:
            cells_to_visit.append((position[0], position[1] - 1))
        if not maze[position[1]][position[0]].bottom_wall:
            cells_to_visit.append((position[0], position[1] + 1))
        return cells_to_visit

    def test_gen_random_maze(self):
        maze = gen_random_maze(10, 5)
        self.assertEqual(len(maze), 5)
        self.assertEqual(len(maze[0]), 10)

        # try to reach all the cells to verify that the maze is correctly generated
        exit_cells = set()
        visited_cells = set()
        cell_stack = [(0, 0)]
        while len(cell_stack):
            position = cell_stack.pop()
            if position not in visited_cells:
                visited_cells.add(position)
                if maze[position[1]][position[0]].content == EXIT:
                    exit_cells.add(position)
                cell_stack = cell_stack + self._find_cells_to_visit(maze, position)
        self.assertEqual(len(visited_cells), 10 * 5)
        self.assertEqual(len(exit_cells), 1)
