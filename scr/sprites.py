import pygame
speed_boost_timer = [0.0]
time_bonus = [0.0]

class Snake:
    """This class creates and controls the snake."""

    def __init__(self, x, y):
        """Starts the snake at a given position."""
        self.segments = [(x, y)]
        self.direction = (1, 0)

    def move(self):
        """Moves the snake forward one step."""
        head_x, head_y = self.segments[0]
        dx, dy = self.direction
        new_head = (head_x + dx, head_y + dy)
        self.segments.insert(0, new_head)
        self.segments.pop()

    def __str__(self):
        return f"Snake at {self.segments[0]}"

    def __repr__(self):
        return f"Snake(length={len(self.segments)})"


class Food:
    """This class creates food that the snake can eat."""

    def __init__(self, x, y):
        """Creates food at a given position."""
        self._x = x
        self._y = y
        self._points = 10

    def get_pos(self):
        """Returns the position of the food."""
        return (self._x, self._y)

    def get_points(self):
        """Returns how many points this food gives."""
        return self._points

    def draw(self, screen):
        """Draws the food as a red square."""
        x = self._x * 20
        y = self._y * 20
        pygame.draw.rect(screen, (220, 40, 40), (x, y, 18, 18))

    def __str__(self):
        return f"Food at ({self._x}, {self._y}) worth {self._points} pts"

    def __repr__(self):
        return f"Food(x={self._x}, y={self._y})"


class Apple(Food):
    """Apple — red, 10 points."""

    def __init__(self, x, y):
        """Creates an Apple."""
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
        """Creates a Berry."""
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


class Peach(Food):
    """Peach — orange, 30 points."""

    def __init__(self, x, y):
        """Creates a Peach."""
        super().__init__(x, y)
        self._points = 30

    def draw(self, screen):
        """Draws an orange peach."""
        x = self._x * 20
        y = self._y * 20
        pygame.draw.rect(screen, (255, 160, 80), (x, y, 18, 18))

    def __str__(self):
        return f"Peach at ({self._x}, {self._y})"

    def __repr__(self):
        return f"Peach(x={self._x}, y={self._y})"


class Grape(Food):
    """Grape — dark purple, 50 points."""

    def __init__(self, x, y):
        """Creates a Grape."""
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


class Obstacle:
    """A wall the snake must avoid."""

    def __init__(self, x, y, w, h):
        """Creates an obstacle block."""
        self._x = x
        self._y = y
        self._w = w
        self._h = h

        try:
            self._image = pygame.image.load("assets/brick.png").convert_alpha()
            self._image = pygame.transform.scale(self._image, (20, 20))
        except:
            self._image = None

    def get_cells(self):
        """Returns all grid cells this obstacle covers."""
        cells = []
        for dx in range(self._w):
            for dy in range(self._h):
                cells.append((self._x + dx, self._y + dy))
        return cells

    def draw(self, screen):
        """Draws the obstacle as a dark brown rectangle."""
        for dx in range(self._w):
            for dy in range(self._h):
                x = (self._x + dx) * 20
                y = (self._y + dy) * 20
                if self._image:
                    screen.blit(self._image, (x, y))
                else:
                    pygame.draw.rect(screen, (60, 40, 20), (x, y, 20, 20))

    def __str__(self):
        return f"Obstacle at ({self._x}, {self._y})"

    def __repr__(self):
        return f"Obstacle(x={self._x}, y={self._y})"