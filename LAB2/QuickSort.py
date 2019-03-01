import random
import datetime

#Node Functions
class Node(object):
    # Constructor
    def __init__(self, item, next=None, prev=None):  
        self.item = item
        self.next = next 
        self.prev = prev

#List Functions
class List(object):   
    # Constructor
    def __init__(self): 
        self.head = None
        self.tail = None 

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

def IsEmpty(L):  
    return L.head == None 

def Print(L):
    # Prints list L's items in order using a loop
    temp = L.head
    while temp is not None:
        print(temp.item, end=' ')
        temp = temp.next
    print()  # New line
    
def Copy(L):
    C = List()
    temp = L.head
    while temp is not None:
        Append(C, temp.item)
        temp = temp.next    
    return C

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

def Append(L,x): 
    # Inserts x at end of list L
    new_node = Node(x, None,None)
    if IsEmpty(L):
        L.head = new_node
        L.tail = L.head
    else:
        new_node.prev = L.tail
        new_node.next = None
        L.tail.next = new_node
        L.tail = new_node


#Quick Sort algorithm 
# O(nlog n) running time
def QuickSort(left,right):
    start  = None
    current = None
    Copyof_Integer = 0
    
    #If the left and right pointers are the same, then return
    if left==right:
        return
    
    start = left
    current = start.next
    
    
    #Loop to get to the right of List
    while current is not None:
        if start.item < current.item:
            #Swap items
            Copyof_Integer = current.item
            current.item = start.item
            start.item = Copyof_Integer
        
        if current == right:
            break
        
        current = current.next
        
    Copyof_Integer = left.item
    left.item = current.item
    current.item = Copyof_Integer
    
    Old_current = current
    
    current = current.prev
    if current != None:
        if left.prev != current and current.next != left:
            QuickSort(left,current)
            
    current = Old_current
    current = current.next
    if current != None:
        if current.prev != right and right.next != current:
            QuickSort(current, right) 

def Median(L):
    C = Copy(L)
    QuickSort(C.head,C.tail)
    print('Sorted List:', end=' ')
    Print(C)
    return ElementAt(C,Getlength(C)//2)

def ElementAt(L,x):
    temp = L.head
    while x>1:
        temp = temp.next
        x = x-1
    return temp.item

n = 10
L = List()

#After List is created but empty, appends random values based on what value of n
#with nth, numbers and range of values are defined
for i in range (n):
    Append(L, random.randrange(1,n*10+1,1))
    
Print(L)
start = datetime.datetime.now()
QuickSort(L.head,L.tail)
end = datetime.datetime.now()
delta = end - start
print(Median(L))
print('Running time', delta.total_seconds()*1000)
Print(L)
