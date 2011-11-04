'''
Created on Nov 3, 2011

@author: robert
'''
import pyglet
import resources


class MouseMovement(object):

    '''
    This is taken mainly from experimentation and pyglet's
    example code. :D
    '''

    def __init__(self):
        self.cursor = pyglet.window.ImageMouseCursor(resources.cursor, 0, 0)

    def hover(self, other_object):
        pass
                