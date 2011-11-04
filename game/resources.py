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

cursor.anchor_y = 0
cursor.anchor_x = cursor.height