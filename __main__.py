import pygame

pygame.init()

SCREEN_WIDTH, SCREEN_HEIGHT = 800, 800
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

clock = pygame.time.Clock()

allowed_events = [
    pygame.QUIT,
    pygame.MOUSEBUTTONDOWN,
    pygame.MOUSEBUTTONUP,
]
pygame.event.set_blocked(None) #None means all will be blocked
for event in allowed_events:
    pygame.event.set_allowed(event)

class Mouse_state(list):

    def __new__(cls, *args):
        return super().__new__(cls, args)

    def __init__(self, state):
        
        self.state = state

        self.mb1 = state[0]
        self.append(state[0])

        self.mb2 = state[1]
        self.append(state[1])

        self.mb3 = state[2]
        self.append(state[2])

        self.scroll_up = state[3]
        self.append(state[3])

        self.scroll_down = state[4]
        self.append(state[4])

class Mouse:
    def __init__(self, state: Mouse_state = pygame.mouse.get_pressed(5),  pos: pygame.Vector2 = pygame.mouse.get_pos()):
        self.pos: pygame.Vector2 = pygame.Vector2(pos[0], pos[1])

        self.state: Mouse_state = Mouse_state(state)

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
    
    # def __setattr__(self, name, value):
    #     if name == "shortened":
    #         self.__init__()
    #     elif name == "top_left":
    #         self[0] = value
    #     elif name == "top_right":
    #         self[1] = value
    #     elif name == "bottom_left":
    #         self[2] = value
    #     elif name == "bottom_right":
    #         self[3] = value
    #     super().__setattr__(name, value)

    # def __delattr__(self, name):
    #     if name == "border":
    #         self.__init__(-1, self.top_left, self.top_right, self.bottom_left, self.bottom_right)
    #     elif name == "top_left":
    #         self.__init__(self.shortened, -1, self.top_right, self.bottom_left, self.bottom_right)
    #     elif name == "top_right":
    #         self.__init__(self.shortened, self.top_left, -1, self.bottom_left, self.bottom_right)
    #     elif name == "bottom_left":
    #         self.__init__(self.shortened, self.top_left, self.top_right, -1, self.bottom_right)
    #     elif name == "bottom_right":
    #         self.__init__(self.shortened, -1, self.top_right, self.bottom_left, -1)
    #     elif name == "border":
    #         self.__init__(-1, self.top_left, self.top_right, self.bottom_left, self.bottom_right)
    #     else:
    #         super().__delattr__(name)

class Rect(pygame.Rect):
    def __init__(
            self,
            surface: pygame.Surface,
            color: pygame.Color,
            size: pygame.Vector2,
            pos: pygame.Vector2,
            width: int = 0,
            border: Border = Border()
            ):
        
        super().__init__(pos, size)

        self.surface: pygame.Surface = surface
        self.color: pygame.Color = color

        self.rect: pygame.Rect = pygame.Rect(pos, size)
        self.size: pygame.Vector2 = size
        self.pos: pygame.Vector2 = pos

        self.width: int = width
        self.border = border
    
    def draw(
        self,
        surface: pygame.Surface | None = None,
        color: pygame.Color | None = None,
        rect: pygame.Rect | None = None,
        width: int = None,
        border: Border | None = None,
    ):
        """Draws self to self.surface"""

        #o short for output
        if surface == None:
            o_surface = self.surface
        else:
            o_surface = surface
        
        if color == None:
            o_color = self.color
        else:
            o_color = color
        
        if rect == None:
            o_rect = self.rect
        else:
            o_rect = rect

        if width == None:
            o_width = self.width
        else:
            o_width = width
        
        short_in_func = self.border.is_shortened
        default_in_func = self.border.is_default
        
        def check_validity(obj, other_return_object):
            if obj == -1:
                return other_return_object
            else:
                return obj

        if border == None:
            if short_in_func:
                o_border_short = self.border.shortened
            o_border_full = self.border
        else:
            default_in_func = False
            if border.is_shortened:
                o_border_short = border.shortened
            
            o_border_full = Border(
                -1,
                check_validity(border[0], self.border[0]),
                check_validity(border[1], self.border[1]),
                check_validity(border[2], self.border[2]),
                check_validity(border[3], self.border[3]),
            )
            if not o_border_full.is_default:
                short_in_func = False
                default_in_func = False
        
        print(border)
        print(o_border_full)

        #o is short for output
        match (short_in_func, default_in_func, o_width):
            case (True, True, 0):
                print("176")
                pygame.draw.rect(o_surface, o_color, o_rect)
            case (True, False, 0):
                print("179")
                pygame.draw.rect(o_surface, o_color, o_rect, border_radius=o_border_short)
            case (True, False, _):
                print("182")
                pygame.draw.rect(o_surface, o_color, o_rect, o_width, o_border_short)
            case (True, True, _):
                print("185")
                pygame.draw.rect(o_surface, o_color, o_rect, o_width)
            case (False, False, _):
                print("191")
                print(o_border_full[3])
                pygame.draw.rect(o_surface,
                    o_color,
                    o_rect,
                    o_width,
                    border_top_left_radius=o_border_full[0],
                    border_top_right_radius=o_border_full[1],
                    border_bottom_left_radius=o_border_full[2],
                    border_bottom_right_radius=o_border_full[3]
                )

#         print(f"139| <{self.color=}> <{self.rect=}> <{self.width=}> <{self.border=}> <{self.border.shortened=}>\n \
# <{self.border.is_shortened=}> <{self.border.default=}> <{self.surface}>\n")
        return self

mouse = Mouse()

playButton = Rect(screen, (255, 255, 255), (200, 100), (300, 500))

while True:

    screen.fill((3, 6, 22))
    # screen.fill((125, 125, 125))

    all_events = pygame.event.get()
    for event in all_events:
        if event.type == pygame.QUIT:
            pygame.quit()
            raise SystemExit
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                mouse.state.mb1 = True
                mouse.state[0] = True
            elif event.button == 2:
                mouse.state.mb2 = True
                mouse.state[1] = True
            elif event.button == 3:
                mouse.state.mb3 = True
                mouse.state[2] = True
            elif event.button == 4:
                mouse.state.scroll_up = True
                mouse.state[3] = True
            elif event.button == 5:
                mouse.state.scroll_down = True
                mouse.state[4] = True
        elif event.type == pygame.MOUSEBUTTONUP:
            if event.button == 1:
                mouse.state.mb1 = False
                mouse.state[0] = False
            elif event.button == 2:
                mouse.state.mb3 = False
                mouse.state[1] = False
            elif event.button == 3:
                mouse.state.mb2 = False
                mouse.state[2] = False
            elif event.button == 4:
                mouse.state.scroll_up = False
                mouse.state[3] = False
            elif event.button == 5:
                mouse.state.scroll_down = False
                mouse.state[4] = False
    mouse.pos = pygame.mouse.get_pos()
    
    playButton.draw()

    pygame.display.update()
    clock.tick(60)