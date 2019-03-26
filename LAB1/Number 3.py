#IVAN GASTELUM
#COURSE 2302 DATA STRUCTURES
#INSTRUCTOR DR. OLAC FUENTES , TA: ANINDITA
#DATE LAST MODIFICATION 2/13/2019

import numpy as np
import matplotlib.pyplot as plt
import math 

def Draw_Tree(ax,p,n,w,t):
    if n>0:
        p[0,0] = p[1,0] - w     #fisrt point goes to the left direction 
        p[0,1] = p[1,1] - t     #first point goes down in y direction
        p[2,0] = p[1,0] + w     #second point goes to the right direction
        p[2,1] = p[1,1] - t     #second point goes down in y direction
        ax.plot(p[:,0],p[:,1],color='k')
        q = np.array([[0,0],[p[0,0],p[0,1]],[0,0]])
        r = np.array([[0,0],[p[2,0],p[2,1]],[0,0]])
        #Recursive call with n - 1 , the width to be half of the last call
        Draw_Tree(ax,q,n-1,w/2,t)
        Draw_Tree(ax,r,n-1,w/2,t)

plt.close("all")
origin = np.array([[0,0],[0,0],[0,0]]) #Origin will have the three points needed to create one branch of two roots
n=3         #Number of recursive calls
w=50        #the width of the graph in the x cooridnate
t=200/n     #the length of the graph in the y coordinate
fig, ax = plt.subplots() 
Draw_Tree(ax,origin,n,w,t)
ax.set_aspect(1.0)
ax.axis('off')
plt.show()
fig.savefig('Recursive Tree.png')
 