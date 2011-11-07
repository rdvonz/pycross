'''
Created on Nov 3, 2011

@author: robert
'''
import pyglet
import resources
import window
from pyglet.window import mouse

#mouse_icon = pyglet.window.ImageMouseCursor(resources.cursor)
#set_cursor = window.window.set_mouse_cursor(mouse_icon)

mouse_location = (0,0)

@window.window.event
def on_mouse_press(x, y, buttons, modifiers):
    global mouse_location
    if buttons == mouse.LEFT:
        mouse_location = (x, y)
        return True

def hover(mouse, objtwo):
    global mouse_location
    bx = ((objtwo.x - (objtwo.width / 2)), (objtwo.x + (objtwo.width / 2)))
    by = (objtwo.y - objtwo.height / 2, objtwo.y + objtwo.height / 2)
    if (bx[1] > mouse_location[0] > bx[0]):
        if (by[1] > mouse_location[1] > by[0]):
            return True


