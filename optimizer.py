# Optimizer for compiler.py
# Author: Jacob Moore

import sys
from my_parser import MyParser

my_parser= MyParser()

if len(sys.argv) != 2:
    print("Usage: python3 optimizer.py <input_file>")
    sys.exit(1)

input_file = sys.argv[1]

with open(input_file, 'r') as file:
    c_code = file.read()

ast = my_parser.parse(c_code)

# Intermediate representation brought in from the parser
ir = my_parser.generate_3_address_code(ast)

def const_prop(ir):

    # Check to see if IR is an assignment statement
    if ir[0] == '=':
        lop = ir[1]
        rop = ir[2]
        if isinstance(rop, int):
            my_parser.symbol_table[lop] = rop
            return('=', lop, rop)
    return ir    
     

def const_fold(ir):
    
    # Check to see if IR is an assignment.
    if ir[0] == '=':
        lop = ir[1]
        rop = ir[2]
        if isinstance(rop, tuple):
            my_parser.symbol_table[lop] = rop
            return('=', lop, rop)
    return ir
    

#def copy_prop(ir):
#
#
#def dead_code_removal(ir):

optimized_ir = ir
optimized_ir = const_prop(optimized_ir)
optimized_ir = const_fold(optimized_ir)

print("Optimized IR:")
print(optimized_ir)


    

