import pygame

pygame.init()

SCREEN_WIDTH, SCREEN_HEIGHT = 800, 800
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

clock = pygame.time.Clock()

screen.fill((255, 255, 255))
surf = pygame.Surface((200, 200), pygame.SRCALPHA)
pygame.draw.rect(
    surf,
    (0, 0, 255, 125),
    (0, 0, 200, 200)
)

screen.blit(surf, (0, 0))

pygame.display.update()

while True:
    events = pygame.event.get()
    for event in events:
        if event.type == pygame.QUIT:
            pygame.quit()
            raise SystemExit

    clock.tick(20)