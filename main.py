# -*- coding: utf-8 -*-
"""
Created on Fri Nov  4 13:26:03 2011

@author: Robert Von Z
"""
import pyglet
from game import resources, level, window, mouse
pyglet.gl.glClearColor(0.2, 0.4, 0.5, 1.0)

lvl = level.Level(pyglet.image.load('resources/levels/testgrid.bmp'))

lvl.draw_picross()
secs = 60*15
cur_time = 0
decrement = 5
time = pyglet.text.Label(str(secs),
                         x = 50,
                         y = 400)

@window.window.event
def on_draw():
    window.window.clear()
    window.batch.draw()
    time.draw()
def update(dt):
    window.window.clear()
    global secs
    global cur_time
    global time
    global decrement
    global cur_color
    cur_time+=dt
    
    if cur_time >= 1:
        secs -= 1
        time.begin_update()
        time = pyglet.text.Label(str(secs),
                             x = 50,
                             y = 400,
                             batch = window.batch)
        cur_time = 0
    if secs <= 0:
        print "you lost"
        #exit(0)
    for cell in lvl.cell_list:
            print cell.is_tile
                
    window.window.push_handlers(mouse.on_mouse_press)


if __name__ == '__main__':
    pyglet.clock.schedule_interval(update, 1 / 120.0)
    pyglet.app.run()