# Parser for COMP 5210 compiler.py project.
# Author: Ben Hulsey
# Author: Jacob Moore

#https://sly.readthedocs.io/en/latest/sly.html#introduction

# https://docs.python.org/3/library/symtable.html#module-symtable
# for symbol table

from sly import Parser
from tokenizer import Tokenizer
import sys
from pprint import pprint
import ast


class MyParser(Parser):

    # Debugging help from SLY
    debugfile = 'parser.out'

    # Brings in the token list.
    tokens = Tokenizer.tokens
    
    # Sets the Precedence for mathematical operations.
    # PLUS/MINUS have  the same precedence and are  left-associative.
    # TIMES/DIVIDE have higher precedence since they apprear later in the list.
    precedence = (
        ('left', "+", "-"),
        ('left', "*", "/"),
        ('right', UMINUS)
    )
    
    # Starts the parsing at Expr not Empty.
    start = 'Expr'

#    def __init__(self):
#        self.names = {}  # Symbol table to store variable names and their values
#
#    @_('Expr')
#    def Expr(self, p):
#        pass

    # This will act as an epsilon for escaping.
    @_('')
    def Empty(self, p):
        pass
        
        
    # Parsing starts here        
    @_('Expr "+" Term',
       'Expr "-" Term'
       'Expr "*" Term'
       'Expr "/" Term')
    def Expr(self, p):
        line = p.lineno
        index = p.index
        return (p[1], p.Expr, p.Term, line, index)


    # This is a way to handle negative numbers.
    @_('"-" Expr %prec UMINUS')
    def Expr(p):
        return  -p.Expr
    
    # Expr escape.
    @_('Empty')
    def Expr(self, p):
        pass

    
    @_('Term "*" Factor',
       'Term "/" Factor'
       'Term "+" Factor'
       'Term "-" Factor')
    def Term(self, p):
        line = p.lineno
        index = p.index
        return (p[1], p.Term, p.Factor, line, index)

    # Term escape
    @_('Empty')
    def Term(self, p):
        pass

    @_("(" 'Expr' ")")
    def Factor(self, p):
        return ('group-expression', p.Expr)

    @_('NUM')
    def Factor(self, p):
        return int(p.NUM)
        


#    @_('ID')
#    def Factor(self, p):
#        pass

    def error(self, p):
        print("Syntax Error at token", p.type)
        if not p:
            print("End of File!")
            return



#        # Read ahead looking for a closing '}'
#        while True:
#            tokens = next(self.tokens, None)
#            if not tokens or tokens.type == '}':
#                break
#        self.restart()

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
    
    while True:
        try:
            result = parser.parse(lexer.tokenize(c_code))
        
            print(ast.dump(ast.parse(result), indent=4))
        
        
        
        except SyntaxError as e:
        print(e)
