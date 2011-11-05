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

        self.pixels = list(self.grouper(3, self.raw_image.get_data(self.raw_image.format,
                                self.raw_image.pitch)))

    def grouper(self, n, iterable, fillvalue=None):
        "grouper(3, 'ABCDEFG', 'x') --> ABC DEF Gxx"
        args = [iter(iterable)] * n
        return itertools.izip_longest(*args, fillvalue=fillvalue)


level = CreateLevel(pyglet.image.load('../resources/levels/lv1.bmp'))
print level.pixels