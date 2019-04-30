#IVAN GASTELUM
#LABORATORY #7 MAZE SOLUTION
#COURSE 2302 DATA STRUCTURES
#INSTRUCTOR DR. OLAC FUENTES , TA: ANINDITA
#DATE LAST MODIFICATION 4/29/2019

import matplotlib.pyplot as plt
import numpy as np
import datetime
import random
import queue

#Method that draws the maze with walls array 
def draw_maze(walls,maze_rows,maze_cols,cell_nums=False):
    fig, ax = plt.subplots()
    for w in walls:
        if w[1]-w[0] ==1: #vertical wall
            x0 = (w[1]%maze_cols)
            x1 = x0
            y0 = (w[1]//maze_cols)
            y1 = y0+1
        else:#horizontal wall
            x0 = (w[0]%maze_cols)
            x1 = x0+1
            y0 = (w[1]//maze_cols)
            y1 = y0  
        ax.plot([x0,x1],[y0,y1],linewidth=1,color='k')
    sx = maze_cols
    sy = maze_rows
    ax.plot([0,0,sx,sx,0],[0,sy,sy,0,0],linewidth=2,color='k')
    if cell_nums:
        for r in range(maze_rows):
            for c in range(maze_cols):
                cell = c + r*maze_cols   
                ax.text((c+.5),(r+.5), str(cell), size=10,
                        ha="center", va="center")
    ax.axis('off') 
    ax.set_aspect(1.0)

#Returns a list containing the sets encoded in S
def dsfToSetList(S):
    #Returns aa list containing the sets encoded in S
    sets = [ [] for i in range(len(S)) ]
    for i in range(len(S)):
        sets[find(S,i)].append(i)
    sets = [x for x in sets if x != []]
    return sets

#Creates a np array of -1, referring as all numbers to be roots
def DisjointSetForest(size):
    return np.zeros(size,dtype=np.int)-1    

def find(S,i):
    # Returns root of tree that i belongs to
    if S[i]<0:
        return i
    return find(S,S[i])

def find_c(S,i): #Find with path compression 
    if S[i]<0: 
        return i
    r = find_c(S,S[i]) 
    S[i] = r 
    return r

def union_c(S,i,j):
    # Joins i's tree and j's tree, if they are different
    # Uses path compression
    ri = find_c(S,i) 
    rj = find_c(S,j)
    if ri!=rj:
        S[rj] = ri
         
def union_by_size(S,i,j):
    # if i is a root, S[i] = -number of elements in tree (set)
    # Makes root of smaller tree point to root of larger tree 
    # Uses path compression
    ri = find_c(S,i) 
    rj = find_c(S,j)
    if ri!=rj:
        if S[ri]>S[rj]: # j's tree is larger
            S[rj] += S[ri]
            S[ri] = rj
        else:
            S[ri] += S[rj]
            S[rj] = ri

def union(S,i,j):
    # Joins i's tree and j's tree, if they are different
    ri = find(S,i) 
    rj = find(S,j)
    if ri!=rj:
        S[rj] = ri

def breadthFirst_Search(G,v,y):
    visited = np.full(len(G),False,dtype=bool)
    prev = np.zeros(len(G),dtype=np.int)-1
    Q = queue.Queue()
    Q.put(v)
    visited[v] = True
    while not Q.empty():
        u = Q.get()
        #print(u, end=' ')
        for t in G[u]:
            if visited[t]==False:
                visited[t] = True
                prev[t] = u
                Q.put(t)
        if t==y:
            #print(t, end=' ')
            print('Goal reached')
            print()
    return prev

def depthFirst_Search(G,v,y):
    visited = np.full(len(G),False,dtype=bool)
    prev = np.zeros(len(G),dtype=np.int)-1
    S = []
    S.append(v)
    visited[v] = True
    while S:
        u = S.pop(-1)
        #print(u, end=' ')
        for t in G[u]:
            if visited[t]==False:
                visited[t] = True
                prev[t] = u
                S.append(t)
        if t==y:
            #print(t, end=' ')
            print('Goal reached')
            print()
    return prev

def depthFirst_Recursive(G,source):
    global VISITED
    global PREV
    VISITED[source] = True
    for t in G[source]:
        if VISITED[t]==False:
            PREV[t] = source
            depthFirst_Recursive(G,t)

def adj_list(r,c,walls):
    vertices = r * c
    G = [[] for i in range(vertices)]
    w = wall_list(r,c)
    for i in w:
        if i not in walls:
            G[i[0]].append(i[1])
            G[i[1]].append(i[0])
    return G
                        

def wall_list(maze_rows, maze_cols):
    # Creates a list with all the walls in the maze
    w =[]
    for r in range(maze_rows):
        for c in range(maze_cols):
            cell = c + r*maze_cols
            if c!=maze_cols-1:
                w.append([cell,cell+1])
            if r!=maze_rows-1:
                w.append([cell,cell+maze_cols])
    return w

plt.close("all") 
maze_rows = 10
maze_cols = 15
n = maze_rows * maze_cols

walls = wall_list(maze_rows,maze_cols)

#draw_maze(walls,maze_rows,maze_cols,cell_nums=True) 

#Program begins HERE: creates a disjoint set forest and a list of lists with separated sets
S = DisjointSetForest(150)
dsf = dsfToSetList(S)

#Choose the option by which you want to create the maze
print('Choose one of the three ways of generating a maze')
print('1: By Selecting number of walls removed')
print('2: Creating a Standard Maze')
choice = int(input('Choice: '))

#Choice 1 creates the maze with standard union
if choice==1:
    m = int(input('Type the number of walls to remove: '))
    start = datetime.datetime.now()
    temp = m
    while len(dsf)>1 and temp!=0:
        d = random.randint(0,len(walls)-1)
        wall = walls[d]
        c1 = wall[0]
        c2 = wall[1]
        print(c1,c2)
        
        f1 = find(S,c1)
        f2 = find(S,c2)
        if f1 != f2:
            walls.pop(d)
            temp = temp-1
            union(S,c1,c2)
            dsf = dsfToSetList(S)
            #draw_maze(walls,maze_rows,maze_cols) 
        print(dsf)
    
    if temp!=0:
        while temp!=0:
            d = random.randint(0,len(walls)-1)
            walls.pop(d)
            temp = temp-1
           
    end = datetime.datetime.now()
    delta = end - start
    if m<n-1:
        print(' A path from source to destination is not guaranteed to exist (when m < n − 1)')
    elif m>n-1:
        print('There is at least one path from source to destination (when m > n − 1)')
    else:
        print('The is a unique path from source to destination (when m = n − 1)')
    
    print()
    print('Time elapsed to generate the maze:',delta.total_seconds()*1000)

#Choice 1 creates the maze with union by size
if choice==2:
    start = datetime.datetime.now()
    m=0
    while len(dsf)>1:
        d = random.randint(0,len(walls)-1)
        wall = walls[d]
        c1 = wall[0]
        c2 = wall[1]
        print(c1,c2)
        
        f1 = find(S,c1)
        f2 = find(S,c2)
        if f1 != f2:
            walls.pop(d)
            m+=1
            union_by_size(S,c1,c2)
            dsf = dsfToSetList(S)
            #draw_maze(walls,maze_rows,maze_cols) 
        print(dsf)
           
    end = datetime.datetime.now()
    delta = end - start
    print()
    print('Number of walls removed, m = ',m)
    print('Total number of cells, n = ', n)
    print('Time elapsed to generate the maze:',delta.total_seconds()*1000)


G = adj_list(maze_rows,maze_cols,walls)

PREV = np.zeros(len(G),dtype=np.int)-1
VISITED = np.full(len(G),False,dtype=bool)

print(G)
r = breadthFirst_Search(G,0,149)
s = depthFirst_Search(G,0,149)
depthFirst_Recursive(G,0)
#print(PREV)
#print(s)
#print(r)

draw_maze(walls,maze_rows,maze_cols) 