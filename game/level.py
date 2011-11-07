# -*- coding: utf-8 -*-
"""
Created on Fri Nov  4 13:26:03 2011

@author: robert
"""
import pyglet
import window
from pyglet.gl import GL_TRIANGLES
from itertools import groupby
from itertools import izip_longest


def grouper(n, iterable, fillvalue=None):
    "grouper(3, 'ABCDEFG', 'x') --> ABC DEF Gxx"
    args = [iter(iterable)] * n
    return izip_longest(*args, fillvalue=fillvalue)


class Level(object):

    def __init__(self, image):
        '''
        Constructor currently provides:
        Ability to load a level image
        width and height of the cells
        data for rows and columns
        column and row numbers to solve the picross
        '''
        #Get pixel data from the level image
        self.raw_image = image.get_image_data()

        self.pixels = list(grouper(
        3, self.raw_image.get_data(self.raw_image.format,
                                self.raw_image.pitch)))
        self.spacing = 1

        #Holds the data for each row and each column

        self.rows = self.get_row()
        self.columns = self.get_column()

        self.row_numbers = self.get_numbers(self.rows)
        self.column_numbers = self.get_numbers(self.columns)
        
        
        print 'ROW:', self.row_numbers
        print 'COLUMN', self.column_numbers
        self.cell_list = []
        
        #Tile specific variables
        self.width = 20
        self.height = 20
        self.spacing = 1
        
        #Grid Centering variables
        self.total_width = (self.raw_image.width * self.width) + (self.spacing * self.raw_image.width -1)
        self.total_height = (self.raw_image.height * self.height) + (self.spacing * self.raw_image.height -1)
        
    def draw_picross(self):
        '''
        Really messy, as a result of making a cell it's own class.
        Reasoning: To get boolean values on whether you solve it there.
        '''
        #total width is the height of the tile * (# tiles + spacing)
        #For some reason it's off by one tile. Which is why I'm subtracting 21

        #Stores every cell object, this will be used for game logic later on
        self.cell_list = []

        count = 0

        #height of Tile * height of tile = total tiles
        center_x = (window.window.width - self.total_width) / 2
        center_y = (window.window.height - self.total_height) / 2

        for i in range(self.raw_image.width):
            y = center_y + (self.height + self.spacing) * i
            x = center_x

            for j in range(self.raw_image.height):
                x = center_x + (self.width + self.spacing) * j

                if 0 == self.pixels[count][0]:
                    is_tile = True
                else:
                    is_tile = False

                self.cell_list.append(Cell(self.width, self.height, x, y,  is_tile))
                count += 1

    def get_row(self):
        '''
        Splits image into rows
        (Useful for getting picross numbers)
        '''
        return list(grouper(self.raw_image.width, self.pixels))

    def get_column(self):
        '''
        Splits images into columns
        (useful for picross numbers)
        '''
        column = []
        for cur_column in range(self.raw_image.width):
            cells = []
            for row in self.rows:
                cells.append(row[cur_column])
            column.append(cells)

        return column

    def get_numbers(self, cell_list):
        '''
        Gets the number values for solving a picross
        '''
        cell_numbers = []
        for cells in cell_list:
            cur_cells = []
            for k, g in groupby(cells):
                if 0 in k:
                    cur_cells.append(len(list(g)))
            cell_numbers.append(cur_cells)
        return cell_numbers
    
class Cell(object):

    def __init__(self, width, height, x, y, is_tile, group=None):
        '''
        Constructs a rectangle
        mainly made to solve the need for an is_tile value
        '''
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.is_tile = is_tile
        self.is_clicked = False

        xone = x - (self.width / 2)
        xtwo = x + (self.width / 2)
        yone = y - (self.width / 2)
        ytwo = y + (self.width / 2)
        pixel_color = [255, 255, 255]
        color = []

        for i in range(4):
            color.append(pixel_color[0])
            color.append(pixel_color[1])
            color.append(pixel_color[2])

        vertices = (xone, yone, xone,
                    ytwo, xtwo, ytwo, xtwo, yone)

        indices = [0, 1, 2, 0, 2, 3]

        self.vertex_list = window.batch.add_indexed(4, GL_TRIANGLES, group,
                                                 indices,
                                                 ('v2f', vertices),
                                                 ('c3B', color))