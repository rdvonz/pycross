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

    def __init__(self, batch, x=None, y=None, 
                 verts=None, radius=None, color=(), group=None):
        #List of points
        self.radius = radius
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
            vertices.append(x + self.radius*cos(step*i))
            vertices.append(y + self.radius*sin(step*i))
            
        colorIndex = []
        for i in range(0,verts+2):
            colorIndex.append(color[0])
            colorIndex.append(color[1])
            colorIndex.append(color[2])
        self.vertex_list = batch.add_indexed(verts+2, GL_TRIANGLES, 
                                             group, indices, 
                                             ('v2f', vertices),
                                             ('c3B', colorIndex))
        
    def velocity(self, velocity_x, velocity_y):
        for i in range(0,len(self.vertex_list.vertices)):
            if i%2==0:
                self.vertex_list.vertices[i]+=velocity_x
            else:
                self.vertex_list.vertices[i]+=velocity_y
        
class Rectangle(object):
    '''
    
    '''
    
    def __init__(self, batch, width=0, 
                 length=0, x=0, y=0, 
                 color=(), group=None):
        xone = x-(width/2)
        xtwo = x+(width/2)
        yone = y-(length/2)
        ytwo = y+(length/2)
        
        vertices = (xone, yone, xone, 
                    ytwo, xtwo, ytwo, xtwo, yone)
        
        indices = [0,1,2,0,2,3]
        colorIndex = []
        for i in range(0,4):
            colorIndex.append(color[0])
            colorIndex.append(color[1])
            colorIndex.append(color[2])
            
        self.vertex_list = batch.add_indexed(4, GL_TRIANGLES, group, indices, 
                                             ('v2f', vertices), 
                                             ('c3B', colorIndex))
        