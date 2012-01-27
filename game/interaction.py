'''
Created on Nov 3, 2011

@author: robert
'''
import pyglet
import resources
import window
from pyglet.window import mouse
import level
#mouse_icon = pyglet.window.ImageMouseCursor(resources.cursor)
#set_cursor = window.window.set_mouse_cursor(mouse_icon)


class Interaction():
    def __init__(self, grid):
        self.LEFT = 1
        self.RIGHT = 2
        self.i = 0
        self.grid = grid
        window.window.push_handlers(self.on_mouse_press)
    def hover(self, obj, mouse_location, button):
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
        if (obj_x[1] > mouse_location[0] > obj_x[0]):
            if (obj_y[1] > mouse_location[1] > obj_y[0]):
                self.i+=1
                return button
        
    def on_mouse_press(self, x, y, buttons, modifiers):
        '''
        Event handler used to poll for mouse presses
        '''
        if buttons == mouse.LEFT:
            self.grid_interaction((x, y), self.LEFT)

        elif buttons == mouse.RIGHT:
            self.grid_interaction((x, y), self.RIGHT)
        return True


    def on_mouse_drag(self, x, y, dx, dy, buttons, modifiers):
        pass

    def grid_interaction(self, (x,y), button):
    
        #Event loop
    
        #Iterates over every tile in the level
        for tile in self.grid:
            #If, on a mouse press, user is currently hovering over a tile
            if self.hover(tile, (x,y), button) == self.LEFT:
                #and the tile is a solution
                if tile.is_tile:
                    #Change the color to black
                    tile.change_image('clicked')
                else:
                    tile.is_clicked = True
    
            elif self.hover(tile, (x,y), button) == self.RIGHT:
                if not(tile.is_marked):
                    tile.change_image('marked')
                    tile.is_marked = True
                elif tile.is_marked:
                    tile.change_image('normal')
                    tile.is_marked = False