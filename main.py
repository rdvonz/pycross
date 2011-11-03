import pyglet
from pyglet import *
from math import pi, sin, cos
from game import primitives
from pyglet.gl import *

batch = pyglet.graphics.Batch()
window = pyglet.window.Window()
pyglet.gl.glClearColor(0.2, 0.4, 0.5, 1.0)

circle = primitives.Circle(window.width/2, window.height/2, 50, 200, batch=batch)
   
@window.event
def on_draw():
    window.clear()
    batch.draw()

if __name__ == '__main__':
    pyglet.app.run()