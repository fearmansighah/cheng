#Defining function for randomising desired states of the stacks.
from stack import Stack

import random
import numpy as np



#Function for randomising
def randomiser(in1):
    #current state of stacks is passed. Necessary attributes of stacks are passed
    current = in1
    no_stacks = len(in1)
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

