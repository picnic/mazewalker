WALL = 0
EMPTY = 1
EXIT = 2

class Cell:
    """ 
    This is a class for storing a cell content and its surrounding walls. 

    Attributes: 
        left_wall (bool): Is there a wall on the left of the cell. 
        right_wall (bool): Is there a wall on the right of the cell. 
        top_wall (bool): Is there a wall on the top of the cell. 
        bottom_wall (bool): Is there a wall on the bottom of the cell. 
    """

    def __init__(self, left=True, right=True, top=True, bottom=True, content=EMPTY):
        """ 
        Constructor for Cell.

        Parameters: 
            left (bool): True if there is a WALL on the left.
            right (bool): True if there is a WALL on the right.
            top (bool): True if there is a WALL on the top.
            bottom (bool): True if there is a WALL on the bottom.
            content (int): EMPTY or EXIT
        """
        self.left_wall = left
        self.right_wall = right
        self.top_wall = top
        self.bottom_wall = bottom
        self.content = content


class Maze:
    """ 
    This is a class for storing maze information and handling player movement. 
    """

    def __init__(self, cells, initial_position):
        """ 
        The constructor for Maze. 
  
        Parameters: 
            cells (list[list[Cell]]): rows of columns of cells
            initial_position ((int, int)): initial position of the player in the maze (column, row).    
        """
        self._initial_position = initial_position
        self._position = initial_position
        self._cells = cells

    def init_position(self):
        """ 
        Moves the player to the initial position defined in the constructor. 
        """
        self._position = self._initial_position

    def _get_current_cell(self):
        return self._cells[self._position[1]][self._position[0]]

    def move_left(self):
        """ 
        Moves the player to the left cell when there is no wall on the left of the current cell. 

        Returns: 
            int: WALL if there is a wall on the left, else the content of the new cell (EMPTY or EXIT).
        """
        if self._get_current_cell().left_wall:
            return WALL
        self._position = (self._position[0] - 1, self._position[1])
        return self._get_current_cell().content

    def move_right(self):
        """ 
        Moves the player to the right cell when there is no wall on the right of the current cell. 

        Returns: 
            int: WALL if there is a wall on the right, else the content of the new cell (EMPTY or EXIT).
        """
        if self._get_current_cell().right_wall:
            return WALL
        self._position = (self._position[0] + 1, self._position[1])
        return self._get_current_cell().content

    def move_up(self):
        """ 
        Moves the player to the top cell when there is no wall on the top of the current cell. 

        Returns: 
            int: WALL if there is a wall on the top, else the content of the new cell (EMPTY or EXIT).
        """
        if self._get_current_cell().top_wall:
            return WALL
        self._position = (self._position[0], self._position[1] - 1)
        return self._get_current_cell().content

    def move_down(self):
        """ 
        Moves the player to the bottom cell when there is no wall on the bottom of the current cell. 

        Returns: 
            int: WALL if there is a wall on the bottom, else the content of the new cell (EMPTY or EXIT).
        """
        if self._get_current_cell().bottom_wall:
            return WALL
        self._position = (self._position[0], self._position[1] + 1)
        return self._get_current_cell().content
