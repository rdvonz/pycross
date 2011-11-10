# -*- coding: utf-8 -*-
"""
Created on Fri Nov  4 13:26:03 2011

@author: Robert Von Z
"""
import pyglet
from game import resources, level, window, interaction
pyglet.gl.glClearColor(0.2, 0.4, 0.5, 1.0)


#Load the current level
lvl = level.Level(pyglet.image.load('resources/levels/lv2.bmp'))
gameboard = lvl.draw_grid()
lvl.draw_column_numbers()
lvl.draw_row_numbers()

#Player interaction class
interact = interaction.Interaction(gameboard)

print lvl.row_numbers
window.window.push_handlers(interact.on_mouse_press)
@window.window.event
def on_draw():
    window.window.clear()
    window.batch.draw()




if __name__ == '__main__':
    pyglet.app.run()