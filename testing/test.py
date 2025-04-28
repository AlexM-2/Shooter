import pygame

pygame.init()

SCREEN_WIDTH, SCREEN_HEIGHT = 800, 800
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

clock = pygame.time.Clock()

class Coordinate:
    def __init__(self, x: float, y: float):

        x = float(x)
        y = float(y)

        super(tuple).__init__(tuple, (x, y))

        self.x = x
        self.y = y
        print("correct")
    
    def __str__(self):
        return f"({self.x}, {self.y})"

while True:
    events = pygame.event.get()
    for event in events:
        if event.type == pygame.QUIT:
            pygame.quit()
            raise SystemExit
    
    screen.fill((0,0,0))

    pygame.display.update()
    clock.tick(60)

