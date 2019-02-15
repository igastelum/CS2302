#IVAN GASTELUM
#COURSE 2302 DATA STRUCTURES
#INSTRUCTOR DR. OLAC FUENTES , TA: ANINDITA
#DATE LAST MODIFICATION 2/13/2019

import numpy as np
import matplotlib.pyplot as plt
import math 

def circle(center,rad):                 #Method to create a circle
    n = int(3*rad*math.pi)
    t = np.linspace(0,6.3,n)
    x = center[0]+rad*np.sin(t)
    y = center[1]+rad*np.cos(t)
    return x,y

def draw_circles(ax,n,center,radius):
    if n>0:
        center1 = [center[0]-(2/3)*radius,center[1]] #Defines the first center in x and y coordinates
        a,b = circle(center1,radius/(3))            #c and d will be defined as the two coordinates to create circle with first center defined
        ax.plot(a,b,color='k')
        draw_circles(ax,n-1,center1,radius/3)
        
        center2 = center                            #Second center will always share same center 
        c,d = circle(center2,radius/(3))            #c and d will be defined as the two coordinates to create circle with second center defined
        ax.plot(c,d,color='k')
        draw_circles(ax,n-1,center2,radius/3)
        
        center3 = [center[0]+(2/3)*radius,center[1]] #Third center will always share same center
        e,f = circle(center3,radius/(3))            #e and f will be defined as the two coordinates to create circle with third center defined
        ax.plot(e,f,color='k')
        draw_circles(ax,n-1,center3,radius/3)
        
        center4 = [center[0],center[1]+(2/3)*radius] #Fourth center will always share same center
        g,h = circle(center4,radius/(3))            #g and h will be defined as the two coordinates to create circle with fourth center defined
        ax.plot(g,h,color='k')
        draw_circles(ax,n-1,center4,radius/3)
        
        center5 = [center[0],center[1]-(2/3)*radius] #Fifth center will always share same center
        i,j = circle(center5,radius/(3))            #i and j will be defined as the two coordinates to create circle with third center defined
        ax.plot(i,j,color='k')
        draw_circles(ax,n-1,center5,radius/3)
        #center[0]=center[0]*w
        #draw_circles(ax,n-1,center,radius*w,w)
      
plt.close("all") 
fig, ax = plt.subplots() 
center = [100,0]
radius = 100
x,y = circle(center,radius)
ax.plot(x,y,color='k')
draw_circles(ax, 3, center, radius)
ax.set_aspect(1.0)
ax.axis('off')
plt.show()
fig.savefig('Recursive circles pattern.png')