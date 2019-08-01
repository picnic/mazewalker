import unittest
from mazewalker.maze import *

class TestMaze(unittest.TestCase):

    def setUp(self):
        # Test maze (3x3):
        # +-----+
        # |   | |
        # +-+ + +
        # |  X  |
        # + +   +
        # | |   |
        # +-----+
        self.cells = [
            [Cell(True, False, True, True, EMPTY), Cell(False, True, True, False, EMPTY), Cell(True, True, True, False, EMPTY)],
            [Cell(True, False, True, False, EMPTY), Cell(False, False, False, False, EXIT), Cell(False, True, False, False, EMPTY)],
            [Cell(True, True, False, True, EMPTY), Cell(True, False, False, True, EMPTY), Cell(False, True, False, True, EMPTY)],
        ]
        self.maze = Maze(self.cells, (2, 1))
    
    def test_cell_init(self):
        cell = Cell()
        self.assertEqual(cell.left_wall, True)
        self.assertEqual(cell.right_wall, True)
        self.assertEqual(cell.top_wall, True)
        self.assertEqual(cell.bottom_wall, True)
        self.assertEqual(cell.content, EMPTY)
        cell = Cell(False, True, True, False, EXIT)
        self.assertEqual(cell.left_wall, False)
        self.assertEqual(cell.right_wall, True)
        self.assertEqual(cell.top_wall, True)
        self.assertEqual(cell.bottom_wall, False)
        self.assertEqual(cell.content, EXIT)
        cell = Cell(True, False, False, True, EMPTY)
        self.assertEqual(cell.left_wall, True)
        self.assertEqual(cell.right_wall, False)
        self.assertEqual(cell.top_wall, False)
        self.assertEqual(cell.bottom_wall, True)
        self.assertEqual(cell.content, EMPTY)

    def test_init(self):
        self.assertEqual(self.maze._cells, self.cells)
        self.assertEqual(self.maze._initial_position, (2, 1))
        self.assertEqual(self.maze._position, (2, 1))

    def test_init_position(self):
        self.maze.move_up()
        self.assertEqual(self.maze._position, (2, 0))
        self.maze.init_position()
        self.assertEqual(self.maze._position, (2, 1))

    def test_move_left_wall(self):
        self.maze._position = (2, 0)
        ret = self.maze.move_left()
        self.assertEqual(ret, WALL)
        self.assertEqual(self.maze._position, (2, 0))

    def test_move_left_empty(self):
        self.maze._position = (1, 0)
        ret = self.maze.move_left()
        self.assertEqual(ret, EMPTY)
        self.assertEqual(self.maze._position, (0, 0))

    def test_move_left_exit(self):
        self.maze._position = (2, 1)
        ret = self.maze.move_left()
        self.assertEqual(ret, EXIT)
        self.assertEqual(self.maze._position, (1, 1))

    def test_move_right_wall(self):
        self.maze._position = (1, 0)
        ret = self.maze.move_right()
        self.assertEqual(ret, WALL)
        self.assertEqual(self.maze._position, (1, 0))

    def test_move_right_empty(self):
        self.maze._position = (0, 0)
        ret = self.maze.move_right()
        self.assertEqual(ret, EMPTY)
        self.assertEqual(self.maze._position, (1, 0))

    def test_move_right_exit(self):
        self.maze._position = (0, 1)
        ret = self.maze.move_right()
        self.assertEqual(ret, EXIT)
        self.assertEqual(self.maze._position, (1, 1))

    def test_move_up_wall(self):
        self.maze._position = (0, 1)
        ret = self.maze.move_up()
        self.assertEqual(ret, WALL)
        self.assertEqual(self.maze._position, (0, 1))

    def test_move_up_empty(self):
        self.maze._position = (2, 1)
        ret = self.maze.move_up()
        self.assertEqual(ret, EMPTY)
        self.assertEqual(self.maze._position, (2, 0))

    def test_move_up_exit(self):
        self.maze._position = (1, 2)
        ret = self.maze.move_up()
        self.assertEqual(ret, EXIT)
        self.assertEqual(self.maze._position, (1, 1))

    def test_move_down_wall(self):
        self.maze._position = (0, 0)
        ret = self.maze.move_down()
        self.assertEqual(ret, WALL)
        self.assertEqual(self.maze._position, (0, 0))

    def test_move_down_empty(self):
        self.maze._position = (0, 1)
        ret = self.maze.move_down()
        self.assertEqual(ret, EMPTY)
        self.assertEqual(self.maze._position, (0, 2))

    def test_move_down_exit(self):
        self.maze._position = (1, 0)
        ret = self.maze.move_down()
        self.assertEqual(ret, EXIT)
        self.assertEqual(self.maze._position, (1, 1))
