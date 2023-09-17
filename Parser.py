# https://www.dabeaz.com/ply/ply.html
# https://stackoverflow.com/questions/25712334/ply-lex-and-yacc-issues
# need to fix how the lexer = lex.lex reads in the tokens


import ply.lex as lex
import ply.yacc as yacc
import importlib.util
import sys

# import a file
with open ("test.py", 'r') as file:
	file_content = file.read()

# Call tokenizer used from 
# https://docs.python.org/3/library/importlib.html?highlight=import%20lib#module-importlib.util
file_path = 'C:\Users\Jacob\OneDrive - Auburn University\Comp 5210\Compiler-Construction\Tokenizer.py'
module_name = 'Tokenizer' 

spec = importlib.util.spec_from_file_location(module_name, file_path)
module = importlib.util.module_from_spec(spec)
sys.modules[module_name] = module
spec.loader.exec_module(module)
 
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
   '''Term : Term TIMES Factor
           | Term DIVIDE Factor
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



