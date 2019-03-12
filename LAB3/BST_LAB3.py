#IVAN GASTELUM
#COURSE 2302 DATA STRUCTURES
#INSTRUCTOR DR. OLAC FUENTES , TA: ANINDITA
#DATE LAST MODIFICATION 3/11/2019

class BST(object):
    # Constructor
    def __init__(self, item, left=None, right=None):  
        self.item = item
        self.left = left 
        self.right = right      
        
def Insert(T,newItem):
    if T == None:
        T =  BST(newItem)
    elif T.item > newItem:
        T.left = Insert(T.left,newItem)
    else:
        T.right = Insert(T.right,newItem)
    return T

def Delete(T,del_item):
    if T is not None:
        if del_item < T.item:
            T.left = Delete(T.left,del_item)
        elif del_item > T.item:
            T.right = Delete(T.right,del_item)
        else:  # del_item == T.item
            if T.left is None and T.right is None: # T is a leaf, just remove it
                T = None
            elif T.left is None: # T has one child, replace it by existing child
                T = T.right
            elif T.right is None:
                T = T.left    
            else: # T has two chldren. Replace T by its successor, delete successor
                m = Smallest(T.right)
                T.item = m.item
                T.right = Delete(T.right,m.item)
    return T
         
def InOrder(T):
    # Prints items in BST in ascending order
    if T is not None:
        InOrder(T.left)
        print(T.item,end = ' ')
        InOrder(T.right)
  
def InOrderD(T,space):
    # Prints items and structure of BST
    if T is not None:
        InOrderD(T.right,space+'   ')
        print(space,T.item)
        InOrderD(T.left,space+'   ')
  
def SmallestL(T):
    # Returns smallest item in BST. Returns None if T is None
    if T is None:
        return None
    while T.left is not None:
        T = T.left
    return T   
 
def Smallest(T):
    # Returns smallest item in BST. Error if T is None
    if T.left is None:
        return T
    else:
        return Smallest(T.left)

def Largest(T):
    if T.right is None:
        return T
    else:
        return Largest(T.right)   

def Find(T,k):
    # Returns the address of k in BST, or None if k is not in the tree
    if T is None or T.item == k:
        return T
    if T.item<k:
        return Find(T.right,k)
    return Find(T.left,k)
    
def FindAndPrint(T,k):
    f = Find(T,k)
    if f is not None:
        print(f.item,'found')
    else:
        print(k,'not found')
   

#Iterative method to return the address of the key k, only if k is in the Tree
def Search_Iterative(T, k):
    while T is not None:
        if T.item == k:
            break
        elif T.item>k:
            T = T.left
        elif T.item<k:
            T = T.right
    return T
        
#Converts a sorted list into a BST
def FromList_ToTree(A):
    if not A:
        return None
    
    mid = (len(A))//2
    
    T = BST(A[mid])
    
    T.left = FromList_ToTree(A[:mid])
    T.right = FromList_ToTree(A[mid+1:])
    return T

#Method that return the value of the depth from root of T
def GetDepth(T):
    depth = 0
    if T is None:
        return 0
    elif T.left is not None:
        depth = 1 + GetDepth(T.left)
        return depth
    elif T.right is not None:
        depth = 1 + GetDepth(T.right)
    return depth

#Prints the values of the tree at each level of depth
def Print_ByDepth(T):
    for i in range(GetDepth(T)+1):
        print('Keys at depth:',i,':',List_withDepth(T,[],i))
                
#Returns a list of items at each level of depth
def List_withDepth(T,List,depth):
    if T is None:
        return List
    if depth == 0:
        List.append(T.item)
        return List
    else:
        List_withDepth(T.left,List,depth-1)
        List_withDepth(T.right,List,depth-1)
        return List
        
#Converts a balanced binary search tree into a sorted list
def FromTree_ToList(T,A):
    if T is not None:
        FromTree_ToList(T.left,A)
        A.append(T.item)
        FromTree_ToList(T.right,A)
    return A
        
# NUMBER 3: balanced binary search tree given a sorted list as input. Note: this should not use the insert operation,
#the tree must be built directly from the list in O(n) time.  
T = None
A = [1,2,3,4,5,7,8,9,10,12,15,18]
T = FromList_ToTree(A)


#NUMBER 2, RETURNS THE ADDRESS OF k IN BST, If k is not found, returns None
key = 7
print(Search_Iterative(T,key))
'''
for a in A:
    T = Insert(T,a)
'''

#NUMBER 4, Extracting the elements in a binary search tree into a sorted list. 
#As above, this should be done in O(n) time. 
E =[]
E = FromTree_ToList(T,E) 
print(' NEW list: ',E)

#NUMBER 5, Printing the elements in a binary tree ordered by depth. 
h = GetDepth(T)
print('The Depth from root is:', h)
Print_ByDepth(T)

