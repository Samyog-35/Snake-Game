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
class Food:
      """This class creates food that the snake can eat."""

def __init__(self, x, y):
        """
        Creates food at a given position.
        x, y: position of the food on the grid
        """
        # store the position
        self._x = x
        self._y = y

        # how many points this food gives
        self._points = 10

def get_pos(self):
        """Returns the position of the food as (x, y)."""
        return (self._x, self._y)

def get_points(self):
        """Returns how many points this food is worth."""
        return self._points

def draw(self, screen):
    """
     Draws the food on the screen as a red square.
    screen: the pygame window to draw on
    """
    # each cell is 20 pixels wide
    x = self._x * 20
    y = self._y * 20
    pygame.draw.rect(screen, (220, 40, 40), (x, y, 18, 18))

def __str__(self):
    """Shows food info when you print it."""
    return f"Food at ({self._x}, {self._y}) worth {self._points} pts"

def __repr__(self):
    """Shows food info in the debugger"""
    return f"Food(x={self._x}, y={self._y})"
class Apple(Food):
     """Apple — red, 10 points."""

def __init__(self, x, y):
    """Creates an Apple at position x, y."""
    super().__init__(x, y)
    self._points = 10

def draw(self, screen):
    """Draws a red apple."""
    x = self._x * 20
    y = self._y * 20
    pygame.draw.rect(screen, (220, 40, 40), (x, y, 18, 18))

def __str__(self):
    return f"Apple at ({self._x}, {self._y})"

def __repr__(self):
    return f"Apple(x={self._x}, y={self._y})"


class Berry(Food):
    """Berry — purple, 20 points."""

    def __init__(self, x, y):
        """Creates a Berry at position x, y."""
        super().__init__(x, y)
        self._points = 20

    def draw(self, screen):
        """Draws a purple berry."""
        x = self._x * 20
        y = self._y * 20
        pygame.draw.rect(screen, (130, 0, 180), (x, y, 18, 18))

    def __str__(self):
        return f"Berry at ({self._x}, {self._y})"

    def __repr__(self):
        return f"Berry(x={self._x}, y={self._y})"


class Grape(Food):
    """Grape — dark purple, 50 points."""

    def __init__(self, x, y):
        """Creates a Grape at position x, y."""
        super().__init__(x, y)
        self._points = 50

    def draw(self, screen):
        """Draws a dark purple grape."""
        x = self._x * 20
        y = self._y * 20
        pygame.draw.rect(screen, (90, 0, 140), (x, y, 18, 18))

    def __str__(self):
        return f"Grape at ({self._x}, {self._y})"

    def __repr__(self):
        return f"Grape(x={self._x}, y={self._y})"