import random
import datetime

#Node Functions
class Node(object):
    # Constructor
    def __init__(self, item, next=None):  
        self.item = item
        self.next = next 
        
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

#This is the main method to call the Merge Sort Algorithm
# O(nlog n) running time
def MergeSort(L):
    if Getlength(L)<=1:     #base case of recursive method
        return L            #returns L when L has one or zero elements after splitting
    else:
        Left_Half, Right_Half = Split_Lists(L) #if list is has more than 2 elements, recursion continues
        left = MergeSort(Left_Half)
        right = MergeSort(Right_Half)
        return Merge_Lists(left, right, L)
    #return Merge_Lists(left, right)

#Method to split a list L into Right List RL, and Left List LL
def Split_Lists(L):
    #Two seprate lists are created in order to store values
    LL = List()
    RL = List()
    if Getlength(L)<=1:     #base case when one list has one element and the other is empty
        Append(LL,L.head.item)
        return LL, None
    else:                   #when both are not empty, keeps splitting values
        temp1 = L.head
        midPoint = Getlength(L)//2
        counter = 0         #a counter is created to stop at the mid point of the List
        while counter!=midPoint:
            Append(LL,temp1.item)
            counter=counter + 1
            temp1 = temp1.next
                            # this part stores the second half of the list into the right list
        while counter != Getlength(L):
            Append(RL,temp1.item)
            counter=counter+1
            temp1 = temp1.next
        
        return LL,RL

#The final method to merge back two lists into one and sort them in their correct spot
#original L is called in this method to automatically store values 
def Merge_Lists(L1,L2,L):
    temp1 = L1.head
    temp2 = L2.head
    temp = L.head
    while temp1 is not None and temp2 is not None:
        if temp1.item < temp2.item:
            temp.item = temp1.item
            temp1 = temp1.next
            temp = temp.next
        else:
            temp.item = temp2.item
            temp2 = temp2.next
            temp = temp.next
    while temp1 is not None:
        temp.item = temp1.item
        temp1 = temp1.next
        temp = temp.next
    while temp2 is not None:
        temp.item = temp2.item
        temp2 = temp2.next
        temp = temp.next
    
    return L

def Copy(L):
    C = List()
    temp = L.head
    while temp is not None:
        Append(C, temp.item)
        temp = temp.next    
    return C

def Median(L):
    C = Copy(L)
    MergeSort(C)
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
L = MergeSort(L)
end = datetime.datetime.now()
delta = end - start
print('Running time', delta.total_seconds()*1000)
Print(L)