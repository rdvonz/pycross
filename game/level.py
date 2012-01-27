# -*- coding: utf-8 -*-
"""
Created on Tue Nov  8 13:55:03 2011

@author: robert
"""
import pyglet
from pyglet.gl import *
from itertools import groupby
from itertools import izip_longest
from numpy import array
import window
import resources


def grouper(n, iterable, fillvalue=None):
    '''
    Taken from the python recipe in the itertools documentation
    '''
    args = [iter(iterable)] * n
    return izip_longest(*args, fillvalue=fillvalue)


class Level(object):
    def __init__(self, image):
        '''
        Constructor
        '''
        #Raw image data
        self.raw_image = image.get_image_data()

        #Simplifying variables
        self.width = self.raw_image.width
        self.height = self.raw_image.height

        #Game board
        self.grid = self.get_grid()
        self.column_grid = self.get_column(self.grid)
        self.row_numbers = self.get_numbers(self.grid)
        self.column_numbers = self.get_numbers(self.column_grid) 

        #Some default parameters of the tiles DEPRECATED:
        self.tile_width = 20
        self.tile_height = 20

        #Spacing is the width or height + 1 (assuming a square)
        self.tile_spacing = self.tile_width + 1
        self.total_width = self.tile_spacing * self.width
        self.total_height = self.tile_spacing * self.height

        #Variables used for the grid
        self.offset_x = 50
        self.offset_y = -50
        self.pos_x = (window.window.width - self.total_width +
        self.tile_width / 2 + (self.tile_spacing - self.tile_width)) - self.offset_x
        self.pos_y = (self.tile_height / 2) - self.offset_y

    def get_grid(self):
        '''
        Takes a 16bit bmp image and generates an array
        to load the level data
        '''

        #Create a list of all the pixel data from the image
        img_data = list(self.raw_image.get_data('RGB', self.width * 3))

        #Temp list to create an array
        tiles = []
        for pixel in list(grouper(3, img_data)):
            if '\x00' in pixel or 0 in pixel:
                tiles.append(1)
            else:
                tiles.append(0)

        #Create the grid
        grid = array(tiles).reshape(self.width, self.height)
        return grid

    def draw_grid(self):
        '''
        Creates a matrix of tiles that can be drawn on the screen
        '''

        #Variables to place the picross grid

        tile_list = []

        y = self.pos_y
        for tiles in self.grid:

            x = self.pos_x
            for tile in tiles:
                tile_list.append(Tile_Sprite(tile, x, y, batch=window.batch))

                x += self.tile_spacing
            y += self.tile_spacing
        return tile_list

    def draw_column_numbers(self):
        y = self.pos_y - 5
        for numbers in self.row_numbers:
            x = self.pos_x - 20
            for number in numbers:
                pyglet.text.Label(str(number),
                                  x=x,
                                  y=y,
                                  font_size=10,
                                  color=(0, 0, 0, 255),
                                  batch=window.batch)
                x -= 10
            y += self.tile_spacing
    
    def draw_row_numbers(self):
        x = self.pos_x - 10
        for numbers in self.column_numbers:
            y = self.pos_y + self.total_height
            
            for number in numbers:
                print number
                pyglet.text.Label(str(number),
                                  x=x,
                                  y=y,
                                  font_size=10,
                                  color=(0, 0, 0, 255),
                                  batch = window.batch)
                y += 15
            x += self.tile_spacing                    

    def get_column(self, grid):
        '''
        Gets image data in column format
        Useful for getting column numbers of a
        picross
        '''
        column = []
        for cur_column in range(self.width):
            tiles = []
            for row in grid:
                tiles.append(row[cur_column])
            column.append(tiles)
        column = array(column).reshape(self.width, self.height)
        return column

    def get_numbers(self, grid):
        '''
        Gets number values for solving the picross
        '''
        numbers = []
        for tiles in grid:
            cur_row = []
            if sum(tiles) == 0:
                cur_row.append(0)
            for k, g in groupby(tiles):
                if k:
                    cur_row.append(len(list(g)))
            numbers.append(cur_row)
        return numbers


class Tile(object):

    def __init__(self, width, height, x, y, is_tile, group = None):

        #Width attribute is a must to get mouse detection
        self.width = width
        self.height = height

        #Position of the tile
        self.x = x
        self.y = y

        #Some boolean values to check stuff:
        self.is_tile = is_tile
        self.is_clicked = 0
        self.is_marked = False

        #This will be used later (maybe) for colorful picrosses
        #It's currently white.
        self.base_color = [255, 255, 255]

        #Vertices of Tile
        xone = x - (self.width / 2)
        xtwo = x + (self.width / 2)
        yone = y - (self.width / 2)
        ytwo = y + (self.width / 2)
        vertices = (xone, yone, xone,
                    ytwo, xtwo, ytwo, xtwo, yone)

        #Order of vertices
        indices = [0, 1, 2, 0, 2, 3]

        self.vertex_list = window.batch.add_indexed(4, GL_TRIANGLES, group,
                                                 indices,
                                                 ('v2f', vertices),
                                                 ('c3B', self.base_color * 4))
                                                 
class Tile_Sprite(pyglet.sprite.Sprite):
    def __init__(self, is_tile, x, y, batch=None):
        super(Tile_Sprite, self).__init__(img = resources.tile, x = x, y = y, batch=batch)
        self.is_tile = is_tile
        self.is_clicked = 0
        self.is_marked = 0
    def change_image(self, state):
        if state == 'clicked':
            self.image = resources.clicked
        elif state == 'marked':
            self.image = resources.marked
        elif state == 'normal':
                self.image = resources.tile

class Numbers(pyglet.text.Label):
    '''
    Draws numbers and rows for solving a picross
    '''
    def __init__(self, column_numbers, row_numbers, *args, **kwargs):
        Super().__init__(text, x, y, width, height)

