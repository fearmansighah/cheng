from turtle import position
from crane import Crane
from stack import Stack



def initialise_stack(stack):
    # creating list       
    columns = [] 
    
    for pos in range(len(stack)):
        nBoxes = stack[pos]
        columns.append(Stack(size=nBoxes, position=pos))
        print(columns[pos].size, columns[pos].position)

    return columns


def main():

    input_stack = [3, 1, 2, 1, 4, 0, 1]
    input_columns = initialise_stack(input_stack)

    process_stack = [3, 2, 2, 2, 4, 3, 1, 4, 0]
    process_columns = initialise_stack(process_stack)

    output_columns = input_columns
    

    jonathan = Crane()
    

if __name__ == "__main__":
    main()