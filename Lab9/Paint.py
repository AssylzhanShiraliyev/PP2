import pygame
import sys
import math

pygame.init()

# Screen dimensions
width, height = 800, 600
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption('Simple Paint')
clock = pygame.time.Clock()

# Colors
white = (255, 255, 255)
black = (0, 0, 0)
green = (0, 255, 0)
red = (255, 0, 0)
blue = (0, 0, 255)
gray = (200, 200, 200)

# Brush and mode settings
drawing = False
brush_color = black
shape_mode = "pencil"
start_pos = None

class Button:
    def __init__(self, x, y, width, height, text, color, action):
        self.rect = pygame.Rect(x, y, width, height)
        self.text = text
        self.color = color
        self.action = action

    def draw(self, screen):
        pygame.draw.rect(screen, self.color, self.rect)
        font = pygame.font.Font(None, 24)
        text_surface = font.render(self.text, True, white)
        text_rect = text_surface.get_rect(center=self.rect.center)
        screen.blit(text_surface, text_rect)

    def check_action(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN:
            if self.rect.collidepoint(event.pos):
                self.action()

# Functions for tools
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

def set_square():
    global shape_mode
    shape_mode = "square"

def set_right_triangle():
    global shape_mode
    shape_mode = "right_triangle"

def set_equilateral_triangle():
    global shape_mode
    shape_mode = "equilateral_triangle"

def set_rhombus():
    global shape_mode
    shape_mode = "rhombus"

def set_pencil():
    global shape_mode
    shape_mode = "pencil"

def clear_screen():
    screen.fill(white)

def exit_app():
    pygame.quit()
    sys.exit()

# Shape drawing functions
def draw_square(start_pos, end_pos):
    size = min(abs(end_pos[0] - start_pos[0]), abs(end_pos[1] - start_pos[1]))
    rect = pygame.Rect(start_pos[0], start_pos[1], size, size)
    pygame.draw.rect(screen, brush_color, rect)

def draw_right_triangle(start_pos, end_pos):
    base = end_pos[0] - start_pos[0]
    height = end_pos[1] - start_pos[1]
    points = [(start_pos[0], start_pos[1]),
              (start_pos[0] + base, start_pos[1]),
              (start_pos[0], start_pos[1] + height)]
    pygame.draw.polygon(screen, brush_color, points)

def draw_equilateral_triangle(start_pos, end_pos):
    side_length = math.sqrt((end_pos[0] - start_pos[0])**2 + (end_pos[1] - start_pos[1])**2)
    height = (math.sqrt(3) / 2) * side_length
    points = [(start_pos[0], start_pos[1]),
              (start_pos[0] + side_length, start_pos[1]),
              (start_pos[0] + side_length / 2, start_pos[1] - height)]
    pygame.draw.polygon(screen, brush_color, points)

def draw_rhombus(start_pos, end_pos):
    center_x = (start_pos[0] + end_pos[0]) // 2
    center_y = (start_pos[1] + end_pos[1]) // 2
    half_width = abs(end_pos[0] - start_pos[0]) // 2
    half_height = abs(end_pos[1] - start_pos[1]) // 2
    points = [
        (center_x, start_pos[1]),    # Top
        (end_pos[0], center_y),      # Right
        (center_x, end_pos[1]),      # Bottom
        (start_pos[0], center_y)     # Left
    ]
    pygame.draw.polygon(screen, brush_color, points)

# Buttons
buttons = [
    Button(10, 10, 80, 30, 'Pencil', gray, set_pencil),
    Button(100, 10, 80, 30, 'Black', black, set_black),
    Button(190, 10, 80, 30, 'Green', green, set_green),
    Button(280, 10, 80, 30, 'Red', red, set_red),
    Button(370, 10, 80, 30, 'Blue', blue, set_blue),
    Button(460, 10, 80, 30, 'Clear', gray, clear_screen),
    Button(550, 10, 80, 30, 'Exit', gray, exit_app),
    Button(640, 10, 80, 30, 'Rectangle', gray, set_rectangle),
    Button(730, 10, 80, 30, 'Circle', gray, set_circle),
    Button(10, 50, 80, 30, 'Eraser', gray, set_eraser),
    Button(100, 50, 80, 30, 'Square', gray, set_square),
    Button(200, 50, 80, 30, 'Right Tri', gray, set_right_triangle),
    Button(280, 50, 80, 30, 'Eq. Tri', gray, set_equilateral_triangle),
    Button(370, 50, 80, 30, 'Rhombus', gray, set_rhombus)
]

clear_screen()

# Main loop
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                drawing = True
                start_pos = pygame.mouse.get_pos()

        elif event.type == pygame.MOUSEBUTTONUP:
            if event.button == 1:
                drawing = False
                end_pos = pygame.mouse.get_pos()
                if start_pos:
                    if shape_mode == "rectangle":
                        pygame.draw.rect(screen, brush_color, pygame.Rect(start_pos[0], start_pos[1], end_pos[0] - start_pos[0], end_pos[1] - start_pos[1]), 0)
                    elif shape_mode == "circle":
                        radius = int(math.sqrt((end_pos[0] - start_pos[0]) ** 2 + (end_pos[1] - start_pos[1]) ** 2))
                        pygame.draw.circle(screen, brush_color, start_pos, radius, 0)
                    elif shape_mode == "square":
                        draw_square(start_pos, end_pos)
                    elif shape_mode == "right_triangle":
                        draw_right_triangle(start_pos, end_pos)
                    elif shape_mode == "equilateral_triangle":
                        draw_equilateral_triangle(start_pos, end_pos)
                    elif shape_mode == "rhombus":
                        draw_rhombus(start_pos, end_pos)
                start_pos = None

        for button in buttons:
            button.check_action(event)

    # Drawing while holding mouse
    if drawing and start_pos:
        mouse_x, mouse_y = pygame.mouse.get_pos()
        if shape_mode == "pencil" and mouse_y > 80:
            pygame.draw.circle(screen, brush_color, (mouse_x, mouse_y), 5)
        elif shape_mode == "eraser" and mouse_y > 80:
            pygame.draw.circle(screen, white, (mouse_x, mouse_y), 10)

    # Draw the toolbar background
    pygame.draw.rect(screen, gray, (0, 0, width, 80))

    # Draw all buttons
    for button in buttons:
        button.draw(screen)

    pygame.display.flip()
    clock.tick(60)
