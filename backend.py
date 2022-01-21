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

def generate_output(in_column, process, crane):

    out_column = in_column
    for step in process:
        crane.movement(step, out_stack)
    
    for pos in out_stack:
        print(pos)
        print(pos.size, pos.position)



def main():

    input_stack = [3, 1, 2, 1, 4, 0, 1]
    input_columns = initialise_stack(input_stack)

    process_stack = [3, 2, 2, 2, 4, 3, 1, 4, 0]

    jonathan = Crane()

    output_columns = generate_output(input_columns, process_stack, jonathan)
    

    
    

if __name__ == "__main__":
    main()