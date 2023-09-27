# Parser for COMP 5210 Compiler.py project.
# Author: Ben Hulsey
# Author: Jacob Moore

#https://sly.readthedocs.io/en/latest/sly.html#introduction

# https://docs.python.org/3/library/symtable.html#module-symtable
# for symbol table

from sly import Lexer, Parser
from tokenizer import Tokenizer

# Error handling for unknown characters
def ERROR(token):
   print(f"Unknown character: {token.value[0]}")
   token.lexer.skip(1)

# Define the lexer
lexer = Tokenizer()

# Grammar rules
class MyParser(Parser):
    tokens = lexer.tokens

    # Define the precedence and associativity of operators
    precedence = (
        ('left', 'PLUS', 'MINUS'),
        ('left', 'TIMES', 'DIVIDE'),
    )

    @_('Expr PLUS Term', 'Expr MINUS Term', 'Term')
    def Expr(self, p):
        if len(p) == 1:
            p[0] = p[1]
        else:
            if p[2] == '+':
                p[0] = p[1] + p[3]
            elif p[2] == '-':
                p[0] = p[1] - p[3]

    @_('Term TIMES Factor', 'Term DIVIDE Factor', 'Factor')
    def Term(self, p):
        if len(p) == 1:
            p[0] = p[1]
        else:
            if p[2] == '*':
                p[0] = p[1] * p[3]
            elif p[2] == '/':
                p[0] = p[1] / p[3]

    @_('LPAREN Expr RPAREN', 'NUM', 'ID')
    def Factor(self, p):
        if len(p) == 4 and p[1] == '(' and p[2] == ')' and p[3] is None:
            raise SyntaxError("Syntax error: Empty parentheses")
        elif len(p) == 2:
            p[0] = p[1]

    def error(self, p):
        raise SyntaxError(f"Syntax error at token {p.type}")

# Build the parser
parsers = MyParser()

# Creates output
data = "1 + 2 * (3 - 4)"
lexer = Tokenizer()
tokens = []
for tok in lexer.tokenize(data):
    tokens.append((tok.type, tok.value))
    print(tok)



