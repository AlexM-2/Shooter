import pygame
import sys
import xml.etree.ElementTree as ET
from math import floor, ceil

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

def rd(n: float):
    n = float(n)
    if n % 1 < 0.5:
        return floor(n)
    else:
        return ceil(n)

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

class Rect:
    def __init__(self, width: int, height: int, x: int, y: int, r: int = 0, style: str = "none"):

        self.width: int = width
        self.height: int = height
            
        self.x: int = x
        self.y: int = y

        self.r: int = r

        #converts style into a dictionary
        if style == "none":
            self.style = "none"
        else:
            self.style = {item.split(":")[0]: item.split(":")[1] for item in style.split(";")}
    
    def draw(self, output_surface: pygame.Surface):
        pygame.draw.rect(output_surface, pygame.Color(self.style["fill"]), (self.x, self.y, self.width, self.height))

class SVG:

    def __init__(self, file_path: str):
        self.tree = ET.parse(file_path)
        self.root = self.tree.getroot()

        #searching through the root's attributes
        for attr_name, value in self.root.items():
            if attr_name == "width":
                self.width = value
            elif attr_name == "height":
                self.height = value
        
        #searching through the root's elements
        def search_for_elements(root: ET.Element):
            for element in root:
                

                element_tag = ""
                n = 0
                valid = False
                for char in element.tag:
                    if valid == True:
                        element_tag+= char
                    if char == "}":
                        valid = True
                    n+= 1

                if element_tag == "g":
                    search_for_elements(element)
                elif element_tag == "rect":
                    attribs = element.attrib
                    element.__class__.__setattr__(
                        self,
                        attribs.get("id"), 
                        Rect(
                            rd(attribs.get("width", 50)),
                            rd(attribs.get("height", 50)),
                            rd(attribs.get("x", 0)),
                            rd(attribs.get("y", 0)),
                            rd(attribs.get("rx", 0)),
                            attribs.get("style", "none")
                        )
                    )
        
        search_for_elements(self.root)


mouse_pos = pygame.mouse.get_pos()
mouse_state = list(pygame.mouse.get_pressed(5))
mouse_velocity = (0, 0)

font = pygame.font.Font("freesansbold.ttf", 30)
text = font.render("Play Game", True, (0, 0, 0))

play_button = Sprite(pygame.Surface((200, 100)), (300, 500))

player = Sprite(pygame.Surface((100, 100)), (0,0))

on_menu_screen = True
activated = False

svg_test = SVG("Assets/test.svg")
print(f"{svg_test.rect2.width=} {svg_test.rect2.height=} {svg_test.rect2.x=} {svg_test.rect2.y=}")

def menu_screen():
    pygame.draw.rect(
        play_button.image,
        (255, 255, 255),
        (0, 0) + tuple(play_button.size),
        border_radius=20
    )
    if play_button.rect.collidepoint(mouse_pos):
        pygame.draw.rect(
            play_button.image,
            (175, 175, 175),
            (10, 10) + (play_button.size[0] - 20, play_button.size[1] - 20),
            border_radius=10
        )
        if mouse_state[0] == True:
            pygame.draw.rect(
                play_button.image,
                (200, 200, 200),
                (10, 10) + (play_button.size[0] - 20, play_button.size[1] - 20),
                border_radius=10
            )
            global activated
            activated = True
        else:
            pygame.draw.rect(
                play_button.image,
                (175, 175, 175),
                (10, 10) + (play_button.size[0] - 20, play_button.size[1] - 20),
                border_radius=10
            )
            if activated == True:
                global on_menu_screen
                on_menu_screen = False
                activated = False
    else:
        pygame.draw.rect(
            play_button.image,
            (125, 125, 125),
            (10, 10) + (play_button.size[0] - 20, play_button.size[1] - 20),
            border_radius=10
        )
        activated = False

    svg_test.rect1.draw(screen)

    play_button.image.blit(text, Vector2((play_button.size[0]/2) - (text.get_rect()[2]/2), (play_button.size[1]/2) - (text.get_rect()[3]/2)))
    screen.blit(play_button.image, play_button.rect)

def game():
    pass

while True:

    screen.fill(SCREEN_COLOR)
    play_button.image.fill(SCREEN_COLOR)
    # screen.fill((125, 125, 125))

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