import pygame
import sys
import random
import time
from database import SnakeGameDB

class SnakeGame:
    def __init__(self):
        """Initialize game with database connection"""
        pygame.init()
        
        # Game settings
        self.width, self.height = 500, 500
        self.cell_size = 20
        self.screen = pygame.display.set_mode((self.width, self.height))
        pygame.display.set_caption('Snake Game')
        
        # Colors and assets
        self.black = (0, 0, 0)
        self.green = (0, 255, 0)
        self.apple_img = pygame.transform.scale(
            pygame.image.load("apple.png"), (30, 30))
        self.orange_img = pygame.transform.scale(
            pygame.image.load("orange.png"), (30, 30))
        
        # Game state
        self.reset_game()
        
        # Database connection
        self.db = SnakeGameDB()
        self.player_id = None
        self.clock = pygame.time.Clock()  # Initialize clock here
    
    def reset_game(self):
        """Reset game state to initial values"""
        self.snake_pos = [100, 100]
        self.snake_body = [[100, 100], [80, 100], [60, 100]]
        self.direction = 'RIGHT'
        self.change_to = self.direction
        self.score = 0
        self.level = 1
        self.snake_speed = 15
        self.food_list = []
        self.generate_initial_food()
        self.game_over = False
        self.paused = False
    
    def generate_initial_food(self):
        """Generate initial food items"""
        for _ in range(3):
            self.food_list.append(self.generate_food())
    
    def generate_food(self):
        """Generate new food with random properties"""
        food_x = random.randrange(1, (self.width // self.cell_size)) * self.cell_size
        food_y = random.randrange(1, (self.height // self.cell_size)) * self.cell_size
        weight = random.randint(1, 5)
        fruit_type = random.choice(['apple', 'orange'])
        return {
            'x': food_x,
            'y': food_y,
            'weight': weight,
            'spawn_time': time.time(),
            'type': fruit_type
        }
    
    def handle_events(self):
        """Process keyboard events"""
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    self.paused = not self.paused
                    if self.paused:
                        self.save_game()
                elif not self.paused:
                    if event.key == pygame.K_UP and self.direction != 'DOWN':
                        self.change_to = 'UP'
                    elif event.key == pygame.K_DOWN and self.direction != 'UP':
                        self.change_to = 'DOWN'
                    elif event.key == pygame.K_RIGHT and self.direction != 'LEFT':
                        self.change_to = 'RIGHT'
                    elif event.key == pygame.K_LEFT and self.direction != 'RIGHT':
                        self.change_to = 'LEFT'
        return True
    
    def update_game_state(self):
        """Update game logic"""
        if self.paused or self.game_over:
            return
        
        # Change direction
        self.direction = self.change_to
        
        # Move snake
        if self.direction == 'UP':
            self.snake_pos[1] -= self.cell_size
        elif self.direction == 'DOWN':
            self.snake_pos[1] += self.cell_size
        elif self.direction == 'LEFT':
            self.snake_pos[0] -= self.cell_size
        elif self.direction == 'RIGHT':
            self.snake_pos[0] += self.cell_size
        
        # Snake body movement
        self.snake_body.insert(0, list(self.snake_pos))
        
        # Check food collision
        food_eaten = None
        for food in self.food_list:
            if self.snake_pos == [food['x'], food['y']]:
                self.score += food['weight'] * 10
                food_eaten = food
                break
        
        # Remove eaten food and spawn new
        if food_eaten:
            self.food_list.remove(food_eaten)
        
        # Remove expired food (after 5 seconds)
        current_time = time.time()
        self.food_list = [
            food for food in self.food_list 
            if current_time - food['spawn_time'] <= 5
        ]
        
        # Ensure minimum 3 food items
        while len(self.food_list) < 3:
            self.food_list.append(self.generate_food())
        
        # Level progression
        if self.score >= self.level * 50:
            self.level += 1
            self.snake_speed += 2
        
        # Check collisions
        if (self.snake_pos[0] < 0 or self.snake_pos[0] >= self.width or
            self.snake_pos[1] < 0 or self.snake_pos[1] >= self.height or
            self.snake_pos in self.snake_body[1:]):
            self.game_over = True
            self.save_game()
        
        # Remove tail if no food eaten
        if not food_eaten:
            self.snake_body.pop()
    
    def draw(self):
        """Render game objects"""
        self.screen.fill(self.black)
        
        # Draw snake
        for block in self.snake_body:
            pygame.draw.rect(
                self.screen, self.green,
                pygame.Rect(block[0], block[1], self.cell_size, self.cell_size))
        
        # Draw food
        for food in self.food_list:
            draw_x = food['x'] - 5
            draw_y = food['y'] - 5
            
            if food['type'] == 'apple':
                self.screen.blit(self.apple_img, (draw_x, draw_y))
            else:
                self.screen.blit(self.orange_img, (draw_x, draw_y))
        
        # Draw score and level
        font = pygame.font.SysFont("arial", 25)
        score_text = font.render(
            f"Score: {self.score}  Level: {self.level}", True, self.green)
        self.screen.blit(score_text, [10, 10])
        
        # Pause message
        if self.paused:
            pause_font = pygame.font.SysFont("arial", 40)
            pause_text = pause_font.render("PAUSED", True, (255, 255, 255))
            self.screen.blit(pause_text, [
                self.width // 2 - pause_text.get_width() // 2,
                self.height // 2 - pause_text.get_height() // 2
            ])
        
        pygame.display.flip()
    
    def save_game(self):
        """Save current game state to database"""
        if self.player_id:
            game_data = {
                'snake_body': self.snake_body,
                'direction': self.direction,
                'food_list': self.food_list
            }
            self.db.save_game_session(
                self.player_id, self.score, self.level,
                len(self.snake_body), game_data
            )
    
    def show_game_over(self):
        """Display game over screen"""
        font = pygame.font.SysFont("arial", 40)
        game_over_text = font.render("GAME OVER", True, (255, 0, 0))
        score_text = font.render(f"Final Score: {self.score}", True, (255, 255, 255))
        
        self.screen.blit(game_over_text, [
            self.width // 2 - game_over_text.get_width() // 2,
            self.height // 2 - 50
        ])
        self.screen.blit(score_text, [
            self.width // 2 - score_text.get_width() // 2,
            self.height // 2 + 10
        ])
        
        pygame.display.flip()
        time.sleep(3)
    
    def run(self):
        """Main game loop"""
        # Player registration
        username = input("Enter your username: ")
        self.player_id = self.db.get_or_create_player(username)
        
        # Get player stats
        max_score, max_level, max_length = self.db.get_player_stats(self.player_id)
        if max_score:
            print(f"Welcome back! Your records - Score: {max_score}, Level: {max_level}")
        
        running = True
        while running:
            running = self.handle_events()
            
            if not self.paused and not self.game_over:
                self.update_game_state()
            
            self.draw()
            
            if self.game_over:
                self.show_game_over()
                self.reset_game()
            
            self.clock.tick(self.snake_speed)  # Use self.clock instead of clock
        
        self.db.close()
        pygame.quit()
        sys.exit()

if __name__ == "__main__":
    game = SnakeGame()
    game.run()