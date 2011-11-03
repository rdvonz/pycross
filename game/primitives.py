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
        v0 = (x - int(width / 2), y + int(length / 2))
        v1 = (x - int(width / 2), y - int(length / 2))
        v2 = (x + int(width / 2), y + int(length / 2))
        v3 = (x + int(width / 2), y - int(length / 2))
        vertices = [v0[0], v0[1], v1[0], v1[1], v2[0], v2[1], v3[0], v3[1]]
        self.vertex_list = 
        