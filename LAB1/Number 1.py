#IVAN GASTELUM
#COURSE 2302 DATA STRUCTURES
#INSTRUCTOR DR. OLAC FUENTES , TA: ANINDITA
#DATE LAST MODIFICATION 2/13/2019

import numpy as np
import matplotlib.pyplot as plt #Import in order to plot
import math 

def Find_center1(c,r):      #This method finds the first center
    x = c[0] + r
    y = c[1] + r
    return np.array([x,y])

def Find_center2(c,r):      #This method finds the second center
    x = c[0] - r
    y = c[1] + r
    return np.array([x,y])

def Find_center3(c,r):      #This method finds the third center
    x = c[0] - r
    y = c[1] - r
    return np.array([x,y])

def Find_center4(c,r):      #This method finds the fourth center
    x = c[0] + r
    y = c[1] - r
    return np.array([x,y])
    

def Define_points(c,r):
    point1 = [c[0]-r,c[1]-r]    #c0 refers to x cordinate and c1 to y coord 
    point2 = [c[0]+r,c[1]-r]    #r is passing the radius (length of square/2)
    point3 = [c[0]+r,c[1]+r]    #point1 to point4 define the four corners
    point4 = [c[0]-r,c[1]+r]
    point5 = [c[0]-r,c[1]-r]
    return point1,point2,point3,point4,point5

def cuadrados(ax,n,p,rad,center):
    if n>0:
        #The new rad is set to be half of the last taken radius
        #center1, center2,center3,center4 will have new x,y coordinates
        #p,q,r,w will receive new fours points
        # by taking reference the first center
        #once centers and arrays with points are set, recursive call begins
        center1 = Find_center1(center,rad)
        new_rad = rad/2         
        p = np.array(Define_points(center1,new_rad)) 
        ax.plot(p[:,0],p[:,1],color='k')            
        cuadrados(ax,n-1,p,new_rad,center1)
        
        center2 = Find_center2(center,rad)
        q = np.array(Define_points(center2,new_rad))
        ax.plot(q[:,0],q[:,1],color='k')
        cuadrados(ax,n-1,p,new_rad,center2)
        
        center3 = Find_center3(center,rad)
        r = np.array(Define_points(center3,new_rad))
        ax.plot(r[:,0],r[:,1],color='k')
        cuadrados(ax,n-1,p,new_rad,center3)
        
        center4 = Find_center4(center,rad)
        w = np.array(Define_points(center4,new_rad))
        ax.plot(w[:,0],w[:,1],color='k')
        cuadrados(ax,n-1,p,new_rad,center4)
        
plt.close("all")
rad = 800
x=0
center = [0,0]
p = np.array([[-rad,-rad],[rad,-rad],[rad,rad],[-rad,rad],[-rad,-rad]])
fig, ax = plt.subplots()
ax.plot(p[:,0],p[:,1],color='k')
cuadrados(ax,4,p,rad,center)
ax.set_aspect(1.0)
ax.axis('off')
plt.show()
fig.savefig('Recursive Squares.png')
