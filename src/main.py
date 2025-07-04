import sys
import pygame
import svgutil

pygame.init()

SCREEN_WIDTH, SCREEN_HEIGHT = 800, 800
SCREEN_COLOR = pygame.color.Color(3, 6, 22)
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

clock = pygame.time.Clock()

allowed_events = [
    pygame.QUIT,
    pygame.MOUSEBUTTONDOWN,
    pygame.MOUSEBUTTONUP,
    pygame.MOUSEMOTION,
]
pygame.event.set_blocked(None) #None means all will be blocked
pygame.event.set_allowed(allowed_events)

Vector2 = pygame.math.Vector2
Color = pygame.color.Color

class Sprite(pygame.sprite.Sprite):
    def __init__(self, image: pygame.Surface, pos: Vector2, *groups):

        super().__init__(*groups)

        rect = image.get_rect()

        super().__setattr__("pos", pos)
        super().__setattr__("size", Vector2(rect[2:]))
        super().__setattr__("rect", pygame.rect.Rect(*pos, *rect[2:]))
            
        super().__setattr__("image", image)
    
    def __setattr__(self, name: str, value):

        if name == "pos":
            super().__setattr__("pos", Vector2(value))
            super().__setattr__("rect", pygame.rect.Rect(value | self.size))
        elif name == "size":
            super().__setattr__("size", Vector2(value))
            super().__setattr__("rect", pygame.rect.Rect(self.pos | value))
        elif name == "rect":
            self.rect = value
            super().__setattr__("pos", Vector2(value[:2]))
            super().__setattr__("size", Vector2(value[2:]))
        else:
            super().__setattr__(name, value)

mouse_pos = pygame.mouse.get_pos()
mouse_state = list(pygame.mouse.get_pressed(5))
mouse_velocity = (0, 0)

svg = svgutil.SVGFile("Assets/play_button.svg")
play_button = svg.render()

on_menu_screen = True
activated = False

def menu_screen():
    # pygame.draw.rect(
    #     play_button.image,
    #     (255, 255, 255),
    #     (0, 0) + tuple(play_button.size),
    #     border_radius=20
    # )
    # if play_button.rect.collidepoint(mouse_pos):
    #     pygame.draw.rect(
    #         play_button.image,
    #         (175, 175, 175),
    #         (10, 10) + (play_button.size[0] - 20, play_button.size[1] - 20),
    #         border_radius=10
    #     )
    #     if mouse_state[0] == True:
    #         pygame.draw.rect(
    #             play_button.image,
    #             (200, 200, 200),
    #             (10, 10) + (play_button.size[0] - 20, play_button.size[1] - 20),
    #             border_radius=10
    #         )
    #         global activated
    #         activated = True
    #     else:
    #         pygame.draw.rect(
    #             play_button.image,
    #             (175, 175, 175),
    #             (10, 10) + (play_button.size[0] - 20, play_button.size[1] - 20),
    #             border_radius=10
    #         )
    #         if activated == True:
    #             global on_menu_screen
    #             on_menu_screen = False
    #             activated = False
    # else:
    #     pygame.draw.rect(
    #         play_button.image,
    #         (125, 125, 125),
    #         (10, 10) + (play_button.size[0] - 20, play_button.size[1] - 20),
    #         border_radius=10
    #     )
    #     activated = False

    screen.blit(play_button, (0, 0))

def game():
    pass

while True:

    screen.fill(SCREEN_COLOR)

    all_events = pygame.event.get()
    for event in all_events:
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                mouse_state[0] = True
            elif event.button == 2:
                mouse_state[1] = True
            elif event.button == 3:
                mouse_state[2] = True
            elif event.button == 4:
                mouse_state[3] = True
            elif event.button == 5:
                mouse_state[4] = True
        elif event.type == pygame.MOUSEBUTTONUP:
            if event.button == 1:
                mouse_state[0] = False
            elif event.button == 2:
                mouse_state[1] = False
            elif event.button == 3:
                mouse_state[2] = False
            elif event.button == 4:
                mouse_state[3] = False
            elif event.button == 5:
                mouse_state[4] = False
        elif event.type == pygame.MOUSEMOTION:
            mouse_pos = event.pos
            mouse_velocity = event.rel
    
    if on_menu_screen:
        menu_screen()
    else:
        game()
    
    pygame.display.update()
    clock.tick(60)