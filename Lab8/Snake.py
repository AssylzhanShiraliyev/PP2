import pygame
import sys
import random

pygame.init()

# Screen dimensions and cell size
width, height = 500, 500
cell_size = 10

# Set up the screen
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption('Simple Snake')

# Colors
black = (0, 0 , 0)
green = (0, 255, 0)
red = (255, 0, 0)

# Snake starting position and body
snake_pos = [100, 100]
snake_body = [[100, 100], [80, 100], [60, 100]]
direction = 'RIGHT'
change_to = direction

# Food position
food_pos = [random.randrange(1, (width//cell_size)) * cell_size, random.randrange(1, (height//cell_size)) * cell_size]
food_spawn = True

# Score and level
score = 0
level = 1
snake_speed = 15

# Clock to control the speed of the snake
clock = pygame.time.Clock()

# Function to display the score and level
def show_score(score, level):
    font = pygame.font.SysFont("arial", 25)
    score_text = font.render(f"Score: {score}  Level: {level}", True, green)
    screen.blit(score_text, [10, 10])

# Main game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP and direction != 'DOWN':
                change_to = 'UP'
            elif event.key == pygame.K_DOWN and direction != 'UP':
                change_to = 'DOWN'
            elif event.key == pygame.K_RIGHT and direction != 'LEFT':
                change_to = 'RIGHT'
            elif event.key == pygame.K_LEFT and direction != 'RIGHT':
                change_to = 'LEFT'

    # Change the direction
    direction = change_to

    # Move the snake
    if direction == 'UP':
        snake_pos[1] -= cell_size
    elif direction == 'DOWN':
        snake_pos[1] += cell_size
    elif direction == 'LEFT':
        snake_pos[0] -= cell_size
    elif direction == 'RIGHT':
        snake_pos[0] += cell_size

    # Snake body movement (adding the new head and removing the tail)
    snake_body.insert(0, list(snake_pos))
    if snake_pos == food_pos:
        food_spawn = False
        score += 10  # Increase score when food is eaten
        if score % 50 == 0:  # Increase level every 50 points
            level += 1
            snake_speed += 5  # Increase speed when level up
    else:
        snake_body.pop()

    # Check if the snake hits the boundaries
    if snake_pos[0] < 0 or snake_pos[0] >= width or snake_pos[1] < 0 or snake_pos[1] >= height:
        running = False  # End the game if the snake hits the boundary

    # Check if the snake collides with itself
    for block in snake_body[1:]:
        if block == snake_pos:
            running = False  # End the game if the snake collides with itsel

    # Spawn food randomly
    if not food_spawn:
        food_pos = [random.randrange(1, (width//cell_size)) * cell_size, random.randrange(1, (height//cell_size)) * cell_size]
    food_spawn = True

    # Update the screen
    screen.fill(black)

    # Draw the snake
    for block in snake_body:
        pygame.draw.rect(screen, green, pygame.Rect(block[0], block[1], cell_size, cell_size))

    # Draw the food
    pygame.draw.rect(screen, red, pygame.Rect(food_pos[0], food_pos[1], cell_size, cell_size))

    # Display the score and level
    show_score(score, level)

    # Update the display
    pygame.display.flip()

    # Control the snake speed
    clock.tick(snake_speed)

# Quit the game
pygame.quit()
sys.exit()

