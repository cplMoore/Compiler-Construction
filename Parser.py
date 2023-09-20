# Parser for COMP 5210 Compiler.py project.
# Author: Ben Hulsey
# Author: Jacob Moore
# https://stackoverflow.com/questions/25712334/ply-lex-and-yacc-issues
# need to fix how the lexer = lex.lex reads in the tokens

from sly import Parser
import Tokenizer

 
# Error handling for unknown characters
def ERROR(token):
   print(f"Unknown character: {token.value[0]}")
   token.lexer.skip(1)

# Build the lexer
lexer = lex.lex()# This needs to pass some kind of parameter

# Grammar rules
def Expr(p):
   '''Expr : Term PLUS Expr
           | Minus MINUS Expr
           | Term'''
   if len(p) == 2:
      p[0] = p[1]
   else:
      p[0] = (p[2], p[1], p[3])

def Term(p):
   '''Term : Factor TIMES Term
           | Factor DIVIDE Term
           | Factor'''
   if len(p) == 2:
      p[0] = p[1]
   else:
      p[0] = (p[2], p[1], p[3])

def Factor(p):
   '''Factor : LPAREN Expr RPAREN
             | NUM
             | ID'''
   if len(p) == 4:
      p[0] = p[2]
   else:
      p[0] = p[1]

# Error handling for syntax errors
def Error(p):
   print(f"Syntax error at token {p.type}")

# Build the parser
parser = yacc.yacc()

#Creates output
result = parser.parse(file_content)
print(result)



