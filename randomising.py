#Defining function for randomising desired states of the stacks.
from pydoc import doc
from stack import Stack

import random
import numpy as np

input = []


def randomising(input):
    #current state of stacks is passed. Necessary attributes of stacks are passed
    current = input
    no_stacks = len(input)
    desired = np.zeros(no_stacks)
    totalBox = 0

    #summing number of boxes from each stack
    for x in input:
        totalBox += x.size

    #Algorithm to construct random desired output
    y = True
    sum = 0
    while y:
        n = random.randrange(1, no_stacks+1)
        if desired[n] != 0:
            desired[n] = random.randrange(1, 5)
            sum += desired[n]
            if sum < totalBox:
                continue
            elif sum > totalBox:
                desired[n] = desired[n] - (sum - totalBox)
                y = False
            elif sum == totalBox:
                y = False

    return desired