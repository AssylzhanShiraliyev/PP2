import pygame
import sys
import math
pygame.init()

width, height = 800, 600
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption('Simple Paint')

# Colors
white = (255, 255, 255)
black = (0, 0 , 0)
green = (0, 255, 0)
red = (255, 0, 0)
blue = (0, 0, 255)
gray = (200, 200, 200)

# Brush and mode settings
drawing = False
brush_color = black
shape_mode = "pencil"  # 'pencil', 'rectangle', 'circle', 'eraser'

# Store the starting point for rectangle and circle
start_pos = None

class Button:
    def __init__(self, x, y, width, height, text, color, action):
        self.rect = pygame.Rect(x, y, width, height)
        self.text = text
        self.color = color
        self.action = action

    def draw(self, screen):
        pygame.draw.rect(screen, self.color, self.rect)
        font = pygame.font.Font(None, 30)
        text_surface = font.render(self.text, True, white)
        # Center the text horizontally and vertically
        text_rect = text_surface.get_rect(center=self.rect.center)
        screen.blit(text_surface, text_rect)

    def check_action(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN:
            if self.rect.collidepoint(event.pos):
                self.action()

# Brush color and action functions
def set_black():
    global brush_color
    brush_color = black
def set_green():
    global brush_color
    brush_color = green
def set_red():
    global brush_color
    brush_color = red
def set_blue():
    global brush_color
    brush_color = blue
def set_eraser():
    global shape_mode
    shape_mode = "eraser"
def set_rectangle():
    global shape_mode
    shape_mode = "rectangle"
def set_circle():
    global shape_mode
    shape_mode = "circle"
def set_pencil():
    global shape_mode
    shape_mode = "pencil"
def clear_screen():
    screen.fill(white)
def exit_app():
    pygame.quit()
    sys.exit()

# Button list 
buttons = [
    Button(10, 10, 60, 30, 'Pencil', gray, set_pencil),
    Button(80, 10, 60, 30, 'Black', black, set_black),
    Button(150, 10, 60, 30, 'Green', green, set_green),
    Button(220, 10, 60, 30, 'Red', red, set_red),
    Button(290, 10, 60, 30, 'Blue', blue, set_blue),
    Button(360, 10, 60, 30, 'Clear', gray, clear_screen),
    Button(430, 10, 60, 30, 'Exit', gray, exit_app),
    Button(500, 10, 70, 30, 'Rectangle', gray, set_rectangle),  
    Button(590, 10, 60, 30, 'Circle', gray, set_circle),
    Button(660, 10, 60, 30, 'Eraser', gray, set_eraser)
]

clear_screen()  # Fill the screen with white

# Main loop
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:  # Left click - start drawing
                drawing = True
                start_pos = pygame.mouse.get_pos()  # Store starting position
        elif event.type == pygame.MOUSEBUTTONUP:
            if event.button == 1:  # Left click - stop drawing
                drawing = False
                start_pos = None  # Reset starting position

        for button in buttons:
            button.check_action(event)

    if drawing:
        mouse_x, mouse_y = pygame.mouse.get_pos()

        if shape_mode == "pencil" and mouse_y > 50:
            pygame.draw.circle(screen, brush_color, (mouse_x, mouse_y), 5)
        elif shape_mode == "eraser" and mouse_y > 50:
            pygame.draw.circle(screen, white, (mouse_x, mouse_y), 10)
        elif shape_mode == "rectangle" and mouse_y > 50 and start_pos:
            pygame.draw.rect(screen, brush_color, pygame.Rect(start_pos[0], start_pos[1], mouse_x - start_pos[0], mouse_y - start_pos[1]), 0)  
        elif shape_mode == "circle" and mouse_y > 50 and start_pos:
            radius = int(math.sqrt((mouse_x - start_pos[0])**2 + (mouse_y - start_pos[1])**2))
            pygame.draw.circle(screen, brush_color, start_pos, radius, 0)  

    pygame.draw.rect(screen, gray, (0, 0, width, 50))  # Drawing the button panel

    # Draw all buttons
    for button in buttons:
        button.draw(screen)

    pygame.display.flip()
