# COMP 5210 Compiler Construction project.
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

	token_specs = [
		('ID',       r'[A-Za-z_][A-Za-z0-9_]*'),#Identifiers
        	('NUMBER',   r'\d+\.\d+|\d+'),#Numbers used chatgpt to figure out how to read number tokens
		('EQREL',    r'\=\='),#Added the relational operators
		('NOTEQ',    r'\!='),
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
		('NEGATE',   r'!'),#Logical not
		('INCRMNT',  r'\+\+'),#Increments a value by one
		('DECRMNT',  r'\-\-'),#Decrements a value by one
		('MISMATCH', r'\.'),				
	]

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

#statements = '''
#int main() {
#printf("Hello World");
#return 0;
#}
#'''


for token in tokenize(file_content):
	print(token)
