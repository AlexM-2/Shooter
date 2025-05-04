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
        

pygame.Vector2

class Mouse:
    def __init__(self, state: Mouse_state = (False, False, False, False, False),  pos: pygame.Vector2 = pygame.mouse.get_pos()):
        self.pos: pygame.Vector2 = pygame.Vector2(pos[0], pos[1])

        self.state: Mouse_state = Mouse_state(state)

mouse = Mouse()

playButton = pygame.sprite.Sprite()

while True:

    all_events = pygame.event.get()
    for event in all_events:
        if event.type == pygame.QUIT:
            pygame.quit()
            raise SystemExit
        elif event.type == pygame.MOUSEBUTTONDOWN:
            mouse.pos = event.pos
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
            mouse.pos = event.pos
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
        print(f"{mouse.state=}")
    
    screen.fill((3, 6, 22))

    pygame.display.update()
    clock.tick(60)