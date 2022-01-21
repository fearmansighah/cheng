from randomising import randomiser
from crane import Crane
from stack import Stack



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



def main():

    input_stack = [3, 1, 2, 1, 4, 0, 1]
    input_columns = initialise_stack(input_stack)

    process_stack = [3, 2, 2, 2, 4, 3, 1, 4, 0]

    jonathan = Crane()

    output_stack, output_columns = generate_output(input_columns, process_stack, jonathan)

    print1A(input_stack, process_stack, output_stack)
    print1B()
    

    
    

if __name__ == "__main__":
    main()