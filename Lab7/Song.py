import pygame

pygame.init()
screen = pygame.display.set_mode((600, 400))
pygame.display.set_caption("Music Player")

pygame.mixer.init()

playlist = ["song1.mp3", "song2.mp3"]
current_track = 0

is_paused = False

def play_track(index):
    pygame.mixer.music.load(playlist[index])
    pygame.mixer.music.play()

font = pygame.font.SysFont("Arial", 28)
instructions = font.render("P = Play | S = Pause | N = Next | B = Back", True, (0, 0, 0))

running = True
while running:
    screen.fill((255, 255, 255))
    screen.blit(instructions, (50, 180))
    pygame.display.flip()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_p:
                if is_paused:
                    pygame.mixer.music.unpause()
                    is_paused = False
                else:
                    play_track(current_track)
                    is_paused = False
            if event.key == pygame.K_s:
                pygame.mixer.music.pause()
                is_paused = True
            if event.key == pygame.K_n:
                current_track = (current_track + 1) % len(playlist)
                play_track(current_track)
                is_paused = False
            if event.key == pygame.K_b:
                current_track = (current_track - 1) % len(playlist)
                play_track(current_track)
                is_paused = False

pygame.quit()
