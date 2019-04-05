#IVAN GASTELUM
#COURSE 2302 DATA STRUCTURES
#INSTRUCTOR DR. OLAC FUENTES , TA: ANINDITA
#DATE LAST MODIFICATION 4/4/2019

import numpy as np
import datetime
import math
# Implementation of hash tables with chaining using strings

#WORD OBJECT CREATION
class Word(object):
    #Constructor
    def __init__(self, word, emb):
        self.word = word
        self.emb = emb

#HASH TABLE CONSTRUCTOR
class HashTableC(object):
    # Builds a hash table of size 'size'
    # Item is a list of (initially empty) lists
    # Constructor
    def __init__(self,size):  
        self.item = []
        for i in range(size):
            self.item.append([])
        self.num_items = 0

#Return the maximum height when a BST is given
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

#Calculates the Load Factor when a Hash Table with chaining is given
def LoadFactor(H):
    LF = H.num_items / len(H.item)
    return LF

#Calculates the standard deviation with a Hash Table reference
def StandardDev(H):
    x = []
    for a in H.item:
        x.append(len(a))
    x = np.array(x)
    STD = np.std(x)
    return STD

#Inserts an object W into a Hash Table H in their respective bucket
def InsertC(H,W):
    # Inserts k in appropriate bucket (list) 
    # Does nothing if k is already in the table
    H.num_items += 1
    b = HashCode(W.word)%len(H.item)
    H.item[b].append(W)

#Finds the word in the Hash Table   
def FindC(H,k):
    # Returns bucket (b) and index (i) 
    # If k is not in table, i == -1
    b = HashCode(k)%len(H.item)
    for i in range(len(H.item[b])):
        if H.item[b][i].word == k:
            return b, i, H.item[b][i]
    return b, -1, -1
     
#Counts number of nodes in a BST T 
def NumberOfNodes(T):
    if T is None:
        return 0
    else:
        return 1 + NumberOfNodes(T.left) + NumberOfNodes(T.right)

#Uses a formula to calculate the index of Hash Table where the item should be inserted
def HashCode(s):
    g = 253
    Hash = 0
    for a in range(len(s)):
        Hash = g * Hash + ord(s[a])
    return Hash

#Resizes the current Hash Table by double the size
def ReSize(H):
    temp = HashTableC(len(H.item)*2)
    for a in range (len(H.item)):
        for j in H.item[a]:
            InsertC(H,W)
    return temp

#Calculates the percentage of empty buckets in a Hash Table
def PercentageH(H):
    count = 0
    for a in H.item:
        if not a:
            count+=1
    percentage = (count/len(H.item))*100
    return percentage

  
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

#Inserts object of words and embedings to the BST   
def InsertBST(T,newItem):
    if T == None:
        T =  BST(newItem)
    elif T.item.word > newItem.word:
        T.left = InsertBST(T.left,newItem)
    else:
        T.right = InsertBST(T.right,newItem)
    return T

#Traverses the whole BST T and print every word item
def PrintTree(T):
    if T is None:
        return
    else:
        PrintTree(T.left)
        print(T.item.word, end=' ')
        PrintTree(T.right)
        print(T.item.word, end=' ')

def FindBST(T,k):
    # Returns the address of k in BST, or None if k is not in the tree
    if T is None or T.item.word == k:
        return T
    if T.item.word<k:
        return FindBST(T.right,k)
    return FindBST(T.left,k)

def FindBST1(T,k):
    # Returns the address of k in BST, or None if k is not in the tree
    if T is None or T.item.word == k:
        return T
    if T.item.word<k:
        return FindBST1(T.right,k)
    return FindBST1(T.left,k)

print('Choose table implementation')
print('Type 1 for binary search tree or 2 for hash table with chaining')
choice = int(input('Choice:'))

#Calculates the sum of squares of the whole array of embeddings
def SumSquareEmb(emb):
    Sum = 0
    for i in range (len(emb)):
        Sum = Sum + emb[i]**2
    return Sum

#CHOICE 1 READING AND BUILDING BST
if choice == 1:
    print('Building Binary Search Tree')
    F = open("glove.6B.50d.txt", encoding='utf-8-sig')
    Array_Objects = np.array([])
    fakeword = Word("ssssss", [0,0,0,0,0,0,0])
    T = BST(fakeword)
    start = datetime.datetime.now()
    for line in F:
        line = line.rstrip('\n')
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
    
    #PrintTree(T)
    end = datetime.datetime.now()
    delta = end - start
    print('Binary Search Tree stats:')
    print('Number of nodes', NumberOfNodes(T))
    print('Height', MaxHeight(T))
    print('Running time for binary search tree construction:', delta.total_seconds()*1000)
    print()
    
    #Testing Similarities
    print('Reading word file to determine similarities')
    print()
    
    D = open("words.txt", encoding='utf-8-sig')
    for line in D:
        line = line.rstrip('\n')
        #line = line.rstrip()
        B = line.split(' ')
        word1 = str(B[0])
        word2 = str(B[1])
        Obj1 = FindBST(T,word1)
        Obj2 = FindBST1(T,word2)
        if Obj1 is None or Obj2 is None:
            print('One word is not found in the BST')
            break
        Emb1 = Obj1.item.emb
        Emb2 = Obj2.item.emb
        DotProduct = np.dot(Emb1,Emb2)
        Magnitude = math.sqrt(SumSquareEmb(Emb1)) * math.sqrt(SumSquareEmb(Emb2))
        FinalResult = DotProduct/Magnitude
        print('Similarity [', Obj1.item.word,',',Obj2.item.word,'] =',FinalResult)
    


#CHOICE 2 READING AND BUILDING HASH TABLE
if choice == 2:
    print('Building the Hash Table with chaining')
    F = open("glove.6B.50d.txt", encoding='utf-8-sig')
    Array_Objects = np.array([])
    initial_size = 500000
    loadFactor = 0
    H = HashTableC(initial_size)
    start = datetime.datetime.now()
    for line in F:
        line = line.rstrip('\n')
        A = line.split(' ')
        word = A[0]
        floats = []
        for i in range (1,len(A)):
            floats.append(float(A[i]))
        #Array_Objects.append(Word(word,floats))
        floats = np.array(floats, dtype=np.float)
        W = Word(word,floats)
        InsertC(H,W)
    
    end = datetime.datetime.now()
    delta = end - start
    
    print('Hash Table with chaining stats:')
    print('Initial Table size', initial_size)
    loadfactor = LoadFactor(H)
    while loadfactor>1:
        H = ReSize(H)
        loadfactor = LoadFactor(H)
    print('Final Table size', len(H.item))
    print('Load Factor:', loadFactor)
    print('Percentage of empty lists:', PercentageH(H),'%')
    print('Running time for a Hash Table construction:', delta.total_seconds()*1000)
    print('Standard deviation of the lengths of the lists:', StandardDev(H))
    print()
    
    print('Reading word file to determine similarities')
    print()
    #READING Similarities
    D = open("words.txt", encoding='utf-8-sig')
    for line in D:
        line = line.rstrip('\n')
        B = line.split(' ')
        word1 = str(B[0])
        word2 = str(B[1])
        Obj1 = FindC(H,word1)
        Obj2 = FindC(H,word2)
        if Obj1 is None or Obj2 is None:
            print('One word is not found in the BST')
            break
        Emb1 = Obj1[2].emb
        Emb2 = Obj2[2].emb
        DotProduct = np.dot(Emb1,Emb2)
        Magnitude = math.sqrt(SumSquareEmb(Emb1)) * math.sqrt(SumSquareEmb(Emb2))
        FinalResult = DotProduct/Magnitude
        print('Similarity [', Obj1[2].word,',',Obj2[2].word,'] =',FinalResult)
    
    
    