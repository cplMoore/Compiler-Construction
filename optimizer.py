# Optimizer for compiler.py
# Author: Jacob Moore

import sys
from my_parser import MyParser
from tokenizer import Tokenizer

def const_prop(ir):

    # Check to see if IR is an assignment statement
    if ir[0] == '=':
       # Assign left and right operations 
        lop = ir[1]
        rop = ir[2]
        # Checks to see if assignment is a constant
        if isinstance(lop, ID) and isinstance(rop, int):
            my_parser.symbol_table[lop] = rop
            return('=', lop, rop)
    return ir    
     

def const_fold(ir):
    
    # Check to see if IR is an assignment.
    if ir[0] == '=':
        # Assign left and right operator
        lop = ir[1]
        rop = ir[2]
        # Checks to see if assignment has an expression
        if isinstance(lop, ID) and isinstance(rop, tuple):
            my_parser.symbol_table[lop] = rop
            return('=', lop, rop)
    return ir
    

def copy_prop(ir):

    # Check to see if IR is an assignment
    if ir[0] == '=':
        # Assign left and right operator
        lop = ir[1]
        rop = ir[2]
        # Check to see if the left and right are variables
        if isinstance(lop, ID) and isinstance(rop, ID):
            my_parser.symbol_table[lop] = rop
            return('=', lop, rop)   
    return ir
    
    
def dead_code_removal(ir):

    # Check to see if IR is an assignment
    if ir[0] == '=':
        # Assign left and right operator
        lop = ir[1]
        rop = ir[2]
        # Check to see if the left and right are variables
        if isinstance(lop, ID) and isinstance(rop, ID):
            my_parser.symbol_table[lop] = rop
            return('=', lop, rop)
    return ir
        
if __name__ == '__main__':

    if len(sys.argv) != 2:
        print("Usage: python3 optimizer.py <input_file>")
        sys.exit(1)

    input_file = sys.argv[1]

    with open(input_file, 'r') as file:
        c_code = file.read()

    tokens = Tokenizer()
    my_parser = MyParser()
    tok_stream = tokens.tokenize(c_code)
    
    ast = my_parser.parse(tok_stream) 
    
    # Intermediate representation brought in from the parser
    ir = my_parser.generate_3_address_code(ast)   

    optimized_ir = ir
    optimized_ir = const_prop(optimized_ir)
    optimized_ir = const_fold(optimized_ir)
    optimized_ir = copy_prop(optimized_ir)
    optimized_ir = dead_code_removal(optimized_ir)

    print("Optimized IR:")
    print(optimized_ir)


    

