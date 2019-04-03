import numpy as np
import datetime
import math
# Implementation of hash tables with chaining using strings

class Word(object):
    #Constructor
    def __init__(self, word, emb):
        self.word = word
        self.emb = emb

class HashTableC(object):
    # Builds a hash table of size 'size'
    # Item is a list of (initially empty) lists
    # Constructor
    def __init__(self,size):  
        self.item = []
        for i in range(size):
            self.item.append([])
        self.num_items = 0

def MaxHeight(T):
    temp = T
    if T is None:
        return 0
    if T is not None:
        LeftH = 1 + MaxHeight(temp.left)
        RightH = 1 + MaxHeight(temp.right)
        if LeftH > RightH:
            return LeftH
        else:
            return RightH

def LoadFactor(H):
    LF = H.num_items / len(H.item)
    return LF
    
def InsertC(H,W,l):
    # Inserts k in appropriate bucket (list) 
    # Does nothing if k is already in the table
    H.num_items += 1
    b = HashCode(W.word)%len(H.item)
    H.item[b].append([W,l])
   
def FindC(H,k):
    # Returns bucket (b) and index (i) 
    # If k is not in table, i == -1
    b = h(k,len(H.item))
    for i in range(len(H.item[b])):
        if H.item[b][i][0] == k:
            return b, i, H.item[b][i][1]
    return b, -1, -1
 
def Delete(T,del_item):
    if T is not None:
        if del_item.word < T.item.word:
            T.left = Delete(T.left,del_item)
        elif del_item.word > T.item.word:
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
                T.item.word = m.item.word
                T.right = Delete(T.right,m.item)    

def NumberOfNodes(T):
    if T is None:
        return 0
    else:
        return 1 + NumberOfNodes(T.left) + NumberOfNodes(T.right)


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

def h(s,n):
    r = 0
    for c in s:
        r = (r*n + ord(c))% n
    return r

def HashCode(s):
    g = 31
    Hash = 0
    for a in range(len(s)):
        Hash = g * Hash + ord(s[a])
    return Hash

def ReSize(H):
    temp = HashTableC(len(H.item)*2)
    for a in range (len(H.item)):
        for j in H.item[a]:
            InsertC(H,W,len(H.item))
    return temp

def PercentageH(H):
    count = 0
    for a in H.item:
        if a is None:
            count+=1
    percentage = (count/len(H.item))*100
    return percentage

'''
H = HashTableC(11)
A = ['data','structures','computer','science','university','of','texas','at','el','paso']
for a in A:
    InsertC(H,a,len(a))
    print(H.item)

for a in A: # Prints bucket, position in bucket, and word length
    print(a,FindC(H,a))
'''    
 
# Code to implement a binary search tree 
# Programmed by Olac Fuentes
# Last modified February 27, 2019


#BINARY SEARCH TREE 
class BST(object):
    # Constructor
    def __init__(self, item, left=None, right=None):  
        self.item = item
        self.left = left 
        self.right = right      

        
def InsertBST(T,newItem):
    if T == None:
        T =  BST(newItem)
    elif T.item.word > newItem.word:
        T.left = InsertBST(T.left,newItem)
    else:
        T.right = InsertBST(T.right,newItem)
    return T

def PrintTree(T):
    if T is None:
        return 
    else:
        print(T.item.word)
        PrintTree(T.left)
        PrintTree(T.right)

def FindBST(T,k):
    # Returns the address of k in BST, or None if k is not in the tree
    if T is None or T.item.word == k:
        return T
    if T.item.word<k:
        return FindBST(T.right,k)
    return FindBST(T.left,k)

print('Choose table implementation')
print('Type 1 for binary search tree or 2 for hash table with chaining')
choice = int(input('Choice:'))


def SumSquareEmb(emb):
    Sum = 0
    for i in emb:
        Sum = Sum + emb[i]**2
    return Sum

#CHOICE 1 READING AND BUILDING BST
if choice == 1:
    print('Building Binary Search Tree')
    F = open("glove.6B.50d.txt", encoding='utf-8')
    Array_Objects = np.array([])
    fakeword = Word("ssssss", [0,0,0,0,0,0,0])
    T = BST(fakeword)
    start = datetime.datetime.now()
    for line in F:
        A = line.split(' ')
        word = A[0]
        floats = []
        for i in range (1,len(A)):
            floats.append(float(A[i]))
        #Array_Objects.append(Word(word,floats))
        floats = np.array(floats, dtype=np.float)
        if word.isalpha():
            W = Word(word,floats)
            InsertBST(T,W)
    
    
    end = datetime.datetime.now()
    delta = end - start
    print('Binary Search Tree stats:')
    print('Number of nodes', NumberOfNodes(T))
    print('Height', MaxHeight(T))
    print('Running time for binary search tree construction:', delta.total_seconds()*1000)
    
    #Testing Similarities
    
    D = open("words.txt", encoding='utf-8')
    for line in D:
        B = line.split(' ')
        word1 = str(B[0])
        word2 = str(B[1])
        print(T.right.item.word,word1)
        print(T.item.word,word2)
        Obj1 = FindBST(T,word1)
        print('current word',T.item.word)
        Obj2 = FindBST(T,word2)
        print(Obj1.item.word)
        print(Obj2.item.word)
        if Obj1 is None or Obj2 is None:
            print('One word is not found in the BST')
            break
        Emb1 = Obj1.item.emb
        Emb2 = Obj2.item.emb
        DotProduct = np.dot(Emb1,Emb2)
        Magnitude = math.sqrt(SumSquareEmb(Emb1)) * math.sqrt(SumSquareEmb(Emb2))
        FinalResult = DotProduct/Magnitude
        print('kkkkkkkkkkk')
    


#CHOICE 2 READING AND BUILDING HASH TABLE
if choice == 2:
    print('Building the Hash Table with chaining')
    F = open("glove.6B.50d.txt", encoding='utf-8')
    Array_Objects = np.array([])
    initial_size = 400010
    loadFactor = 0
    H = HashTableC(initial_size)
    for line in F:
        A = line.split(' ')
        word = A[0]
        floats = []
        for i in range (1,len(A)):
            floats.append(float(A[i]))
        #Array_Objects.append(Word(word,floats))
        floats = np.array(floats, dtype=np.float)
        W = Word(word,floats)
        InsertC(H,W,len(H.item))
    
    print('Hash Table with chaining stats:')
    print('Initial Table size', initial_size)
    loadfactor = LoadFactor(H)
    while loadfactor>1:
        H = ReSize(H)
        loadfactor = LoadFactor(H)
    print('Final Table size', len(H.item))
    print('Load Factor:', loadFactor)
    print('Percentage of empty lists:', PercentageH(H),'%')
    
    
    '''
    loadfactor = LoadFactor(H)
    while loadfactor > 1:
        H = ReSize(H)
        loadfactor = LoadFactor(H)
    '''
    
    
        

#Delete(T,fakeword)
#print(MaxHeight(T))
#rint(T.right.item.myArray)
#print(Array_Objects[0].word)



    