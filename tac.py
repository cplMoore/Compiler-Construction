# Produces three address code for COMP 5210 compiler construction project.
# Author: Jacob Moore
# Author: Ben Hulsey

# https://stackoverflow.com/questions/62983856/in-lr-parsing-is-it-possible-to-construct-a-non-binary-ast
# Used stackoverflow to walk through AST uses with SLY to get a AST and TAC built
import my_parser
 
class TAC():

    def __init__(self):
        self.code = []
        self.t_var = 0
        
    def generate_3_address_code(self, op, arg1, args2, result):  
        code_line = (op, arg1, args2, result)
        self.code.append(code_line)

    def new_temp(self):
        temp = f"{self.t_var}"
        self.t_var += 1
        return temp

    def display_code(self):
        for line in self.code:
            print(line)
            
    def process_expr(self, expr):
        tokens