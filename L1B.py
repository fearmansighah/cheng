inp = [4,4,4,1,3,1,1]
out = [4,4,2, ]
lilstack = []
bigstack = []
process = []
cranestep = [0,1,2,3,4]
craneloc = 0
loc2 = 0
diff = 0
i = 0

#determine stacks bigger and smaller than the output and store
for n in range(len(inp)):

    if inp[n] < out[n]:
        diff = out[n] - inp[n]
        while i < diff:
            lilstack.append(n)
            i += 1
        i = 0

    elif inp[n] > out[n]:
        diff = inp[n] - out[n]
        while i < diff:
            bigstack.append(n)
            i += 1
        i = 0

    else:
        continue

#start moving boxes
while (len(lilstack) > 0) or (len(bigstack) > 0):

    if bigstack[0] == craneloc:
        pass

    elif bigstack[0] < craneloc:
        diff = (craneloc - bigstack[0])
        while i < diff:
            process.append(1)
            craneloc -=1
            i += 1
        i = 0

    elif craneloc < bigstack[0]:
        diff = (bigstack[0] - craneloc)
        while i < diff:
            process.append(2)
            craneloc += 1
            i += 1
        i = 0

    process.append(3)
    bigstack.pop(0)

    if lilstack[0] < craneloc:

        diff = (craneloc - lilstack[0])
        while i < diff:
            process.append(1)
            craneloc -=1
            i += 1
        i = 0

    elif craneloc < lilstack[0]:
        diff = (lilstack[0] - craneloc)
        while i < diff:
            process.append(2)
            craneloc += 1
            i += 1
        i = 0

    process.append(4)
    lilstack.pop(0)

print(process)