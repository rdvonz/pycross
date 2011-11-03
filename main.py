import pyglet
from pyglet import gl, graphics
from math import pi, sin, cos

window = pyglet.window.Window()
def createCircle(radius, x, y, verts):
# x = cos(angle)
# y = sin(angle)
# number of sides is determined by dividing 2pi to number of steps

    step = 2*pi/verts
    #Coordinates of vertices in the circle
    vertList = []
    #Chooses which vertice to draw
    index = []
    #Append center vertice
    vertList.append(x)
    vertList.append(y)
    for i in range(0, verts):
        #Groups vertices into triangles
        index.append(0)
        index.append(i)
        index.append(i+1)
        vertList.append(x + radius*cos(step*i))
        vertList.append(y + radius*sin(step*i))

    #close the circle
    index.append(-1)
    index.append(0)
    index.append(1)
    return pyglet.graphics.vertex_list_indexed(verts+1, index, ('v2f',vertList))

@window.event
def on_draw():
    createCircle(200, window.width/2, window.height/2, 32).draw(pyglet.gl.GL_TRIANGLES)

if __name__ == '__main__':
    pyglet.app.run()