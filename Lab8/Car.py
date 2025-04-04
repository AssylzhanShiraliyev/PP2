import pygame
import random

# Initialize Pygame
pygame.init()

# Window dimensions
width, height = 400, 600
win = pygame.display.set_mode((width, height))
pygame.display.set_caption("Racer")

# Colors
white = (255, 255, 255)
gray = (128, 128, 128)
red = (255, 0, 0)

# Load images
background = pygame.image.load("AnimatedStreet.png")
player = pygame.image.load("Player.png")
enemy = pygame.image.load("Enemy.png")
coin = pygame.image.load("Coin.png") # Coin image

# Load sounds
pygame.mixer.music.load("background.wav")
pygame.mixer.music.play(-1) # Loop background music
crash_sound = pygame.mixer.Sound("crash.wav")  # Load crash sound 

# Fonts for text
font = pygame.font.SysFont("Verdana", 20)
game_over_font = pygame.font.SysFont("Verdana", 60)

# Player variables
player_x = 160
player_y = 480
player_speed = 5

# Enemy variables
enemy_x = random.randint(40, 360)
enemy_y = -100
enemy_speed = 5

# Coins
num_coins = 5 # Number of coins
coins = [] # List to store coins

# Generate initial coins
for i in range(num_coins):
    coin_x = random.randint(40, 360)
    coin_y = random.randint(-150, -50)
    coins.append([coin_x, coin_y])

# Score variables
score = 0
coins_collected = 0

# Timer to increase enemy speed
INC_SPEED = pygame.USEREVENT + 1
pygame.time.set_timer(INC_SPEED, 1000)

# Frames per second (FPS)
clock = pygame.time.Clock()
FPS = 60

running = True
game_over = False

# Function to check if the coin collides with the player
def check_collision_with_player(coin_pos, player_rect):
    coin_rect = coin.get_rect(topleft=(coin_pos[0], coin_pos[1]))
    return coin_rect.colliderect(player_rect)

# Main game loop
while running:
    clock.tick(FPS)

    # Event handling
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == INC_SPEED:
            enemy_speed += 0.5 # Increase enemy speed

    if not game_over:
        # Player controls (left/right movement)
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT] and player_x > 0:
            player_x -= player_speed
        if keys[pygame.K_RIGHT] and player_x < width - player.get_width():
            player_x += player_speed

        # Enemy movement
        enemy_y += enemy_speed
        if enemy_y > height:
            enemy_y = -100
            enemy_x = random.randint(40, 360)
            score += 1
        
        # Coin movement
        for coin_pos in coins[:]:
            coin_pos[1] += 5 # Move coins downwards
            if coin_pos[1] > height:
                coin_pos[1] = random.randint(-150, -50)
                coin_pos[0] = random.randint(40, 360)
            
            # Check if the coin collides with the player
            player_rect = player.get_rect(topleft=(player_x, player_y))
            if check_collision_with_player(coin_pos, player_rect):
                coins_collected += 1 # Increase coin count
                coins.remove(coin_pos) # Remove collected coin
                # Generate a new coin
                new_coin_x = random.randint(40, 360)
                new_coin_y = random.randint(-150, -50)
                coins.append([new_coin_x, new_coin_y])

            # Check if the coin collides with the enemy (avoid passing through the enemy)
            enemy_rect = enemy.get_rect(topleft=(enemy_x, enemy_y))
            if check_collision_with_player(coin_pos, enemy_rect):
                coin_pos[1] = random.randint(-150, -50)  # Reset coin if it collides with enemy
                coin_pos[0] = random.randint(40, 360)  # Randomize position

        # Collision detection with enemy
        player_rect = player.get_rect(topleft=(player_x, player_y))
        enemy_rect = enemy.get_rect(topleft=(enemy_x, enemy_y))

        if player_rect.colliderect(enemy_rect):
            game_over = True
            pygame.mixer.music.stop() # Stop background music
            crash_sound.play()  # Play crash sound
            
        # Drawing
        win.blit(background, (0, 0))  # Draw background
        win.blit(player, (player_x, player_y))  # Draw player
        win.blit(enemy, (enemy_x, enemy_y))  # Draw enemy
        
        # Draw coins
        for coin_pos in coins:
            win.blit(coin, (coin_pos[0], coin_pos[1]))

        # Display score and collected coins
        score_text = font.render(f"Score: {score}", True, white)
        coin_text = font.render(f"Coins: {coins_collected}", True, white)
        win.blit(score_text, (10, 10))
        win.blit(coin_text, (300, 10))

    else:
        # If the game is over, display Game Over
        win.fill(red)
        game_over_text = game_over_font.render("Game Over", True, white)
        
        # Calculate the center position for the text
        text_rect = game_over_text.get_rect(center=(width//2, height//2))
        win.blit(game_over_text, text_rect)

    pygame.display.update() # Update the screen

pygame.quit() # Quit Pygame
