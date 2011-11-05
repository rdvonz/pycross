# -*- coding: utf-8 -*-
"""
Created on Fri Nov  4 13:26:03 2011

@author: robert
"""
import pyglet
from pyglet.gl import GL_TRIANGLES
import itertools


class CreateLevel(object):

    def __init__(self, image):
        self.raw_image = image.get_image_data()

        self.pixels = list(self.grouper(
        3, self.raw_image.get_data(self.raw_image.format,
                                self.raw_image.pitch)))

        #These are, as of now, width and height of tiles
        self.width = 20
        self.length = 20
        self.x = 0
        self.y = 0

        #temp variable to see if drawing works
        self.count = 0

    def grouper(self, n, iterable, fillvalue=None):
        "grouper(3, 'ABCDEFG', 'x') --> ABC DEF Gxx"
        args = [iter(iterable)] * n
        return itertools.izip_longest(*args, fillvalue=fillvalue)

    def rectangle(self, pixel_color, batch, group=None):
        xone = self.x - (self.width / 2)
        xtwo = self.x + (self.width / 2)
        yone = self.y - (self.length / 2)
        ytwo = self.y + (self.length / 2)
        color = []
        for i in range(4):
            color.append(pixel_color[0])
            color.append(pixel_color[1])
            color.append(pixel_color[2])
            
            

        vertices = (xone, yone, xone,
                    ytwo, xtwo, ytwo, xtwo, yone)

        indices = [0, 1, 2, 0, 2, 3]
        colorIndex = []

        self.vertex_list = batch.add_indexed(4, GL_TRIANGLES, group,
                                                 indices,
                                                 ('v2f', vertices),
                                                 ('c3B', color))

    def draw_grid(self, spacing, x, y, Batch):
        primitive_list = []
        self.x = x
        self.y = y
        #num_x * num_y gives us the total number of primitives
        for i in range(self.raw_image.width):
                primitive_list.append(self.rectangle(self.pixels[self.count],
                                                     batch=Batch))
                self.x = x + i * spacing
                
                for j in range(self.raw_image.height):
                    primitive_list.append(self.rectangle(self.pixels[self.count],
                                                         batch=Batch))
                    self.y = y + j * spacing
                    self.count+=1