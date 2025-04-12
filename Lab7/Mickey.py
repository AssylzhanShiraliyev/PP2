import pygame
import time

pygame.init()
screen = pygame.display.set_mode((800, 800))
pygame.display.set_caption("Mickey Mouse")

def load_image(name):
    try:
        return pygame.image.load(name).convert_alpha()
    except:
        return None


clock_face = load_image("clock.png")
right_hand = load_image("rightarm.png")  
left_hand = load_image("leftarm.png")    

center = (400, 400)
clock_rect = clock_face.get_rect(center=center)

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    
    screen.fill((240, 240, 240))
    
    
    screen.blit(clock_face, clock_rect)
    
    
    current_time = time.localtime()
    minutes = current_time.tm_min
    seconds = current_time.tm_sec
    
    
    minute_angle = -((minutes + 60) * 6) % 360  
    second_angle = -(seconds * 6)
    
    
    rotated_min = pygame.transform.rotate(right_hand, minute_angle)
    rotated_sec = pygame.transform.rotate(left_hand, second_angle)
    
    screen.blit(rotated_min, rotated_min.get_rect(center=center))
    screen.blit(rotated_sec, rotated_sec.get_rect(center=center))
    
    pygame.display.flip()
    pygame.time.delay(30)

pygame.quit()