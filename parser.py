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


class Expr:
    pass
    
class binOp(Expr):
    def __init__(self, op, left, right):
        self.op = op
        self.left = left
        self.right = right
        
        
class num(Expr):
    def __init__(self, value):
        self.value = value

class MyParser(Parser):

    # Debugging help from SLY
    debugfile = 'parser.out'

    # Brings in the token list.
    tokens = Tokenizer.tokens
    
    # Sets the Precedence for mathematical operations.
    # PLUS/MINUS have the same precedence and are  left-associative.
    # TIMES/DIVIDE have higher precedence since they apprear later in the list.
    precedence = (
        ('left', "+", "-"),
        ('left', "*", "/"),
    )
    
    # Starts the parsing at Expr not Empty.
    start = 'expr'

#    def __init__(self):
#        self.names = {}  # Symbol table to store variable names and their values
#
#    @_('Expr')
#    def Expr(self, p):
#        pass

    # This will act as an epsilon for escaping.
    @_('')
    def empty(self, p):
        pass
        
        
    # Parsing starts here        
    @_('value "+" expr',
       'value "-" expr',
       'value "*" expr',
       'value "/" expr')
    def expr(self, p):
        line = p.lineno
        index = p.index
        return binOp(p[1], p.value, p.expr, line, index)


#    # This is a way to handle negative numbers.
#    @_('"-" Expr %prec UMINUS')
#    def expr(p):
#        return  -p.expr
    
    # Expr escape.
    @_('empty')
    def expr(self, p):
        pass

    
    @_('factor "*" value',
       'factor "/" value',
       'factor "+" value',
       'factor "-" value')
    def value(self, p):
        line = p.lineno
        index = p.index
        return binOp(p[1], p.factor, p.value, line, index)

    @_('NUM')
    def value(self, p):
        return int(p.NUM)
        
        
    # value escape
    @_('empty')
    def value(self, p):
        pass
#
#    @_("(" 'expr' ")")
#    def factor(self, p):
#        return p.factor
     

    @_('ID')
    def factor(self, p):
        return p.factor

#    def error(self, p):
#        print("Syntax Error at token", p.type)
#        if not p:
#            print("End of File!")
#            return
#
#
#
#        # Read ahead looking for a closing '}'
#        while True:
#            tokens = next(self.tokens, None)
#            if not tokens or tokens.type == '}':
#                break
#        self.restart()
#
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
        

