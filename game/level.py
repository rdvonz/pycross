# -*- coding: utf-8 -*-
"""
Created on Tue Nov  8 13:55:03 2011

@author: robert
"""
import pyglet
from pyglet.gl import *
from itertools import groupby
from itertools import izip_longest
import numpy

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
        self.image = pyglet.image.load(image)
        #Raw image data
        self.raw_image = self.image.get_image_data()
        self.rows = None
    def loadLevel(self):
        '''
        Takes a 16bit bmp image and generates an array
        to load the level data
        '''
        #Create a list of all the pixel data from the image
        img_data = list(self.raw_image.get_data('RGB', self.raw_image.width * 3))
        width = self.raw_image.width
        height = self.raw_image.height
        #Temp list to create an array
        cells = []
        for pixel in list(grouper(3, img_data)):
            print pixel
            if '\x00' in pixel or 0 in pixel:
                cells.append('X')
            else:
                cells.append(' ')
        #Create the grid
        grid = numpy.array(cells).reshape(width,height)
        
        print grid

lvl = Level('../resources/levels/tests/testgrid20.png')
lvl.loadLevel()
        