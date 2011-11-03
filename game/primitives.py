'''
Created on Nov 2, 2011

@author: robert
'''
import pyglet
from pyglet.gl import *
from math import sin, cos, pi

class Circle(object):
    '''
    Draws a beautiful circle
    '''

    def __init__(self, x, y, verts, radius, batch, group=None):
        #List of points
        vertices = []
        
        #Order points are drawn
        indices = []
        
        #Distribution of points
        step = 2*pi/verts
        
        #Center point
        vertices.append(x)
        vertices.append(y)
    
        for i in range(0, verts+1):
            
            #Groups vertices into triangles
            indices.append(0)
            indices.append(i)
            indices.append(i+1)
            
            #calculate points of circle
            vertices.append(x + radius*cos(step*i))
            vertices.append(y + radius*sin(step*i))
            
        
        self.vertex_list = batch.add_indexed(verts+2, GL_TRIANGLES, group, indices, ('v2f', vertices))

class Rectangle(object):
    '''
    
    '''
    
    def __init__(self, width, length, x, y, batch, group=None):
        xone = x-(width/2)
        xtwo = x+(width/2)
        yone = y-(length/2)
        ytwo = y+(length/2)
        vertices = (xone, yone, xone, ytwo, xtwo, ytwo, xtwo, yone)
        indices = [0,1,2,0,2,3]
        self.vertex_list = batch.add_indexed(4, GL_TRIANGLES, group, indices, ('v2f', vertices))
        