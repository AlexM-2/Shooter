import pyglet

window = pyglet.window.Window(800, 800) #creates a window

keyboard = pyglet.window.key.KeyStateHandler() #creates a handler that keeps track of key presses
mouse = pyglet.window.mouse.MouseStateHandler() #creates a handler that keeps track of when the mouse is clicked

window.push_handlers(keyboard, mouse) #adds the mouse and keyboard handlers to the window so they can be used

@window.event #this function will be called when pyglet is ready to redraw the screen
def on_draw():
    print(keyboard.data)
    print(mouse.data)

pyglet.app.run() #run the game