# -*- coding: utf-8 -*-
"""
Created on Fri Nov  4 13:26:03 2011

@author: robert
"""
import pyglet
import itertools
class CreateLevel(object):
    def __init__(self, image):
        self.raw_image = image.get_image_data()
        
    def grouper:
    def pixels:
        

level = CreateLevel(pyglet.image.load('../resources/levels/lv1.bmp'))
format = level.raw_image.format
pitch = level.raw_image.pitch
pixels =  level.raw_image.get_data(format, pitch)
pix = []

def grouper(n, iterable, fillvalue=None):
    "grouper(3, 'ABCDEFG', 'x') --> ABC DEF Gxx"
    args = [iter(iterable)] * n
    return itertools.izip_longest(*args, fillvalue=fillvalue)

