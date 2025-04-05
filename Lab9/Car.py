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
coin = pygame.image.load("Coin.png")        # Normal coin
coin_gold = pygame.image.load("GoldCoin.png")  # Golden coin

# Load sounds
pygame.mixer.music.load("background.wav")
pygame.mixer.music.play(-1)  # Loop background music
crash_sound = pygame.mixer.Sound("crash.wav")  # Sound on collision

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

# Score and coin variables
score = 0
coins_collected = 0
coins_for_speed = 5  # Number of coins required to increase speed
num_coins = 5
coins = []

# Class for coin with type and weight
class Coin:
    def __init__(self, x, y, weight, coin_type):
        self.x = x
        self.y = y
        self.weight = weight
        self.type = coin_type  # "normal" or "gold"

# Function to create a random coin
def create_random_coin():
    x = random.randint(40, 360)
    y = random.randint(-150, -50)
    if random.random() < 0.3:  # 30% chance of gold coin
        weight = random.randint(4, 5)
        coin_type = "gold"
    else:
        weight = random.randint(1, 3)
        coin_type = "normal"
    return Coin(x, y, weight, coin_type)

# Generate initial coins
for _ in range(num_coins):
    coins.append(create_random_coin())

# Timer to increase enemy speed
INC_SPEED = pygame.USEREVENT + 1
pygame.time.set_timer(INC_SPEED, 1000)

# Frames per second
clock = pygame.time.Clock()
FPS = 60

running = True
game_over = False

# Check collision between player and a coin
def check_collision_with_player(coin_obj, player_rect):
    if coin_obj.type == "gold":
        image = coin_gold
    else:
        image = coin
    coin_rect = image.get_rect(topleft=(coin_obj.x, coin_obj.y))
    return coin_rect.colliderect(player_rect)

# Main game loop
while running:
    clock.tick(FPS)

    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == INC_SPEED:
            enemy_speed += 0.5

    if not game_over:
        # Player controls
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT] and player_x > 0:
            player_x -= player_speed
        if keys[pygame.K_RIGHT] and player_x < width - player.get_width():
            player_x += player_speed

        # Move enemy
        enemy_y += enemy_speed
        if enemy_y > height:
            enemy_y = -100
            enemy_x = random.randint(40, 360)
            score += 1

        # Move coins
        for coin_obj in coins:
            coin_obj.y += 5
            if coin_obj.y > height:
                coins.remove(coin_obj)
                coins.append(create_random_coin())

        # Check collisions with coins
        player_rect = player.get_rect(topleft=(player_x, player_y))
        for coin_obj in coins[:]:
            if check_collision_with_player(coin_obj, player_rect):
                coins_collected += coin_obj.weight
                score += coin_obj.weight * 10
                coins.remove(coin_obj)
                coins.append(create_random_coin())

                if coins_collected >= coins_for_speed:
                    enemy_speed += 1

        # Check collision with enemy
        enemy_rect = enemy.get_rect(topleft=(enemy_x, enemy_y))
        if player_rect.colliderect(enemy_rect):
            game_over = True
            pygame.mixer.music.stop()
            crash_sound.play()

        # Drawing
        win.blit(background, (0, 0))
        win.blit(player, (player_x, player_y))
        win.blit(enemy, (enemy_x, enemy_y))
        for coin_obj in coins:
            image = coin_gold if coin_obj.type == "gold" else coin
            win.blit(image, (coin_obj.x, coin_obj.y))

        # Display score
        score_text = font.render(f"Score: {score}", True, white)
        coin_text = font.render(f"Coins: {coins_collected}", True, white)
        win.blit(score_text, (10, 10))
        win.blit(coin_text, (300, 10))

    else:
        win.fill(red)
        game_over_text = game_over_font.render("Game Over", True, white)
        text_rect = game_over_text.get_rect(center=(width // 2, height // 2))
        win.blit(game_over_text, text_rect)

    pygame.display.update()

pygame.quit()
