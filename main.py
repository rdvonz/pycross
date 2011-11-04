import pyglet
from game import primitives, mouse, resources

batch = pyglet.graphics.Batch()
window = pyglet.window.Window()
#pyglet.gl.glClearColor(0.2, 0.4, 0.5, 1.0)


cursor = window.set_mouse_cursor(pyglet.window.ImageMouseCursor(resources.cursor))
#circle = primitives.Circle(x=window.width / 2, y=window.height / 2,
#                           radius=50, verts=50, color=(255, 0, 0),
#                           batch=batch)

#square = primitives.Rectangle(color=(123, 132, 100), x=100, y=100, length=40,
#                              width=40, batch=batch)


def draw_grid(num_x, num_y, spacing, x, y, length, width):
    primitive_list = []
    #num_x * num_y gives us the total number of primitives
    for i in range(num_x):
            primitive_list.append(primitives.Rectangle(x=x + i * spacing, y=y,
                                 color=(255, 255, 255), length=length,
                                 width=width, batch=batch))
            for j in range(num_y):
                primitive_list.append(primitives.Rectangle(x=x + i * spacing,
                                                           y=y + j * spacing,
                                                           color=(255, 255, 255),
                                                           length=length,
                                                           width=width,
                                                           batch=batch))

    return primitive_list

grid = draw_grid(50, 50, 11, 0, 11*5, 10, 10)

@window.event
def on_draw():
    window.clear()
    batch.draw()
    mouse.MouseMovement()
#    window.set_mouse_cursor(cursor)


def on_mouse_motion(x, y, button, modifiers):
    pass


def update(dt):
    #This is probably not the correct way to do this)
    window.push_handlers(on_mouse_motion)


if __name__ == '__main__':
    pyglet.clock.schedule_interval(update, 1 / 120.0)
    pyglet.app.run()