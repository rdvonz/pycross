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
        self.x = 40
        self.y = 40
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
        self.x = 0
        self.y = 0
        print self.pixels
        
        #Grid Centering variables
        self.total_width = (self.raw_image.width * self.width) + (self.spacing * self.raw_image.width -1)
        self.total_height = (self.raw_image.height * self.height) + (self.spacing * self.raw_image.height -1)

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
        
    def draw_picross(self):
        x = 50
        y = 50
        self.cell_list = []
        count = 0
        for i in range(self.raw_image.width):
            y+=21
            x=50
            for j in range(self.raw_image.height):
                print self.pixels[count],'\n'
                self.cell_list.append(Cell(20,20,x,y,self.pixels[count]))
                x+=21
                count+=1
        print self.raw_image.width*self.raw_image.height

class Cell(object):

    def __init__(self, width, height, x, y, tile, group=None):
        '''
        Constructs a rectangle
        mainly made to solve the need for an is_tile value
        '''
        self.x = x
        self.y = y
        self.tile = tile
        self.width = width
        self.height = height        
        self.is_tile = self.check_tile()
        self.is_clicked = False

        xone = x - (self.width / 2)
        xtwo = x + (self.width / 2)
        yone = y - (self.width / 2)
        ytwo = y + (self.width / 2)
        vertices = (xone, yone, xone,
                    ytwo, xtwo, ytwo, xtwo, yone)

        indices = [0, 1, 2, 0, 2, 3]

        self.vertex_list = window.batch.add_indexed(4, GL_TRIANGLES, group,
                                                 indices,
                                                 ('v2f', vertices),
                                                 ('c3B', [255,255,255]*4))
    def check_tile(self):
        if 0 in self.tile:
            return True
        else:
            return False