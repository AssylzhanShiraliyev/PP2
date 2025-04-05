import pygame
import sys
import random
import time

# Initialize Pygame
pygame.init()

# Screen dimensions and cell size
width, height = 500, 500
cell_size = 20

# Set up the screen
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption('Snake')

# Colors
black = (0, 0 , 0)
green = (0, 255, 0)


apple_img = pygame.image.load("apple.png")  
orange_img = pygame.image.load("orange.png")  


apple_img = pygame.transform.scale(apple_img, (30, 30))
orange_img = pygame.transform.scale(orange_img, (30, 30))

# Snake starting position and body
snake_pos = [100, 100]
snake_body = [[100, 100], [80, 100], [60, 100]]
direction = 'RIGHT'
change_to = direction

# Food class with random weight and spawn time
class Food:
    def __init__(self, x, y, weight, spawn_time, fruit_type):
        self.x = x
        self.y = y
        self.weight = weight
        self.spawn_time = spawn_time
        self.fruit_type = fruit_type  # Store fruit type (apple or orange)

# Initial food generation with random weight
food_list = []
for _ in range(3):  # Generate 3 pieces of food
    food_x = random.randrange(1, (width // cell_size)) * cell_size
    food_y = random.randrange(1, (height // cell_size)) * cell_size
    food_weight = random.randint(1, 5)  # Random weight for food
    spawn_time = time.time()
    fruit_type = random.choice(['apple', 'orange'])  # Randomly choose between apple and orange
    food_list.append(Food(food_x, food_y, food_weight, spawn_time, fruit_type))

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

# Function to generate new food
def generate_food():
    food_x = random.randrange(1, (width // cell_size)) * cell_size
    food_y = random.randrange(1, (height // cell_size)) * cell_size
    food_weight = random.randint(1, 5)  # Random weight for food
    spawn_time = time.time()
    fruit_type = random.choice(['apple', 'orange'])  # Randomly choose between apple and orange
    return Food(food_x, food_y, food_weight, spawn_time, fruit_type)

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
    food_to_remove = None
    for food_obj in food_list:
        if snake_pos == [food_obj.x, food_obj.y]:
            score += food_obj.weight * 10  # Increase score based on the food weight
            food_to_remove = food_obj
            break

    # Remove eaten food and spawn new food
    if food_to_remove:
        food_list.remove(food_to_remove)

    # Check if any food disappeared, and generate new food if needed
    for food_obj in food_list[:]:
        if time.time() - food_obj.spawn_time > 5:  # Food disappears after 5 seconds
            food_list.remove(food_obj)
    
    # Ensure there is always food on the screen
    if len(food_list) == 0:
        food_list.append(generate_food())

    # Check for collision with wall or self
    if snake_pos[0] < 0 or snake_pos[0] >= width or snake_pos[1] < 0 or snake_pos[1] >= height:
        running = False  # End the game if the snake hits the boundary

    # Check if the snake collides with itself
    for block in snake_body[1:]:
        if block == snake_pos:
            running = False  # End the game if the snake collides with itself

    # Remove the last part of the snake if no food was eaten
    if food_to_remove is None:
        snake_body.pop()

    # Update the screen
    screen.fill(black)

    # Draw the snake
    for block in snake_body:
        pygame.draw.rect(screen, green, pygame.Rect(block[0], block[1], cell_size, cell_size))

    # Draw food
    for food_obj in food_list:
        draw_x = food_obj.x - 5  
        draw_y = food_obj.y - 5 # Центрируем еду по Y

        if food_obj.fruit_type == 'apple':
            screen.blit(apple_img, (draw_x, draw_y))
        elif food_obj.fruit_type == 'orange':
            screen.blit(orange_img, (draw_x, draw_y))



    # Display the score and level
    show_score(score, level)

    # Update the display
    pygame.display.flip()

    # Control the snake speed
    clock.tick(snake_speed)

# Quit the game
pygame.quit()
sys.exit()
