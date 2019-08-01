import unittest
from unittest.mock import patch, Mock
from importlib import reload
import mazewalker

class TestMazewalker(unittest.TestCase):
    @patch('mazewalker.generator.gen_random_maze')
    @patch('mazewalker.maze.Maze')
    def test_mazewalker(self, MazeMock, gen_random_maze_mock):
        gen_random_maze_mock.return_value = 'gen_random_maze_return_value'
        maze_mock = Mock()
        MazeMock.return_value = maze_mock
        reload(mazewalker)
        gen_random_maze_mock.assert_called_once_with(10, 5)
        MazeMock.assert_called_once_with('gen_random_maze_return_value', (0, 0))
        maze_mock.move_left.return_value = 'left'
        self.assertEqual(mazewalker.move_left(), 'left')
        maze_mock.move_left.assert_called_once_with()
        maze_mock.move_right.return_value = 'right'
        self.assertEqual(mazewalker.move_right(), 'right')
        maze_mock.move_right.assert_called_once_with()
        maze_mock.move_up.return_value = 'up'
        self.assertEqual(mazewalker.move_up(), 'up')
        maze_mock.move_up.assert_called_once_with()
        maze_mock.move_down.return_value = 'down'
        self.assertEqual(mazewalker.move_down(), 'down')
        maze_mock.move_down.assert_called_once_with()
        mazewalker.init_position()
        maze_mock.init_position.assert_called_once_with()


