import pygame
import sys
import random
from sprites import Snake, Food , Apple, Berry, Peach, Grape, Obstacle
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
game_over = False
death_cause = ""

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
            elif event.key == pygame.K_r and game_over:
               #reset everything
               snake = Snake(COLS//2,ROWS//2)
               score = 0
               game_over = False
               death_cause = ""
               food = spawn_food()

        # move snake on timer
    if not game_over:
            move_timer += dt
            if move_timer >= move_delay:
             move_timer = 0.0
            snake.move()
                # wall collision
            hx, hy = snake.segments[0]
            if hx < 0 or hy < 0 or hx >= COLS or hy >= ROWS: 
                game_over = True
                death_cause = "You hit The wall!!!" 

                #self collision 
            if snake.segments[0]in snake.segments[1:]:
                game_over = True
                death_cause = "you bit yourself"


                # ate food
            if snake.segments[0] == food.get_pos():
                score += food.get_points()
                snake.segments.append(snake.segments[-1])
                food = spawn_food()

    # draw
    screen.fill((18, 20, 28))

    food.draw(screen)
#avariable for 
    for i, (gx, gy) in enumerate(snake.segments):
        color = (50, 200, 80) if i == 0 else (30, 160, 60)
        pygame.draw.rect(screen, color,
                        (gx * CELL + 2, gy * CELL + 2, CELL - 4, CELL - 4))

    score_text = font.render(f"Score: {score}", True, (255, 255, 255))
    screen.blit(score_text, (10, 10))





    #message for game over or any (screen,(28,32,46),(100,150,400,200))(game .rec(ren))
    
    
    
    
    if game_over:
        pygame.draw.rect(screen,(28,32,46),(100,150,400,200))


         #game over text
        over_text = font.render("GAME OVER", True,(230,80,60))
        screen.blit(over_text,(220,170))


        #death cause
        cause_text = font.render(death_cause, True,(255,255,255))
        screen.blit(cause_text,(150,220))


        #final score
        score_text2 = font.render(f"Final Score: {score}",True,(80,225,120))
        screen.blit(score_text2,(190,260))


        #restart hint
        hint_text = font.render("Press R to restart",True,(255,255,255))
        screen.blit( hint_text,(180,300))
    pygame.display.flip()