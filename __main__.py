import time

import pygame

pygame.init()

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

class Circle:
    def __init__(self, parent: pygame.Surface, center: Coordinate, radius: float, color: pygame.Color):
        self.parent = parent
        self.center = center
        self.radius = radius
        self.color = color
    
    def draw(self):
        pygame.draw.circle(self.parent, self.color, self.center, self.radius)

class Rect:
    def __init__(self, position: Coordinate, size: Coordinate, color: pygame.Color, border: float, full_border: tuple[float, float, float, float]):
        self.postion = position

        self.size = size

class Group:
    def __init__(self, *objects: pygame.Rect | pygame.Surface | Circle | Rect):
        pass

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 800
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

playButton = pygame.Rect(300, 600, 200, 100)

while True:
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()
            
        screen.fill((3,6,22))

        pygame.draw.rect(screen, (75, 75, 75), playButton)
        # pygame.draw.circle()

        pygame.display.update()
        time.sleep(0.01)