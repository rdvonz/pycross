import pyglet
from game import primitives

batch = pyglet.graphics.Batch()
window = pyglet.window.Window()
pyglet.gl.glClearColor(0.2, 0.4, 0.5, 1.0)

circle = primitives.Circle(x=window.width/2, 
                           y=window.height/2, 
                           radius=50, 
                           verts=50,
                           color=(255,0,0),
                           batch=batch)
square = primitives.Rectangle(color=(123, 132, 100), x=100, y=100, length=40, width=40, batch=batch)
@window.event
def on_draw():
    window.clear()
    batch.draw()

def update(dt):
    #This is probably not the correct way to do this
    for i in range(0,len(circle.vertex_list.vertices)):
        if i%2==0:
            circle.vertex_list.vertices[i]+=1
    batch.draw()
    

if __name__ == '__main__':
    pyglet.clock.schedule_interval(update, 1/120.0)
    pyglet.app.run()