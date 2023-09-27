# Parser for COMP 5210 Compiler.py project.
# Author: Ben Hulsey
# Author: Jacob Moore

#https://sly.readthedocs.io/en/latest/sly.html#introduction

# https://docs.python.org/3/library/symtable.html#module-symtable
# for symbol table

from sly import Parser # import SLY
import tokenizer #import tokenizer file

class MyParser(Parser):
    tokens = tokenizer.Tokenizer.tokens

    def __init__(self):
        self.names = {}  # Symbol table

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
        raise SyntaxError(f"Syntax error at token {p.type}")

if __name__ == '__main__':
    data = "1 + 2 * (3 - 4)"
    lexer = tokenizer.Tokenizer()
    parser = MyParser()

    try:
        result = parser.parse(lexer.tokenize(data))
        print(result)
    except SyntaxError as e:
        print(e)
