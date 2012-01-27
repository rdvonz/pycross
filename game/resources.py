# -*- coding: utf-8 -*-
"""
Created on Thu Nov  3 22:03:33 2011

@author: Robert Von Z
"""

import pyglet

img = pyglet.resource

img.path = ['resources/']

img.reindex()
cursor = img.image('pencil.png')
tile = img.image('tile.png')
clicked = img.image('clicked.png')
marked = img.image('marked_x.png')
gutter = img.image('gutter.png')
img.add_font('8bitwonder.TTF')

def center(image):
    image.anchor_y = image.height/2
    image.anchor_x = image.width/2

center(cursor)
center(gutter)
center(tile)

center(clicked)
center(marked)