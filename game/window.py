# -*- coding: utf-8 -*-
"""
Created on Sun Nov  6 17:57:29 2011

@author: Robert Von Z
"""

#I've found that there are certain modules that need window attributes,
#so I'm instantiating it here for now.
import pyglet

window = pyglet.window.Window(width=800, height=600)
batch = pyglet.graphics.Batch()
grid = pyglet.graphics.Batch()