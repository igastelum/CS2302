#IVAN GASTELUM
#COURSE 2302 DATA STRUCTURES
#INSTRUCTOR DR. OLAC FUENTES , TA: ANINDITA
#DATE LAST MODIFICATION 3/11/2019

import numpy as np
import matplotlib.pyplot as plt
import math 

#NUMBER 1: GRAPHING BST with all nodes after inserting
class BST(object):
    # Constructor
    def __init__(self, item, left=None, right=None):  
        self.item = item
        self.left = left 
        self.right = right      

#Inserting method will be the only method to use for this 
def Insert(T,newItem):
    if T == None:
        T =  BST(newItem)
    elif T.item > newItem:
        T.left = Insert(T.left,newItem)
    else:
        T.right = Insert(T.right,newItem)
    return T

#Recursive method to plot lines and Tree values 
def Draw_Tree(ax,p,n,w,t,T):
    if T is not None:        
        if T.left is not None:
            p[0,0] = p[1,0] - w     #fisrt point goes to the left direction 
            p[0,1] = p[1,1] - t     #first point goes down in y direction
            p[2,0] = p[1,0]      #second point goes to the right direction
            p[2,1] = p[1,1]       #second point goes down in y direction
            ax.plot(p[:,0],p[:,1],color='k')
            plt.text(p[1,0] - w,p[1,1] - t, T.left.item, bbox={"boxstyle":"circle","color":"grey"})
            q = np.array([[0,0],[p[0,0],p[0,1]],[0,0]])
            r = np.array([[0,0],[p[2,0],p[2,1]],[0,0]])
            Draw_Tree(ax,q,n-1,w/2,t,T.left)
        
        if T.right is not None:
            p[0,0] = p[1,0]        #fisrt point goes to the left direction 
            p[0,1] = p[1,1]        #first point goes down in y direction
            p[2,0] = p[1,0] + w    #second point goes to the right direction
            p[2,1] = p[1,1] - t    #second point goes down in y direction
            ax.plot(p[:,0],p[:,1],color='k')
            plt.text(p[1,0] + w,p[1,1] - t, T.right.item, bbox={"boxstyle":"circle","color":"grey"})
            q = np.array([[0,0],[p[0,0],p[0,1]],[0,0]])
            r = np.array([[0,0],[p[2,0],p[2,1]],[0,0]])
            Draw_Tree(ax,r,n-1,w/2,t,T.right)
            
#Declaring Tree and inserting values in same order as in sheet from lab 3 
T = None
A = [10,4,15,2,8,12,18,1,3,5,9,7]
#Search_Iterative(T,key)

for a in A:
    T = Insert(T,a)


plt.close("all")
origin = np.array([[0,0],[0,0],[0,0]]) #Origin will have the three points needed to create one branch of two roots
n=3         #Number of recursive calls
w=100       #the width of the graph in the x cooridnate
t=200/n     #the length of the graph in the y coordinate
fig, ax = plt.subplots() 
plt.text(origin[0,0],origin[1,1], T.item, bbox={"boxstyle":"circle","color":"grey"})
Draw_Tree(ax,origin,n,w,t,T)
ax.set_aspect(1.0)
ax.axis('off')
plt.show()
fig.savefig('BST Tree.png')