# Parser for COMP 5210 compiler.py project.
# Author: Ben Hulsey
# Author: Jacob Moore

#https://sly.readthedocs.io/en/latest/sly.html#introduction

# https://docs.python.org/3/library/symtable.html#module-symtable
# for symbol table

from sly import Parser
from tokenizer import Tokenizer
import sys
    


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
        self.symbol_table = { }
        
        
    # Grammar rules and actions
    
    @_('INT ID LPAREN RPAREN LCB stmt RCB')
    def program(self, p):
        print(f"Function definition: {p.INT} {p.ID}")
        
    @_('INT ID ASSIGN NUM SEMI')
    def stmt(self, p):
        print("Variable assignment: {p.ID} {p.NUM}")
    
    
    @_('RETURN NUM SEMI',
       'RETURN ID SEMI')
    def stmt(self, p):
        print(f"Return statement: {p.NUM}")
        
    
    @_('expr')
    def stmt(self, p):
        print(p.expr)    
        

    @_('expr "+" term',
       'expr "-" term')
    def expr(self, p):
        return (p[1], p.expr, p.term)

    @_('term')
    def expr(self, p):
        return p.term

    @_('term "*" factor',
       'term "/" factor')
    def term(self, p):
        return (p[1], p.term, p.factor)

    @_('factor')
    def term(self, p):
        return p.factor

    @_('NUM')
    def factor(self, p):
        return p.NUM

    @_('LPAREN expr RPAREN')
    def factor(self, p):
        return p.expr
        
    @_('ID')
    def factor(self, p):
        try:
            return self.symbol_table[p.ID]
        except LookupError:
            print(f'Undefined name {p.names!r}')
            return 0


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
         
       
    print(result)
        

