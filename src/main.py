from pyglet.window import Window
from pyglet.window.key import KeyStateHandler
from pyglet.window.mouse import MouseStateHandler
from pyglet.app import run

window = Window(800, 800) #creates a window

keyboard = KeyStateHandler() #creates a handler that keeps track of key presses
mouse = MouseStateHandler() #creates a handler that keeps track of when the mouse is clicked

window.push_handlers(keyboard, mouse) #adds the mouse and keyboard handlers to the window so they can be used

@window.event #this function will be called when pyglet is ready to redraw the screen
def on_draw():
    print(keyboard.data)
    print(mouse.data)

run() #run the game