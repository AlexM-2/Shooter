import pygame
import time


def runTime(init = False):
    if init == True:
        global start_time
        start_time = time.time()
    return time.time() - start_time
runTime(init=True)

pygame.init()

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 800
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Shooter game")

clock = pygame.time.Clock()

player = pygame.Rect(300, 250, 50, 50)

while True:
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            raise SystemExit

    screen.fill((0,0,0))

    pygame.draw.rect(screen, (255, 0, 0), player)

    key = pygame.key.get_pressed()
    if key[pygame.K_a] == True and key[pygame.K_d] == False:
        player.move_ip(-1, 0)
    elif key[pygame.K_a] == False and key[pygame.K_d] == True:
        player.move_ip(1, 0)
    
    if key[pygame.K_w] == True and key[pygame.K_s] == False:
        player.move_ip(0, -1)
    elif key[pygame.K_w] == False and key[pygame.K_s] == True:
        player.move_ip(0, 1)

    pygame.display.update()
    clock.tick(60)