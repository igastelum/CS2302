#IVAN GASTELUM
#COURSE 2302 DATA STRUCTURES
#INSTRUCTOR DR. OLAC FUENTES , TA: ANINDITA
#DATE LAST MODIFICATION 2/13/2019

import numpy as np
import matplotlib.pyplot as plt
import math 

def circle(center,rad):     #Method to obtain center (x,y) and the radius
    n = int(3*rad*math.pi)
    t = np.linspace(0,6.3,n)
    x = center[0]+rad*np.sin(t)
    y = center[1]+rad*np.cos(t)
    return x,y

def draw_circles(ax,n,center,radius,w):
    if n>0:
        x,y = circle(center,radius)
        ax.plot(x,y,color='k')
        center[0]=center[0]*w   #changes the center to a smaller range from 0 to the fist assigned radius
        draw_circles(ax,n-1,center,radius*w,w)
      
plt.close("all") 
fig, ax = plt.subplots() 
draw_circles(ax, 500, [100,0], 100,.95)
ax.set_aspect(1.0)
ax.axis('off')
plt.show()
fig.savefig('Recursive centre.png')