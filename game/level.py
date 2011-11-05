# -*- coding: utf-8 -*-
"""
Created on Fri Nov  4 13:26:03 2011

@author: robert
"""
import pyglet
from pyglet.gl import GL_TRIANGLES
from itertools import groupby
from itertools import izip_longest


def grouper(n, iterable, fillvalue=None):
    "grouper(3, 'ABCDEFG', 'x') --> ABC DEF Gxx"
    args = [iter(iterable)] * n
    return izip_longest(*args, fillvalue=fillvalue)


class Level(object):

    def __init__(self, image):
        self.raw_image = image.get_image_data()

        self.pixels = list(grouper(
        3, self.raw_image.get_data(self.raw_image.format,
                                self.raw_image.pitch)))

        #These are, as of now, width and height of tiles
        self.width = 20
        self.length = 20
        self.x = 0
        self.y = 0

        #temp variable to see if drawing works
        self.count = -1

        self.rows = self.get_row()
        self.columns = self.get_column()
        
        self.row_numbers = self.get_numbers(self.rows)
        self.column_numbers = self.get_numbers(self.columns)

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

        self.vertex_list = batch.add_indexed(4, GL_TRIANGLES, group,
                                                 indices,
                                                 ('v2f', vertices),
                                                 ('c3B', color))

    def draw_grid(self, spacing, x, y, Batch):
        primitive_list = []
        self.x = x
        self.y = y
        self.black = 0

        #num_x * num_y gives us the total number of primitives
        for i in range(self.raw_image.height):
                primitive_list.append(self.rectangle(self.pixels[self.count],
                                                     batch=Batch))
                self.y = y + i * spacing

                for j in range(self.raw_image.width):
                    primitive_list.append(self.rectangle(self.pixels[self.count],
                                                         batch=Batch))
                    self.x = x + j * spacing
                    self.count += 1

    def get_row(self):
        return list(grouper(10, self.pixels))
    
    def get_column(self):
        column = []
        for cur_column in range(self.raw_image.width):
            cells = []
            for row in self.rows:
                cells.append(row[cur_column])
            column.append(cells)
        return column

    def get_numbers(self, cell_list):
        cell_numbers = []
        for cells in cell_list:
            cur_cells = []
            for k, g in groupby(cells):
                if 0 in k:
                    cur_cells.append(len(list(g)))
            cell_numbers.append(cur_cells)
        return cell_numbers






