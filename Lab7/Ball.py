import pygame

pygame.init()
width, height = 600, 400
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Moving Ball")

x, y = width // 2, height // 2
radius = 25
speed = 20

running = True
clock = pygame.time.Clock()

while running:
    screen.fill((255, 255, 255))
    pygame.draw.circle(screen, (255, 0, 0), (x, y), radius)
    pygame.display.flip()
    clock.tick(60)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and x - radius - speed >= 0:
        x -= speed
    if keys[pygame.K_RIGHT] and x + radius + speed <= width:
        x += speed
    if keys[pygame.K_UP] and y - radius - speed >= 0:
        y -= speed
    if keys[pygame.K_DOWN] and y + radius + speed <= height:
        y += speed

pygame.quit()
