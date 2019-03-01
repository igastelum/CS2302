import random
import datetime

#Node Functions
class Node(object):
    # Constructor
    def __init__(self, item, next=None):  
        self.item = item
        self.next = next 
        
def PrintNodes(N):
    if N != None:
        print(N.item, end=' ')
        PrintNodes(N.next)
        
def PrintNodesReverse(N):
    if N != None:
        PrintNodesReverse(N.next)
        print(N.item, end=' ')
        
#List Functions
class List(object):   
    # Constructor
    def __init__(self): 
        self.head = None
        self.tail = None
        
def IsEmpty(L):  
    return L.head == None     
        
def Append(L,x): 
    # Inserts x at end of list L
    if IsEmpty(L):
        L.head = Node(x)
        L.tail = L.head
    else:
        L.tail.next = Node(x)
        L.tail = L.tail.next
        
def Print(L):
    # Prints list L's items in order using a loop
    temp = L.head
    while temp is not None:
        print(temp.item, end=' ')
        temp = temp.next
    print()  # New line 

def PrintRec(L):
    # Prints list L's items in order using recursion
    PrintNodes(L.head)
    print() 
    
def Remove(L,x):
    # Removes x from list L
    # It does nothing if x is not in L
    if L.head==None:
        return
    if L.head.item == x:
        if L.head == L.tail: # x is the only element in list
            L.head = None
            L.tail = None
        else:
            L.head = L.head.next
    else:
         # Find x
         temp = L.head
         while temp.next != None and temp.next.item !=x:
             temp = temp.next
         if temp.next != None: # x was found
             if temp.next == L.tail: # x is the last node
                 L.tail = temp
                 L.tail.next = None
             else:
                 temp.next = temp.next.next
         
def PrintReverse(L):
    # Prints list L's items in reverse order
    PrintNodesReverse(L.head)
    print()     
    
def Copy(L):
    C = List()
    temp = L.head
    while temp is not None:
        Append(C, temp.item)
        temp = temp.next    
    return C

def Search(L,x):
    temp = L.head
    if IsEmpty(L):
        return None
    while temp is not None:
        if temp.item != x:
            temp = temp.next
        else:
            return temp

def InsertAfter(L,x,item):
    s = Search(L,x)
    if s is None:
        Append(L,item)
    else:
        s.next = Node(item, s.next)


def Bubble_Sort(L):
    #Bubble sort
    # O(n^2) running time
    '''Bubble sort sorts numbers of a list by making most of the comparisons
        As a result Bubble sort is not to efficient
    '''
    change  = True
    while change:
        t = L.head
        change = False
        while t.next is not None:
            if t.item>t.next.item:
                temp = t.item
                t.item = t.next.item
                t.next.item = temp
                change = True
            t = t.next

#Method obtains the length of the List
def Getlength(L):       
    temp = L.head
    counter = 0
    if IsEmpty(L):
        return 0
    else:
        while temp is not None:
            counter += 1
            temp = temp.next
        return counter
#Median copies a second List and uses it to be sorted and get the middle item
def Median(L):
    C = Copy(L)
    Bubble_Sort(C)
    print('Sorted List:', end=' ')
    Print(C)
    return ElementAt(C,Getlength(C)//2)

#Method receives List and the nth value of the list with given x
def ElementAt(L,x):
    temp = L.head
    while x>1:
        temp = temp.next
        x = x-1
    return temp.item

def Concatenate(L1,L2):
    if IsEmpty(L2):
        return L1
    elif IsEmpty(L1):
        L1.head = L2.head
        L1.tail = L2.tail
        return L1
    else:
        L1.tail.next = L2.head
        L1.tail = L2.tail
        return L1

n = 10
L = List()
#After List is created but empty, appends random values based on what value of n
#with nth, numbers and range of values are defined
for i in range (n):
    Append(L, random.randrange(1,n*10+1,1))


Print(L)
median = Median(L)
print('The Median of the List is:', median)
