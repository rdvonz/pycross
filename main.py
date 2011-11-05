import pyglet
from game import primitives, resources, level

batch = pyglet.graphics.Batch()
window = pyglet.window.Window()

pyglet.gl.glClearColor(0.2, 0.4, 0.5, 1.0)

mouse = pyglet.window.ImageMouseCursor(resources.cursor)
#cursor = window.set_mouse_cursor(mouse)

der = level.CreateLevel(pyglet.image.load('resources/levels/lv2.bmp'))

der.draw_grid(21, 200, 200, batch)


@window.event
def on_draw():
    window.clear()
    batch.draw()
#    window.set_mouse_cursor(cursor)


def on_mouse_motion(x, y, button, modifiers):
    pass


def update(dt):
    #This is probably not the correct way to do this)
    window.push_handlers(on_mouse_motion)


if __name__ == '__main__':
    pyglet.clock.schedule_interval(update, 1 / 120.0)
    pyglet.app.run()