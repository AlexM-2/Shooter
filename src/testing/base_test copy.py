import pygame
from pathlib import Path

pygame.init()

SCREEN_WIDTH, SCREEN_HEIGHT = 800, 800
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

clock = pygame.time.Clock()

Vector2 = pygame.math.Vector2
Color = pygame.color.Color

class Border_val(int):

    def __new__(cls, val: int, shortened: bool, name: str):
        return super(Border_val, cls).__new__(cls, val)

    def __init__(self, val: int, shortened: bool, name: str):

        super().__init__()

        self.shortened: bool = shortened
        self.name: str = name

class Border(list):
    def __init__(
        self,
        shortened: int = -1,
        top_left: int = -1,
        top_right: int = -1,
        bottom_left: int = -1,
        bottom_right: int = -1
    ):
        super().__init__()
        
        if top_left == -1:
            self.top_left: Border_val = Border_val(shortened, True, "top_left")
        else:
            self.top_left: Border_val = Border_val(top_left, False, "top_left")
        
        if top_right == -1:
            self.top_right: Border_val = Border_val(shortened, True, "top_right")
        else:
            self.top_right: Border_val = Border_val(top_right, False, "top_right")

        if bottom_left == -1:
            self.bottom_left: Border_val = Border_val(shortened, True, "bottom_left")
        else:
            self.bottom_left: Border_val = Border_val(bottom_left, False, "bottom_left")

        if bottom_right == -1:
            self.bottom_right: Border_val = Border_val(shortened, True, "bottom_right")
        else:
            self.bottom_right: Border_val = Border_val(bottom_right, False, "bottom_right")
        
        self.append(self.top_left)
        self.append(self.top_right)
        self.append(self.bottom_left)
        self.append(self.bottom_right)
        
        if self.top_left.shortened == True and self.top_right.shortened == True and self.bottom_left.shortened == True and self.bottom_right.shortened == True:
            self.is_shortened: bool = True
            self.shortened: int = shortened

            if shortened == -1:
                self.is_default = True
            else:
                self.is_default = False
        else:
            self.is_shortened: bool = False
            self.is_default = False

class Surface(pygame.Surface):
    def __init__(self, pos: Vector2, size: Vector2, width: int, border: Border):
        self.pos: Vector2 = pos
        self.size = size

class Sprite(pygame.sprite.Sprite):
    def __init__(self, pos: Vector2, size: Vector2, color: Color):
        super().__init__()

        self.image = pygame.Surface(size)
        self.image.fill(color)
        
        self.rect = Rect(screen,)
    
    def draw():
        pygame.draw.rect()

while True:
    events = pygame.event.get()
    for event in events:
        if event.type == pygame.QUIT:
            pygame.quit()
            raise SystemExit
    
    screen.fill((0,0,0))

    pygame.display.update()
    clock.tick(60)