import pyglet
from pyglet import *
from math import pi, sin, cos
from pyglet.window import key
import random
window = pyglet.window.Window()
key_handler = key.KeyStateHandler()

pyglet.gl.glClearColor(0.2, 0.4, 0.5, 1.0)
def createCircle(radius, x, y, verts):

    step = 2*pi/verts
    #Coordinates of vertices in the circle
    vertList = []
    #Chooses which vertice to draw
    index = []
    color =[]
    #Append center vertice
    vertList.append(x)
    vertList.append(y)
    for i in range(0, verts+1):
        #Groups vertices into triangles
        index.append(0); print 'lol'
        index.append(i); print 'hur'
        index.append(i+1)
        vertList.append(x + radius*cos(step*i))
        vertList.append(y + radius*sin(step*i))
    
    for i in range(0, verts+2):
        color.append(random.randint(0,255))
        color.append(random.randint(0,255))
        color.append(random.randint(0,255))

    return pyglet.graphics.vertex_list_indexed(verts+2, index, ('v2f',vertList), ('c3B', color))
circle = createCircle(100, window.width/2, window.height/2, 500)

#def createSquare(width, length, center):
    #s1 = (center - int(width / 2), center - int(length / 2))
    #s2 = (center + int(width / 2), center - int(length / 2))
    #s3 = (center - int(width / 2), center + int(length / 2))
    #s4 = (center + int(width / 2), center + int(length / 2))
@window.event
def on_draw():
    window.clear()
    circle.draw(pyglet.gl.GL_TRIANGLE_FAN)

if __name__ == '__main__':
    pyglet.app.run()