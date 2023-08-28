# COMP 5210 Compiler Construction project.
# Author: Jacob Moore jwm0083.
# Author: Ben Hulsey bph0022.

from typing import NamedTuple
import re

# Recognize tokens print out tokens and put them in a tokenizer.py file.
# Class and tokenize method was used from https://docs.python.org/3/library/re.html?highlight=regular%20expression.
class Token(NamedTuple):
    type: str
    value: str
    line: int
    column: int

def tokenize(code):
	# Keywords taken from https://docs.python.org/3/library/re.html?highlight=regular%20expression.
	# Taken up to ISO C99.
	keywords = {'AUTO', 'BREAK', 'CASE', 'CHAR' 'CONST', 'CONTINUE', 'DEFAULT', 'DO', 'DOUBLE', 'ELSE',
			'ENUM', 'EXTERN', 'FLOAT', 'FOR', 'GOTO', 'IF', 'INT', 'LONG', 'REGISTER', 'RETURN', 
			'SHORT', 'SIGNED', 'SIZEOF', 'STATIC', 'STRUCT', 'SWITCH', 'TYPEDEF', 'UNION', 
			'UNSIGNED', 'VOID', 'VOLATILE', 'WHILE', 'INLINE', '_BOOL', '_COMPLEX', _IMAGINARY'}

	token_specs = [
	('ID'		r'[A-Za-z_][A-Za-z0-9_]+'),	#Identifiers
        ("Number'       r'[0-9}+.[0-9]+),		#Numbers
	('END'		r';'),				#Statement end
	('NEWLINE' 	r'\n'),				#Moves to a new line
	('TAB'		r'\t'),				#Tabs over right
	('ASSIGN'	r'='),				#Used to assign values to variables
	
	
	]
