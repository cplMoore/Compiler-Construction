# Parser for COMP 5210 compiler.py project.
# Author: Ben Hulsey
# Author: Jacob Moore

#https://sly.readthedocs.io/en/latest/sly.html#introduction

# https://docs.python.org/3/library/symtable.html#module-symtable
# for symbol table

from sly import Parser
from tokenizer import Tokenizer

file_path = "tokenizer.py" #read in a file 
with open(file_path, "r") as file:
        file_contents = file.read()

class MyParser(Parser):
    tokens = Tokenizer.tokens

    def __init__(self):
        self.names = {}  # Symbol table to store variable names and their values

    @_('Expr')
    def statement(self, p):
        return p.Expr

    @_('Expr PLUS Term')
    def Expr(self, p):
        return ('+', p.Expr, p.Term)

    @_('Expr MINUS Term')
    def Expr(self, p):
        return ('-', p.Expr, p.Term)

    @_('Term')
    def Expr(self, p):
        return p.Term

    @_('Term TIMES Factor')
    def Term(self, p):
        return ('*', p.Term, p.Factor)

    @_('Term DIVIDE Factor')
    def Term(self, p):
        return ('/', p.Term, p.Factor)

    @_('Factor')
    def Term(self, p):
        return p.Factor

    @_('LPAREN Expr RPAREN')
    def Factor(self, p):
        return p.Expr

    @_('NUM')
    def Factor(self, p):
        return int(p.NUM)

    @_('ID')
    def Factor(self, p):
        return p.ID


    def error(self, p):
        print("Syntax Error at token", p.type)
        if not p:
            print("End of File!")
            return

        # Read ahead looking for a closing '}'
        while True:
            tok = next(self.tokens, None)
            if not tok or tok.type == 'RBRACE':
                break
        self.restart()

if __name__ == '__main__':
    data = file_contents
    file_contents 
    lexer = Tokenizer()
    parser = MyParser()

    try:
        result = parser.parse(lexer.tokenize(data))
        print(result)
    except SyntaxError as e:
        print(e)
