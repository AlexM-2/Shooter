import pygame

pygame.init()

SCREEN_WIDTH, SCREEN_HEIGHT = 800, 800
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

clock = pygame.time.Clock()

screen.fill((255, 255, 255))

def draw(output_surface: pygame.Surface):
    pygame.draw.rect(output_surface, (255, 0, 0), (200, 200, 200, 200))

draw(screen)

pygame.display.update()

while True:
    events = pygame.event.get()
    for event in events:
        if event.type == pygame.QUIT:
            pygame.quit()
            raise SystemExit
    
    clock.tick(20)