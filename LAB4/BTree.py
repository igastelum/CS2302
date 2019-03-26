#IVAN GASTELUM ID# 80481427
#DATA STRUCTURES 2302 
#PROFESSOR OLAC FUENTE TA: NATH ANINDITA
#DATE OF LAST MODIFICATION: 3/25/2019

class BTree(object):
    # Constructor
    def __init__(self,item=[],child=[],isLeaf=True,max_items=5):  
        self.item = item
        self.child = child 
        self.isLeaf = isLeaf
        if max_items <3: #max_items must be odd and greater or equal to 3
            max_items = 3
        if max_items%2 == 0: #max_items must be odd and greater or equal to 3
            max_items +=1
        self.max_items = max_items

def FindChild(T,k):
    # Determines value of c, such that k must be in subtree T.child[c], if k is in the BTree    
    for i in range(len(T.item)):
        if k < T.item[i]:
            return i
    return len(T.item)
             
def InsertInternal(T,i):
    # T cannot be Full
    if T.isLeaf:
        InsertLeaf(T,i)
    else:
        k = FindChild(T,i)   
        if IsFull(T.child[k]):
            m, l, r = Split(T.child[k])
            T.item.insert(k,m) 
            T.child[k] = l
            T.child.insert(k+1,r) 
            k = FindChild(T,i)  
        InsertInternal(T.child[k],i)   
            
def Split(T):
    #print('Splitting')
    #PrintNode(T)
    mid = T.max_items//2
    if T.isLeaf:
        leftChild = BTree(T.item[:mid]) 
        rightChild = BTree(T.item[mid+1:]) 
    else:
        leftChild = BTree(T.item[:mid],T.child[:mid+1],T.isLeaf) 
        rightChild = BTree(T.item[mid+1:],T.child[mid+1:],T.isLeaf) 
    return T.item[mid], leftChild,  rightChild   
      
def InsertLeaf(T,i):
    T.item.append(i)  
    T.item.sort()

def IsFull(T):
    return len(T.item) >= T.max_items

def Insert(T,i):
    if not IsFull(T):
        InsertInternal(T,i)
    else:
        m, l, r = Split(T)
        T.item =[m]
        T.child = [l,r]
        T.isLeaf = False
        k = FindChild(T,i)  
        InsertInternal(T.child[k],i)   
        
#Method to compute the heigt of a given B Tree     
def height(T):
    if T.isLeaf:
        return 0
    return 1 + height(T.child[0])
        
        
def Search(T,k):
    # Returns node where k is, or None if k is not in the tree
    if k in T.item:
        return T
    if T.isLeaf:
        return None
    return Search(T.child[FindChild(T,k)],k)
  
#Method that return the depth at wich the key k is in the B Tree
def SearchDepth_WithKey(T,k):
    depth = -1
    if k in T.item:
        depth += 1
        return depth
    if T.isLeaf:
        return -10
    else:
        depth = 1 + SearchDepth_WithKey(T.child[FindChild(T,k)],k)
        if depth<0:
            return 1
    return depth
#With given B Tree, it return the smallest number 
def MinElement(T,d):
    if d<0:
        return None
    if d==0:
        return T.item[0]
    else:
        return MinElement(T.child[0],d-1)
#With given B Tree, it returns the largest number in B Tree
def MaxElement(T,d):
    if d<0:
        return None
    if d==0:
        return T.item[-1]
    else:
        return MaxElement(T.child[-1], d-1)
#Method that counts the number of node at a given depth d
def NumberOfNodes(T,d):
    count = 0
    if d<0:
        return None
    if d==0:
        return 1
    else:
        for c in T.child:
            count+=NumberOfNodes(c,d-1)
        return count
#counts the number of Nodes that are full in the B Tree
def FullNodes(T):
    count = 0
    if len(T.item) == T.max_items:
        return 1
    
    if not T.isLeaf:
        for c in T.child:
            count+=FullNodes(c)
    return count  

#Method to count the numbers of leaves that are full 
def FullLeaves(T):
    count = 0
    if len(T.item)==T.max_items and T.isLeaf:
        return 1
    
    if not T.isLeaf:
        for c in T.child:
            count+=FullNodes(c)
    return count 

#Method to obtain all values in a B Tree and converts them into a sorted list
def BTreeToSortedList(T,List):
    if T.isLeaf:
        for i in range(len(T.item)):
            List.append(T.item[i])
    else:
        for i in range (len(T.item)):
            BTreeToSortedList(T.child[i], List)
            List.append(T.item[i])
        BTreeToSortedList(T.child[-1], List)
    return List
            

def PrintAtDepth(T,d):
    if d<0:
        return None
    if d==0:
        for i in range (len(T.item)):
            print(T.item[i],end=' ')
    else:
        for c in T.child:
            PrintAtDepth(c,d-1)                
        
def Print(T):
    # Prints items in tree in ascending order
    if T.isLeaf:
        for t in T.item:
            print(t,end=' ')
    else:
        for i in range(len(T.item)):
            Print(T.child[i])
            print(T.item[i],end=' ')
        Print(T.child[len(T.item)])    
 
def PrintD(T,space):
    # Prints items and structure of B-tree
    if T.isLeaf:
        for i in range(len(T.item)-1,-1,-1):
            print(space,T.item[i])
    else:
        PrintD(T.child[len(T.item)],space+'   ')  
        for i in range(len(T.item)-1,-1,-1):
            print(space,T.item[i])
            PrintD(T.child[i],space+'   ')
    
def SearchAndPrint(T,k):
    node = Search(T,k)
    if node is None:
        print(k,'not found')
    else:
        print(k,'found',end=' ')
        print('node contents:',node.item)
    
L = [30, 50, 10, 20, 60, 70, 100, 40, 90, 80, 110, 120, 1, 11 , 3, 4, 5,105, 115, 200, 2, 45, 6]
T = BTree()    
for i in L:
    print('Inserting',i)
    Insert(T,i)
    PrintD(T,'') 
    #Print(T)
    print('\n####################################')
    
SearchAndPrint(T,60)
SearchAndPrint(T,200)
SearchAndPrint(T,25)
SearchAndPrint(T,20)

print('The height of the B Tree is:',height(T))


#EXERCISE 2: Converting a B Tree into a Sorted list
l = []
l = BTreeToSortedList(T,l)
print('New Sorted list:', l)
print()

#EXERCISE 3 & 4: Executing the method to find the smallest element at given depth 'd'
depth = 0
print ('Minimum element at depth', depth, ':', MinElement(T,depth))
print ('Maximum element at depth', depth, ':', MaxElement(T,depth))
print('Number of nodes at given depth:', NumberOfNodes(T,depth))
PrintAtDepth(T,depth)
print()
depth = 1
print ('Minimum element at depth', depth, ':', MinElement(T,depth))
print ('Maximum element at depth', depth, ':', MaxElement(T,depth))
print('Number of nodes at given depth:', NumberOfNodes(T,depth))
PrintAtDepth(T,depth)
print()
depth = 2
print ('Minimum element at depth', depth, ':', MinElement(T,depth))
print ('Maximum element at depth', depth, ':', MaxElement(T,depth))
print('Number of nodes at given depth:', NumberOfNodes(T,depth))
PrintAtDepth(T,depth)

print()
print('Number of nodes in the tree that are full:', FullNodes(T))
print('Number of leaves in the tree that are full:', FullLeaves(T))

#EXERCISE 9 TO RETURN THE DEPTH if given key is in B Tree
key = 17
k = SearchDepth_WithKey(T,key)
print(k)