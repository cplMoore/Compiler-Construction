# COMP 5210 Tokenizer for Compiler Construction project.
# Author: Jacob Moore jwm0083.
# Author: Ben Hulsey bph0022.

from typing import NamedTuple
import re

# import a file
with open ("test.py") as file:

	file_content = file.read()

# Recognize tokens print out tokens and put them in a tokenizer.py file.
# Class and tokenize method was used from https://docs.python.org/3/library/re.html?highlight=regular%20expression.
class Token(NamedTuple):
    type: str
    value: str
    line: int
    column: int

def tokenize(code):
	# Keywords taken from C documentation.
	# Taken up to ISO C99.
	keywords = {'auto', 'break', 'case', 'char' 'const', 'continue', 'default', 'do', 'double', 'else',
				'enum', 'extern', 'float', 'for', 'goto', 'if', 'int', 'long', 'register', 'return', 
				'short', 'signed', 'sizeof', 'static', 'struct', 'switch', 'typedef', 'union', 
				'unsigned', 'void', 'volatile', 'while', 'inline', '_bool', '_complex' '_imaginary'}

	# Some Tokens found and used from https://www.scaler.com/topics/c/tokens-in-c/
	tokens = ('ID', 'NUMBER', 'EQREL', 'NOTEQ', 'GRT', 'LES', 'GRTEQ', 'LESEQ', 'END', 'NEWLINE',
		      'TAB', 'ASSIGN', 'OP', 'LPAREN', 'RPAREN', 'LCB', 'RCB', 'LOGICAND', 'LOGICOR',
              'NEGATE', 'INCRMNT', 'DECRMNT', 'MISMATCH')

#Regular expressions rules for simple tokens.
# Token definitions
t_ID = r'[A-Za-z_][A-Za-z0-9_]+'#Identifiers
t_NUMBER = r'\d+\.\d+|\d+'#Numbers used chatgpt to figure out how to read number tokens
t_EQREL = r'=='#Added the relational operators
t_NOTEQ = r'!='
t_GRT = r'<'
t_LES = r'>'
t_GRTEQ = r'<\='
t_LESEQ = r'>\='
t_END = r';'#Statement end
t_NEWLINE = r'\n'#Moves to a new line
t_TAB = r'\t'#Tabs over right
t_ASSIGN = r'\='#Used to assign values to variables
t_OP = r'\+-\*/'#Math operators(not sure if I can list like that)
t_LPAREN = r'\('
t_RPAREN = r'\)'
t_LCB = r'\{'
t_RCB = r'\}'
t_LOGICAND = r'\&\&'#Logical and
t_LOGICOR = r'\|\|'#Logical or
t_NEGATE = r'\!'#Logical not
t_INCRMNT = r'\+\+'#Increments a value by one
t_DECRMNT = r'\-\-'#Decrements a value by one
t_MISMATCH = r'\.'				


#number tokens chatgpt message: "how to write a token that reads all numbers in python"
#Token recognizer was taken from https://docs.python.org/3/library/re.html?highlight=re#writing-a-tokenizer
tok_regex = '|'.join('(?P<%s>%s)' % pair for pair in token_specs)
line_num = 1
line_start = 0
for mo in re.finditer(tok_regex, code):
	kind = mo.lastgroup
	value = mo.group()
	column = mo.start() - line_start
	if kind == 'NUMBER':
		value = float(value) if '.' in value else int(value)
	elif kind == 'ID' and value in keywords:
		kind = value
	elif kind == 'NEWLINE':
		line_start = mo.end()
		line_num += 1
		continue
	elif kind == 'TAB':
		continue
		
	elif kind == 'MISMATCH':
		raise RuntimeError(f'{value!r} unexpected on line {line_num}')
	
yield Token(kind, value, line_num, column)


with open("tokens.txt", 'a') as tokens:
	tokens.write(str(Token))