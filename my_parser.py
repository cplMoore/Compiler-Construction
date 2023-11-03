# Parser for COMP 5210 compiler.py project.
# Author: Ben Hulsey
# Author: Jacob Moore

#https://sly.readthedocs.io/en/latest/sly.html#introduction

# https://stackoverflow.com/questions/62983856/in-lr-parsing-is-it-possible-to-construct-a-non-binary-ast
# Used stackoverflow to walk through AST uses with SLY to get a AST and TAC built

# https://docs.python.org/3/library/symtable.html#module-symtable
# for symbol table

from sly import Parser
from tokenizer import Tokenizer
import sys
import pprint




class MyParser(Parser):


     # Debugging help from SLY
    debugfile = 'parser.out'
    
    # Brings in the token list.
    tokens = Tokenizer.tokens
    
    # Keeps order of operations.
    # + and - have the same precedence.
    # * and / have the same precedence, 
    # but have a higher level of precedence than + or - since they come later in the list per SLY.
    precedence = (
        ('left', "+", "-"),
        ('left', "*", "/"),
    )

    def __init__(self):
        super().__init__()
        self.symbol_table = {}
        self.ast = None
        self.three_address_code = []
        self.basic_blocks = []

    def error(self, t):
        print(f"Syntax error at line {t.lineno}, position {t.index}: Unexpected token '{t.value}'")
        sys.exit(1)

    # Grammar rules and actions
    # The last match action is the first grammar rule.
    # i.e. stmt -> expr | INT ID ASSIGN NUM SEMI.
    @_('INT MAIN LPAREN RPAREN LCB stmt_list return_stmt RCB')
    def program(self, p):
        self.ast = ('Function Definition',p.MAIN, p.stmt_list, p.return_stmt)
        return self.ast
         
    @_('expr')
    def program(self, p):
        return p.expr

       
    @_('stmt stmt_list')
    def stmt_list(self, p):
        return [p.stmt] + p.stmt_list
        
    @_('stmt')
    def stmt_list(self, p):
        return [p.stmt]

    @_('INT ID ASSIGN expr SEMI')
    def stmt(self, p):
        variable_name = p.ID
        value = p.expr
        self.symbol_table[variable_name] = value
        self.ast = ('=', variable_name, value)
        return self.ast
        
    @_('LPAREN expr RPAREN')
    def stmt(self, p):
        return p.expr

    @_('RETURN factor SEMI')
    def return_stmt(self, p):
        self.ast = ('return', p.factor)
        return self.ast

    @_('factor "+" expr',
       'factor "-" expr',
       'factor "*" expr', 
       'factor "/" expr')
    def expr(self, p):
        self.ast = (p[1], p.factor, p.expr)
        return self.ast

    @_('factor')
    def expr(self, p):
        return p.factor

    @_('NUM')
    def factor(self, p):
        return p.NUM
        
    @_('ID')
    def factor(self, p):
        try:
            value = self.symbol_table[p.ID]
            self.ast = (value)
            return self.ast
        except LookupError:
            print(f'Undefined name {p.ID!r}')
            sys.exit(1)

    def generate_3_address_code(self, ast):  
        ir = []
                    
        if ast: 
            if isinstance(ast, tuple):
                if ast[0] in ['Function Definition', 'Variable Assignment', 'Return Statement']:
                    ir.append((ast[1], ':', ast[2]))
                    ir.extend(self.generate_3_address_code(ast[2]))
                else:
                    ir.append((ast[1], '=', ast[2]))
                    ir.extend(self.generate_3_address_code(ast[1]))
                    ir.extend(self.generate_3_address_code(ast[2]))
            elif isinstance(ast, int):
                ir.append(ast)

        return ir
        print(ast)
#
#    def is_jump_instruction(self, instruction):
#        return instruction[0] in ("IF", "GOTO")
#
#    def get_jump_target(self, instruction):
#        if instruction[0] == "IF":
#            return instruction[2]
#        elif instruction[0] == "GOTO":
#            return instruction[1]
#        return None                
#     
#    # Had ChatGPT help me (JM) create basic blocks for the 3 address code.           
#    def generate_basic_blocks(self, instructions):
#         leaders = set()
#         leader = 0
#         leaders.add(leader)
#         
#         for i, _ in enumerate(instructions):
#            if i < len(instructions) - 1 and self.is_jump_instruction(instructions[i]):
#                target = self.get_jump_target(instructions[i])
#                leaders.add(target)
#         if i + 1 < len(instructions):
#            leaders.add(i + 1)
#         
#         # Ensure the last instruction is also a leader
#         if not self.is_jump_instruction(instructions[-1]):
#            leaders.add(len(instructions))
#
#         basic_blocks = []
#
#         for i in range(len(leaders) - 1):
#            start = leaders[i]
#            end = leaders[i + 1]
#            basic_block = instructions[start:end]
#            basic_blocks.append(basic_block)
#
#         return basic_blocks        
#    
if __name__ == '__main__':

    if len(sys.argv) != 2:
        print("Usage: python3 my_parser.py <input_file>")
        sys.exit(1)

    input_file = sys.argv[1]

    with open(input_file, 'r') as file:
        c_code = file.read()

    lexer = Tokenizer()
    my_parser = MyParser()
    
    
    result = my_parser.parse(lexer.tokenize(c_code))

    if my_parser.ast:
        print("Abstract Syntax Tree:")
        pprint.pprint(my_parser.ast, indent=4)
        
        print("\nSymbol Table:")
        for variable, value in my_parser.symbol_table.items():
            print(f"{variable} = {value}")
            
        print("\n3-Address Code:")
        my_parser.generate_3_address_code(my_parser.ast)
        
#    tac_instructions = [
#        ("=", "x", 1),
#        ("+", "y", "x", 2),
#        ("IF", "y", "L2"),
#        ("=", "z", 3),
#        ("GOTO", "L1"),
#        ("LABEL", "L2"),
#        ("=", "z", 4),
#        ("LABEL", "L1"),
#        ("return", "z")
#    ]
#
#    for instruction in tac_instructions:
#        if my_parser.is_jump_instruction(tac_instructions):
#            target = my_parser.get_jump_target(tac_instructions)
#            print(f"Jump instruction: {instruction[0]} Target: {target}")
#            
#    basic_blocks = my_parser.generate_basic_blocks(tac_instructions)
#    for i, block in enumerate(basic_blocks):
#        print(f"Basic Block {i}: {block}")
