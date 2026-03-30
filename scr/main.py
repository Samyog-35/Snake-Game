import pygame
import sys
import random
from sprites import Snake, Food, Apple, Berry, Peach, Grape, Obstacle
from utility import get_asset_path

pygame.init()

CELL     = 20
COLS     = 30
ROWS     = 25
SCREEN_W = CELL * COLS
SCREEN_H = CELL * ROWS

screen = pygame.display.set_mode((SCREEN_W, SCREEN_H))
pygame.display.set_caption("Snake Game")
clock  = pygame.time.Clock()
font   = pygame.font.SysFont("arial", 22, bold=True)
FPS    = 60

# create snake in the middle
snake = Snake(COLS // 2, ROWS // 2)
score = 0

# spawn random food
def spawn_food():
    """Spawns random food at a random spot."""
    x = random.randint(0, COLS - 1)
    y = random.randint(0, ROWS - 1)
    return random.choice([Apple, Berry, Peach, Grape])(x, y)

food = spawn_food()

# move timer
move_delay = 0.15
move_timer = 0.0

while True:
    dt = clock.tick(FPS) / 1000.0

    # input
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                snake.direction = (0, -1)
            elif event.key == pygame.K_DOWN:
                snake.direction = (0, 1)
            elif event.key == pygame.K_LEFT:
                snake.direction = (-1, 0)
            elif event.key == pygame.K_RIGHT:
                snake.direction = (1, 0)

    # move snake on timer
    move_timer += dt
    if move_timer >= move_delay:
        move_timer = 0.0
        snake.move()

        # wall collision
        hx, hy = snake.segments[0]
        if hx < 0 or hy < 0 or hx >= COLS or hy >= ROWS:
            print(f"Game Over! Score: {score}")
            pygame.quit()
            sys.exit()

        # ate food
        if snake.segments[0] == food.get_pos():
            score += food.get_points()
            snake.segments.append(snake.segments[-1])
            food = spawn_food()

    # draw
    screen.fill((18, 20, 28))

    food.draw(screen)

    for i, (gx, gy) in enumerate(snake.segments):
        color = (50, 200, 80) if i == 0 else (30, 160, 60)
        pygame.draw.rect(screen, color,
                        (gx * CELL + 2, gy * CELL + 2, CELL - 4, CELL - 4))

    score_text = font.render(f"Score: {score}", True, (255, 255, 255))
    screen.blit(score_text, (10, 10))

    pygame.display.flip()