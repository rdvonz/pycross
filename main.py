# -*- coding: utf-8 -*-
"""
Created on Fri Nov  4 13:26:03 2011

@author: Robert Von Z
"""
import pyglet
from game import resources, level, window, interaction
pyglet.gl.glClearColor(0.2, 0.4, 0.5, 1.0)

#Player interaction class
interact = interaction.Interaction()

#Load the current level
lvl = level.Level(pyglet.image.load('resources/levels/lv3.bmp'))
gameboard = lvl.draw_grid()
lvl.draw_numbers()
print lvl.row_numbers

@window.window.event
def on_draw():
    window.window.clear()
    window.batch.draw()


def update(dt):
    #Event loop

    #Iterates over every tile in the level
    for tile in gameboard:
        #If, on a mouse press, user is currently hovering over a tile
        if interact.hover(tile):
            #and the tile is a solution
            if tile.is_tile:
                #Change the color to black
                tile.vertex_list.colors[:12] = [0, 0, 0] * 4
            else:
                tile.is_clicked = True
    window.window.push_handlers(interact.on_mouse_press)


if __name__ == '__main__':
    pyglet.clock.schedule_interval(update, 1 / 120.0)
    pyglet.app.run()