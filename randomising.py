#Defining function for randomising desired states of the stacks.
from pydoc import doc
from stack import Stack
from crane import Crane

import random
import numpy as np



#Function for randomising
def randomising(in1):
    #current state of stacks is passed. Necessary attributes of stacks are passed
    current = in1
    no_stacks = len(input1)
    desired = np.zeros(no_stacks)
    totalBox = 0

    #summing number of boxes from each stack
    for x in in1:
        totalBox += x.size

    #Algorithm to construct random desired output
    y = True
    sum = 0
    while y:
        n = random.randrange(0, no_stacks)
        if desired[n] == 0:
            desired[n] = random.randrange(1, 5)
            sum += desired[n]
            if sum < totalBox:
                y = True
            elif sum > totalBox:
                desired[n] = desired[n] - (sum - totalBox)
                y = False
            elif sum == totalBox:
                y = False

    desired_int = desired.astype(int)

    #Function returns the randomised array of stack sizes in type numpy.float64.
    return desired_int

#Test program
x = Stack(2, 1)
y = Stack(3, 2)
z = Stack(0, 3)
a = Stack(1, 4)
b = Stack(0, 5)
c = Stack(4, 6)
d = Stack(0, 7)
input1 = [x, y, z, a, b, c, d]
print(f'input 1: [{x.size}, {y.size}, {z.size}, {a.size}, {b.size}, {c.size}, {d.size}]')
desired = randomising(input1)
print(desired)
