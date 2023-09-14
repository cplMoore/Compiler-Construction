# https://www.dabeaz.com/ply/ply.html
https://stackoverflow.com/questions/25712334/ply-lex-and-yacc-issues
# need to fix how the lexer = lex.lex reads in the tokens


import ply.lex as lex
import ply.yacc as yacc

# import a file
with open ("test.py", 'r') as file:
	file_content = file.read()


# Token definitions
tokens = [
		('ID',       r'[A-Za-z_][A-Za-z0-9_]+'),#Identifiers
    ('NUMBER',   r'\d+\.\d+|\d+'),#Numbers used chatgpt to figure out how to read number tokens
		('EQREL',    r'=='),#Added the relational operators
		('NOTEQ',    r'!='),
		('GRT',      r'<'),
		('LES',      r'>'),
		('GRTEQ',    r'<\='),
		('LESEQ',    r'>\='),
		('END',      r';'),#Statement end
		('NEWLINE',  r'\n'),#Moves to a new line
		('TAB',      r'\t'),#Tabs over right
		('ASSIGN',   r'\='),#Used to assign values to variables
		('OP',       r'\+-\*/'),#Math operators(not sure if I can list like that)
		('LPAREN',   r'\('),
		('RPAREN',   r'\)'),
		('LCB',      r'\{'),
		('RCB',      r'\}'),
		('LOGICAND', r'\&\&'),#Logical and
		('LOGICOR',  r'\|\|'),#Logical or
		('NEGATE',   r'\!'),#Logical not
		('INCRMNT',  r'\+\+'),#Increments a value by one
		('DECRMNT',  r'\-\-'),#Decrements a value by one
		('MISMATCH', r'\.'),				
	]

# Error handling for unknown characters
def ERROR(token):
   print(f"Unknown character: {token.value[0]}")
   token.lexer.skip(1)

# Build the lexer
lexer = lex.lex()

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



