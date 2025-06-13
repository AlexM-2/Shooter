import pygame

pygame.init()

SCREEN_WIDTH, SCREEN_HEIGHT = 800, 800
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

clock = pygame.time.Clock()

while True:
    events = pygame.event.get()
    for event in events:
        if event.type == pygame.QUIT:
            pygame.quit()
            raise SystemExit
    
    screen.fill((255, 255, 255))

    pygame.draw.rect(screen, pygame.color.Color(255, 0, 0, ), (10, 50, 100, 150))

    pygame.display.update()
    clock.tick(60)