import pyglet
from game import primitives, resources, level, window
pyglet.gl.glClearColor(0.2, 0.4, 0.5, 1.0)

mouse = pyglet.window.ImageMouseCursor(resources.cursor)
cursor = window.window.set_mouse_cursor(mouse)

lvl = level.Level(pyglet.image.load('resources/levels/lv2.bmp'))

lvl.draw_picross()

@window.window.event
def on_draw():
    window.window.clear()
    window.batch.draw()
    window.window.set_mouse_cursor(cursor)


def on_mouse_motion(x, y, button, modifiers):
    pass


def update(dt):
    #This is probably not the correct way to do this)
    window.window.push_handlers(on_mouse_motion)


if __name__ == '__main__':
    pyglet.clock.schedule_interval(update, 1 / 120.0)
    pyglet.app.run()