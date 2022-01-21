#wec
from ast import Break
import numpy as np

inp = [3,1,2,1,4,0,1]
out = [2,1,3,1,4,0,1]
lilstack = []
bigstack = []
process = []
crane = [0,1,2,3,4]
craneloc = 0
sum1 = 0
sum2 = 0
start = 0
step = 0

#determine stacks bigger and smaller than the output and store
for n in range(len(inp)):
    if inp[n] < out[n]:
        lilstack.append(n)
    elif inp[n] > out[n]:
        bigstack.append(n)
    else:
        continue

# determine the half of the in with more boxes
rem = len(inp)%2
half = len(inp)/2 - rem
for n in range(len(inp)):
    if n > half:
        sum1 = sum1 + inp[n]
    else:
        sum2 = sum2 + inp[n]

#start from the side with the most boxes
if sum2>sum1:
    start = bigstack[len(bigstack)-1]
    start_direction = 0
else: 
    start = bigstack[0]
    start_direction = 1

#start moving boxes
if start = craneloc:
    continue
elif start < craneloc:
    step = craneloc - start
    # crane = 2 xstep
else:
    step = start - craneloc
    #crane = 1 xstep

len_lilstack = len(lilstack)
len_bigstack = len(bigstack)

## crane = 3
step = start - lilstack(len_lilstack)
if start < lilstack:
    #crane = 2
elif start > lilstack:
    #crane = 1
start = craneloc
#crane = 4 
len_lilstack -= 1
lilstack.remove(len_lilstack)

# once crane has dropped box
step = start - bigstack(len_bigstack)
if start < bigstack:
    #crane = 2
elif start > bigstack:
    #crane = 1


# compare input and output, set flags for each stack starting from the left (=/</>)
# remove (=) stacks from the list of stacks
# for remaining stacks, start from the left
# if stack is larger than output, pick up box and move to closest smaller than output stack
# continue for remainder of stacks
# assume crane has no box