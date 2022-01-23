from randomising import randomiser
from process_config_solver import findProcess
from crane import Crane
from stack import Stack
import csv


def initialise_stack(stack):     
    columns = [] 
    
    for pos in range(len(stack)):
        nBoxes = stack[pos]
        columns.append(Stack(size=nBoxes, position=pos))

    return columns

def initialise_csv(csv):
    with open(csv, 'w') as f:
       f.truncate()
    f.close


def generate_output(in_column, process, crane):
    out_stack = []
    out_columns = in_column
    for code in process:
        crane.movement(code, out_columns[crane.position])
    
    for pos in range(len(out_columns)):
        nBoxes = out_columns[pos].size
        out_stack.append(nBoxes)

    with open('output.csv', 'w') as f:
        write = csv.writer(f)
        write.writerow(out_stack)
    f.close

    return out_stack, out_columns


def generate_rand_out(out):
    new_out_stack = randomiser(out)
    new_out_columns = initialise_stack(new_out_stack)

    with open('output.csv', 'w') as f:
        write = csv.writer(f)
        write.writerow(new_out_stack)
    f.close

    return new_out_stack, new_out_columns


def readInpProCSV(csv_file):
    with open(csv_file, newline='') as f:
        reader = csv.reader(f)
        data = list(reader)
    f.close()

    inp =  [int(i) for i in data[0]]
    
    process = [int(i) for i in data[1]]

    return inp, process


def print1A(inp, process, out):
    print('input configuration: ', inp)
    print('process configuration: ', process)
    print('output configuration: ', out)
    print('length of input configuration is: ', len(out))
    print('total number of boxes for input configuration: ', sum(out))
    print('length of output conifguration is: ', len(out))
    print('total number of boxes for output configuration: ', sum(out))
    print('\n')


def print1B(process):
    print(f'process configuration for randomization was: ', process)
    

def print1C(new_out):
    print('randomised output configuration: ', new_out)
    print('length of randomised output configuration is: ', len(new_out))
    print('total number of boxes for randomised output configuration is: ', sum(new_out))
    print('\n')

        

def main():

    initialise_csv('output.csv')

    input_stack, process_stack = readInpProCSV('inputAndProcess.csv')

    input_columns = initialise_stack(input_stack)

    jonathan = Crane()

    output_stack, output_columns = generate_output(input_columns, process_stack, jonathan)
    rand_out_stack, rand_out_columns = generate_rand_out(output_columns)
    rand_process_config = findProcess(output_stack, rand_out_stack, jonathan.position)

    print1A(input_stack, process_stack, output_stack)
    print1C(rand_out_stack)
    print1B(rand_process_config)


if __name__ == "__main__":
    main()