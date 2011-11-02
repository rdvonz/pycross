import pyglet
from pyglet import gl, graphics
from math import pi, sin, cos

window = pyglet.window.Window()
def createCircle(radius, center, verts):
#    x = cos(angle)
#    y = sin(angle)
#    number of side is determined from number of steps from 0 to 2*pi
    step =  2*pi/verts
    vertList = []
    for i in range(0, verts):
        vertList.append(center[0] + radius*cos(step*i))
        vertList.append(center[1] + radius*sin(step*i))
    circle = pyglet.graphics.vertex_list(verts, ('v2f',vertList))
    return circle
@window.event
def on_draw():                      
    for i in range(0,20):
        createCircle(i*20, (window.width/2, window.height/2), 250).draw(pyglet.gl.GL_POINTS)


if __name__ == '__main__':
    pyglet.app.run()