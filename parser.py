# Parser for COMP 5210 compiler.py project.
# Author: Ben Hulsey
# Author: Jacob Moore

#https://sly.readthedocs.io/en/latest/sly.html#introduction

# https://docs.python.org/3/library/symtable.html#module-symtable
# for symbol table

from sly import Parser
from tokenizer import Tokenizer
import sys
import ast
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
        ('left', "*", "/")
    
    )
    
    def __init__(self):        
        super().__init__()
        self.symbol_table = {}
        self.ast = None
        self.three_address_code = []

    def error(self, t):
        print(f"Syntax error at line {t.lineno}, position {t.index}: Unexpected token '{t.value}'")
        sys.exit(1)
        
    # Grammar rules and actions
    # The last match action for a non-terminal token is the first rule assigned.
    
    @_('INT ID LPAREN RPAREN LCB stmt return_stmt RCB')
    def program(self, p):
        self.ast = ('Function Definition', p.ID, p.stmt)
        return self.ast
        
    @_('INT ID ASSIGN NUM SEMI')
    def stmt(self, p):
        self.ast = ('Variable Assignment', p.ID, p.NUM)
        return self.ast
      
    @_('expr')
    def stmt(self, p):
        return p.expr
        
    @_('RETURN NUM SEMI',
       'RETURN ID SEMI')
    def return_stmt(self, p):
        self.ast = ('Return Statement', p.NUM)
        return self.ast

        
    @_('factor "-" expr',
       'factor "+" expr',
       'factor "/" expr',
       'factor "*" expr')
    def expr(self, p):
        self.ast = (p[1], p.factor, p.expr)
        return self.ast

    @_('factor')
    def expr(self, p):
        return p.factor

    @_('ID')
    def factor(self, p):
        try:
            return self.symbol_table[p.ID]
            value = self.symbol_table[p.ID]
            self.ast = ('Variable', p.ID)
            return self.ast
        except LookupError:
            print(f'Undefined name {p.names!r}')
            print(f'Undefined name {p.ID!r}')
            return 0
    
    @_('NUM')
    def factor(self, p):
        return p.NUM

    @_('LPAREN expr RPAREN')
    def factor(self, p):
        return p.expr
        

if __name__ == '__main__':

    # Checks if a c file is provided.
    if len(sys.argv) != 2:
        print("Usage: python3 parser.py <input_file>")
        sys.exit(1)
        
    # Takes the c file passed with compiler.py    
    input_file = sys.argv[1]
    
    # Open and read c file
    with open(input_file, 'r') as file:
        c_code = file.read()
        
    lexer = Tokenizer()
    parser = MyParser()
    result = parser.parse(lexer.tokenize(c_code))
         
    if parser.ast:
        print("Abstract Syntax Tree:")
        print(parser.ast)
        
        
    def generate_3_address_code(ast):
        if ast:
            if isinstance(ast, tuple):
                if ast[0] in ['Function Definition', 'Variable Assignment', 'Return Statement']:
                    print(ast[0], ast[1])
                    generate_3_address_code(ast[2])
                else:
                    print(ast[0], ast[1], ast[2], ast[3])
                    generate_3_address_code(ast[1])
                    generate_3_address_code(ast[2])
            elif isinstance(ast, int):
                print(ast)

    if parser.ast:
        print("3-Address Code:")
        generate_3_address_code(parser.ast)
