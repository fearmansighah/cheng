#wec
from ast import Break
from threading import setprofile

inp = [3,1,2,1,4,0,3]
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
if rem == 0:
    half = len(inp)/2
else:
    half = len(inp)/2 - rem

for n in range(len(inp)):
    if n > half:
        sum2 = sum2 + inp[n]
    else:
        sum1 = sum1 + inp[n]
print(rem, half, sum1, sum2)

#start from the side with the most boxes
if sum2 > sum1:
    start = bigstack[len(bigstack)-1]
else: 
    start = bigstack[0]
print(start)

#start moving boxes
while (len(lilstack) > 0) or (len(bigstack) > 0):
    if start == craneloc:
        pass
    elif start < craneloc:
        step = craneloc - start
        for n in range(step):
            process.append(1)
    else:
        step = start - craneloc
        for n in range(step):
            process.append(2)
    craneloc = start
    inp[craneloc] -= 1
    if inp[craneloc] == out[craneloc]:
        bigstack.remove(craneloc)
    else:
        pass
    print(process)
    print(craneloc)
    process.append(3)

    # box in hand
    step = start - lilstack[len(lilstack)-1]
    if start < lilstack[len(lilstack)-1]:
        for n in range(step):
            process.append(2)
            craneloc += 1
    elif start > lilstack[len(lilstack)-1]:
        for n in range(step):
            process.append(1)
            craneloc -=1
    else:
        continue

    inp[craneloc] += 1
    if inp[craneloc] == out[craneloc]:
        lilstack.remove(craneloc)
    else:
        pass
    process.append(4)
    print(process)
    print(craneloc)
    
    # once crane has dropped box
    step = start - bigstack[len(bigstack)-1]
    if start < bigstack[len(bigstack)-1]:
        for n in range(step):
            process.append(2)
            craneloc += 1 
    elif start > bigstack[len(bigstack)-1]:
        for n in range(step):
            process.append(1)
            craneloc -= 1
    else:
        continue


# compare input and output, set flags for each stack starting from the left (=/</>)
# remove (=) stacks from the list of stacks
# for remaining stacks, start from the left
# if stack is larger than output, pick up box and move to closest smaller than output stack
# continue for remainder of stacks
# assume crane has no box