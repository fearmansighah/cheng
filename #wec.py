#wec
from ast import Break

inp = [3,1,2,1,4,0,3]
out = [2,1,3,1,4,0,1]
lilstack = []
bigstack = []
emptystack = []
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
print(rem, half, sum1, sum2)
#start from the side with the most boxes
if sum2 > sum1:
    start = bigstack[len(bigstack)-1]
else: 
    start = bigstack[0]
print(start)
#start moving boxes
len_lilstack = len(lilstack)
len_bigstack = len(bigstack)

while (len(lilstack) > 0) or (len(bigstack) > 0):
    if start == craneloc:
        pass
    elif start < craneloc:
        step = craneloc - start
        for n in step:
            process.append(1)
    else:
        step = start - craneloc
        for n in step:
            process.append(2)
    
    ## crane = 3
    craneloc = start
    process.append(3)
    print(process)

    step = start - lilstack[len(lilstack)-1]
    print(step)
    
    if start < lilstack[len(lilstack)-1]:
        for n in step:
            process.append(2)
    elif start > lilstack[len(lilstack)-1]:
        for n in step:
            process.append(1)
    else:
        continue

    start = craneloc
    process.append(4)
    if 
    lilstack.pop()
    len_lilstack -= 1

    # once crane has dropped box
    step = start - bigstack(len_bigstack)
    if start < bigstack:
        for n in step:
            process.append(2)
    elif start > bigstack:
        for n in step:
            process.append(1)
    else:
        continue
    
    len_bigstack -= 1


# compare input and output, set flags for each stack starting from the left (=/</>)
# remove (=) stacks from the list of stacks
# for remaining stacks, start from the left
# if stack is larger than output, pick up box and move to closest smaller than output stack
# continue for remainder of stacks
# assume crane has no box