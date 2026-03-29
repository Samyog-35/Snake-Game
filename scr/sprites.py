class Snake:
    """This class creates and controls the snake."""

    def __init__(self, x, y):
        """
        Starts the snake at a given position.

        x, y: starting position of the snake
        """
        self.segments = [(x, y)]  # snake body (head is first)
        self.direction = (1, 0)   # moving right

    def move(self):
        """
        Moves the snake forward.

        It adds a new head in the direction it's moving
        and removes the last part (tail).
        """
        head_x, head_y = self.segments[0]
        dx, dy = self.direction
        new_head = (head_x + dx, head_y + dy)
        self.segments.insert(0, new_head)
        self.segments.pop()