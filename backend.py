from randomising import randomiser
from crane import Crane
from stack import Stack
import numpy as np
import csv


def initialise_stack(stack):
    # creating list       
    columns = [] 
    
    for pos in range(len(stack)):
        nBoxes = stack[pos]
        columns.append(Stack(size=nBoxes, position=pos))

    return columns

def generate_output(in_column, process, crane):

    out_stack = []
    out_columns = in_column
    for step in process:
        crane.movement(step, out_columns[crane.position])
    
    for pos in range(len(out_columns)):
        nBoxes = out_columns[pos].size
        out_stack.append(nBoxes)

    return out_stack, out_columns
    

def print1A(inp, process, out):
    print(inp, process, out, sep='\n')
    print('length of output is ', len(out))
    print('total number of boxes is ', sum(out))
    print('\n')


def print1C(new_out):
    print(new_out)
    print('length of randomised output is ', len(new_out))
    print('total number of boxes is ', sum(new_out))
    print('\n')

    

def generate_rand_out(out):
    new_out_stack = randomiser(out)
    new_out_stack = np.ndarray.tolist(new_out_stack)
    new_out_columns = initialise_stack(new_out_stack)

    with open('output.csv', 'w') as f:
        write = csv.writer(f)
        write.writerow(new_out_stack)
    f.close


    return new_out_stack, new_out_columns
    

def main():

    input_stack = [3, 1, 2, 1, 4, 0, 1]
    input_columns = initialise_stack(input_stack)

    process_stack = [3, 2, 2, 2, 4, 3, 1, 4, 0]

    jonathan = Crane()

    output_stack, output_columns = generate_output(input_columns, process_stack, jonathan)
    rand_out_stack, rand_out_columns = generate_rand_out(output_columns)

    print1A(input_stack, process_stack, output_stack)
    print1C(rand_out_stack)


if __name__ == "__main__":
    main()