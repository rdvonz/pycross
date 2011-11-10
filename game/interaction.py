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


class Interaction(object):
    def __init__(self):
        self.mouse_location = (0, 0)

    def hover(self, obj):
        '''
        Checks if mouse is hovering over an object
        '''

        #X bounds of object
        obj_x = ((obj.x - (obj.width / 2)),
                 (obj.x + (obj.width / 2)))

        #Y bounds of object
        obj_y = (obj.y - obj.height / 2,
                 obj.y + obj.height / 2)

        #Checks if mouse coords are intersecting with object bounds
        if (obj_x[1] > self.mouse_location[0] > obj_x[0]):
            if (obj_y[1] > self.mouse_location[1] > obj_y[0]):
                return True

    def on_mouse_press(self, x, y, buttons, modifiers):
        '''
        Event handler used to poll for mouse presses
        '''
        if buttons == mouse.LEFT:
            self.mouse_location = (x, y)
            return True