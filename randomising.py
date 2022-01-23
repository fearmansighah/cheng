import random
import numpy as np

def randomiser(inp):
    # current state of stacks is passed. Necessary attributes of stacks are passed
    no_stacks = len(inp)
    desired = np.zeros(no_stacks)
    totalBox = 0

    # summing number of boxes from each stack
    for x in inp:
        totalBox += x.size

    # algorithm to construct random desired output
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

    # randomised array of stack sizes in type numpy.float64.
    desired_int = desired.astype(int)

    # convert numpy array to Python list
    desired_int= np.ndarray.tolist(desired_int)

    return desired_int

