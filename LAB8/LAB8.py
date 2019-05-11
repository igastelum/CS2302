#IVAN GASTELUM
#LABORATORY #8 RANDOMIZATION AND BACKTRACKING
#COURSE 2302 DATA STRUCTURES
#INSTRUCTOR DR. OLAC FUENTES , TA: ANINDITA
#DATE LAST MODIFICATION 5/10/2019

import random
from mpmath import mp
import numpy as np
from math import *
import math

#Check trig functions to be equal by appending True or False in an Adjacency Matrix
def equalTrig(trigfunctions,tries=1000,tolerance=0.0001):
    g = np.zeros((len(trigfunctions),len(trigfunctions)),dtype=bool)
    for i in range(len(trigfunctions)):
        for j in range(len(trigfunctions)):
            g[i][j] = equal(trigfunctions[i],trigfunctions[j])
            if g[i][j] and i!=j:
                print(trigfunctions[i],'and',trigfunctions[j],'are equal')
    return g

#equal method to use randomization method with a range of -Pi to Pi 
#Checks a predetermined number of tries, once it reaches a the results to be less than the tolerance
def equal(f1, f2,tries=1000,tolerance=0.0001):
    for i in range(tries):
        t = random.uniform(-math.pi,math.pi)
        y1 = eval(f1)
        y2 = eval(f2)
        if np.abs(y1-y2)>tolerance:
            return False
    return True

#Example of BACKTRACKING code to reach a certain subset that adds up to a goal
def subsetsum(S,last,goal):
    if goal ==0:
        return True, []
    if goal<0 or last<0:
        return False, []
    res, subset = subsetsum(S,last-1,goal-S[last]) # Take S[last]
    if res:
        subset.append(S[last])
        return True, subset
    else:
        return subsetsum(S,last-1,goal) # Don't take S[last]

dsf = []

#Method to receive original Set and two subsets divided
def Partition(S,S1,S2):
    s1 = sum(S1)    #Sum of subset of first half subset
    s2 = sum(S2)    #Sum of subsets of second half subset
    c = S1+S2       #Concatenate the two subsets to keep track of sequence 
    #print(c)
    if s1==s2:      #Base case if equality has been reached
        return True, S1, S2
    if s1>s2 and c not in dsf:  #if inequality exists, pop minimum value from S1 and append it to S2 if s1>s2
        dsf.append(c)
        y = min(S1)
        S1.remove(y)
        S2.append(y)
        res,S1,S2 = Partition(S,S1,S2)
        return res,S1,S2
    if s1<s2 and c not in dsf: #if inequality exists, pop minimum value from S2 and append it to S1 if s1<s2
        dsf.append(c)           #GLOBAL list dsf to keep track of the sequence that checks in order to stop recursion if 
        y = min(S2)             #False statement is reached
        S2.remove(y)
        S1.insert(0,y)
        res,S1,S2 = Partition(S,S1,S2) #Recursive call to continue checking if equality has not been reached
        return res,S1,S2
    return False,S1,S2
    
#Main method to start inputting values

trigFunctions = ['sin(t)','cos(t)','tan(t)','mp.sec(t)','-sin(t)','-cos(t)','-tan(t)','sin(-t)','cos(-t)','tan(-t)','(sin(t))/(cos(t))','2*sin(t/2)*cos(t/2)','sin(t)*sin(t)','1-(cos(t)*cos(t))','(1-cos(2*t))/2','1/(cos(t))']
print('EXECRCISE 1: DETERMINING EQUALITY OF TRIG FUNCTIONS')
print()
G = equalTrig(trigFunctions)
#print(G)

print()
print('EXERCISE 2: BACKTRACKING CODE FOR PARTITION')
print()
S = [2,4,5,9,12]
print('Given Set:',S)
print()
res,S1,S2 = Partition(S,S[0:(len(S)//2)],S[len(S)//2:])
if res:
    print('There is a solution:', S1,'and', S2)
if not res:
    print('There is no solution')
    