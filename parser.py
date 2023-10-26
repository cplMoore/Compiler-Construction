# Parser for COMP 5210 compiler.py project.
# Author: Ben Hulsey
# Author: Jacob Moore

#https://sly.readthedocs.io/en/latest/sly.html#introduction

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
        ('left', "*", "/")
    
    )
    
    def __init__(self):
        self.symbol_table = { }
        
        
    # Grammar rules and actions
    # The last match action for a non-terminal token is the first rule assigned.
    
    @_('INT ID LPAREN RPAREN LCB stmt return_stmt RCB')
    def program(self, p):
        return p.program
    
    @_('expr')
    def stmt(self, p):
        return p.stmt  
    
    @_('INT factor ASSIGN NUM SEMI')
    def stmt(self, p):
        return p.stmt
    
    @_('RETURN factor SEMI')
    def return_stmt(self, p):
        return p.return_stmt
        
    @_('factor "-" expr',
       'factor "+" expr',
       'factor "/" expr',
       'factor "*" expr')
    def expr(self, p):
        return (p[1], p.expr, p.factor)

    @_('factor')
    def expr(self, p):
        return p.factor

    @_('ID')
    def factor(self, p):
        try:
            return self.symbol_table[p.ID]
        except LookupError:
            print(f'Undefined name {p.names!r}')
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
 #   if # TODO have an if stmt to check for the -t flag
    parser = MyParser()
    
    
    result = parser.parse(lexer.tokenize(c_code))
         
# A list inside of a list can be a way to keep track of a tree.       
    pprint.pprint(result, width=30)
        

