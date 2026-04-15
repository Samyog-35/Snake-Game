import pygame
import sys
import random

from sprites import Snake, Apple, Berry, Peach, Grape, Obstacle
from utility import get_asset_path

# ---------------- INIT ----------------
pygame.init()

CELL = 20
COLS = 30
ROWS = 25

SCREEN_W = CELL * COLS
SCREEN_H = CELL * ROWS

screen = pygame.display.set_mode((SCREEN_W, SCREEN_H))
pygame.display.set_caption("Snake Game")

clock = pygame.time.Clock()
font = pygame.font.SysFont("arial", 22, bold=True)
FPS = 60

# ---------------- ASSETS ----------------
bg = pygame.image.load(get_asset_path("Background.png")).convert()
bg = pygame.transform.scale(bg, (SCREEN_W, SCREEN_H))

brick_img = pygame.image.load(get_asset_path("brick.png")).convert_alpha()
brick_img = pygame.transform.scale(brick_img, (CELL, CELL))

# ---------------- GAME STATE ----------------
snake = Snake(COLS // 2, ROWS // 2)
score = 0
game_over = False
death_cause = ""

starve_timer = 18.0
grape_timer = 0.0

speed_boost_timer = [0.0]
freeze_timer = 0.0

state = "start"

skins = {
    "Purple": (160, 70, 200),
    "Red": (220, 50, 50),
    "Blue": (50, 130, 220),
    "Gold": (220, 180, 30),
}

current_skin = ["Red"]

obstacles = []
food_list = []

# ---------------- SPAWN FUNCTIONS ----------------
def spawn_food():
    while True:
        x = random.randint(1, COLS - 2)
        y = random.randint(1, ROWS - 2)

        blocked = False
        for ob in obstacles:
            if (x, y) in ob.get_cells():
                blocked = True

        if not blocked:
            return random.choice([Apple, Berry, Peach, Grape])(x, y)


def spawn_obstacles(count=5):
    obs = []
    for _ in range(count):
        x = random.randint(1, COLS - 2)
        y = random.randint(1, ROWS - 2)
        obs.append(Obstacle(x, y, 1, 1))
    return obs


# initial spawn
food_list = [spawn_food(), spawn_food()]
obstacles = spawn_obstacles()

# ---------------- BORDER ----------------
def draw_border():
    for x in range(SCREEN_W // CELL):
        screen.blit(brick_img, (x * CELL, 0))
        screen.blit(brick_img, (x * CELL, SCREEN_H - CELL))

    for y in range(SCREEN_H // CELL):
        screen.blit(brick_img, (0, y * CELL))
        screen.blit(brick_img, (SCREEN_W - CELL, y * CELL))


# ---------------- START SCREEN ----------------
def draw_start_screen():
    screen.blit(bg, (0, 0))

    title = font.render("SNAKE GAME", True, (80, 200, 120))
    screen.blit(title, (220, 150))

    prompt = font.render("Press ENTER to Start", True, (255, 255, 100))
    screen.blit(prompt, (170, 220))

    controls = font.render("Arrow Keys to Move", True, (150, 150, 150))
    screen.blit(controls, (180, 270))

    hint = font.render("Eat food and survive", True, (150, 150, 150))
    screen.blit(hint, (190, 310))


# ---------------- MAIN LOOP ----------------
move_delay = 0.17
move_timer = 0.0

while True:
    dt = clock.tick(FPS) / 1000.0

    # -------- INPUT --------
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        if event.type == pygame.KEYDOWN:

            if state == "start" and event.key == pygame.K_RETURN:
                state = "game"

            if event.key == pygame.K_UP:
                snake.direction = (0, -1)
            elif event.key == pygame.K_DOWN:
                snake.direction = (0, 1)
            elif event.key == pygame.K_LEFT:
                snake.direction = (-1, 0)
            elif event.key == pygame.K_RIGHT:
                snake.direction = (1, 0)

            elif event.key == pygame.K_r and game_over:
                snake = Snake(COLS // 2, ROWS // 2)
                score = 0
                game_over = False
                death_cause = ""
                food_list = [spawn_food(), spawn_food()]
                obstacles = spawn_obstacles()
                state = "game"

            elif event.key == pygame.K_1:
                current_skin[0] = "Purple"
            elif event.key == pygame.K_2:
                current_skin[0] = "Red"
            elif event.key == pygame.K_3:
                current_skin[0] = "Blue"
            elif event.key == pygame.K_4:
                current_skin[0] = "Gold"

    # -------- GAME LOGIC --------
    if state == "game" and not game_over:

        move_timer += dt

        if move_timer >= move_delay:
            move_timer = 0
            snake.move()

            hx, hy = snake.segments[0]

            # wall collision
            if hx <= 0 or hx >= COLS - 1 or hy <= 0 or hy >= ROWS - 1:
                game_over = True
                death_cause = "You hit the wall!"

            # self collision
            if snake.segments[0] in snake.segments[1:]:
                game_over = True
                death_cause = "You bit yourself"

            # food collision
            for food in food_list[:]:
                if snake.segments[0] == food.get_pos():
                    score += food.get_points()

                    if isinstance(food, Apple):
                        starve_timer = min(starve_timer + 4.0, 18.0)
                    elif isinstance(food, Berry):
                        freeze_timer = 5.0
                    elif isinstance(food, Peach):
                        speed_boost_timer[0] = 5.0
                    elif isinstance(food, Grape):
                        if starve_timer < 12:
                            starve_timer += 8.0

                    snake.segments.append(snake.segments[-1])
                    food_list.remove(food)
                    food_list.append(spawn_food())

    # -------- DRAW --------
    if state == "start":
        draw_start_screen()

    elif state == "game":
        screen.blit(bg, (0, 0))
        draw_border()

        for food in food_list:
            food.draw(screen)

        for ob in obstacles:
            ob.draw(screen)

        for i, (x, y) in enumerate(snake.segments):
            if i == 0:
                color = skins[current_skin[0]]
            else:
                color = tuple(c // 2 for c in skins[current_skin[0]])

            pygame.draw.rect(
                screen,
                color,
                (x * CELL + 2, y * CELL + 2, CELL - 4, CELL - 4)
            )

        score_text = font.render(f"Score: {score}", True, (255, 255, 255))
        screen.blit(score_text, (10, 10))

    # -------- GAME OVER --------
    if game_over:
        pygame.draw.rect(screen, (30, 30, 40), (100, 150, 400, 200))

        over = font.render("GAME OVER", True, (230, 80, 60))
        screen.blit(over, (220, 170))

        cause = font.render(death_cause, True, (255, 255, 255))
        screen.blit(cause, (150, 220))

        final = font.render(f"Final Score: {score}", True, (80, 225, 120))
        screen.blit(final, (190, 260))

        hint = font.render("Press R to Restart", True, (255, 255, 255))
        screen.blit(hint, (180, 300))

    pygame.display.flip()