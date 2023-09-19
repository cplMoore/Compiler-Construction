# COMP 5210 Tokenizer for Compiler Construction project.
# Author: Jacob Moore jwm0083.


import ply.lex as lex



# Keywords taken from C documentation.
# Taken up to ISO C99.
keywords = {'auto', 'break', 'case', 'char' 'const', 'continue', 'default', 'do', 'double', 'else',
		    'enum', 'extern', 'float', 'for', 'goto', 'if', 'int', 'long', 'register', 'return', 
		    'short', 'signed', 'sizeof', 'static', 'struct', 'switch', 'typedef', 'union', 
		    'unsigned', 'void', 'volatile', 'while', 'inline', '_Bool', '_Complex' '_Imaginary'}
                
# Some Tokens found and used from https://www.scaler.com/topics/c/tokens-in-c/
tokens = ('ID', 'NUMBER', 'EQREL', 'NOTEQ', 'GRT', 'LES', 'GRTEQ', 'LESEQ', 'END', 'NEWLINE',
		  'ASSIGN', 'OP', 'LPAREN', 'RPAREN', 'LCB', 'RCB', 'LOGICAND', 'LOGICOR', 'NEGATE', 
          'INCRMNT', 'DECRMNT', 'COMMENT',  'ERROR')

# Regular expressions rules for simple tokens.
# Token definitions
# Got help from Chat GPT on polishing the definitions up.

def t_ID(t):
    r'[A-Za-z_][A-Za-z0-9_]+'
    t.type = t.value.upper()
    return t


def t_NUMBER(t):
    r'\d+\.\d+|\d+'
    t.value = int(t.value)
    return t


def t_EQREL(t):
    r'=='
    return t


def t_NOTEQ(t):
    r'!='
    return t


def t_GRT(t):
    r'<'
    return t


def t_LES(t):
    r'>'
    return t


def t_GRTEQ(t): 
    r'<\='
    return t


def t_LESEQ(t): 
    r'>\='
    return t


def t_END(t):
    r';'
    return t


def t_NEWLINE(t):
    r'\n+'
    t.lexer.lineno += len(t.value)


def t_ASSIGN(t):
    r'\='
    return t


def t_OP(t):
    r'[+\-*/]'
    return t


def t_LPAREN(t):
    r'\('
    return t


def t_RPAREN(t):
    r'\)'
    return t


def t_LCB(t):
    r'\{'
    return t


def t_RCB(t):
    r'\}'
    return t


def t_LOGICAND(t):
    r'\&\&'
    return t


def t_LOGICOR(t):
    r'\|\|'
    return t


def t_NEGATE(t):
    r'\!'
    return t


def t_INCRMNT(t):
    r'\+\+'
    return t


def t_DECRMNT(t):
    r'\-\-'
    return t

# A string containing spaces and tabs.
t_ignore = '\t'

def t_COMMENT(t):
    r'//.*|\*/'
    pass

def t_ERROR(t):
    r'\.'
    with open("tokens.txt", 'a') as token_file:
        token_file.write(f"Unknown character: {t.value}\n")
    t.lexer.skip(1)

# Create lexer
lexer = lex.lex()

with open("test.c", 'r') as input_file:
    input_code = input_file.read()

lexer.input(input_code)

# Write the tokens to a text file
with open("tokens.txt", 'w') as token_file:
    for token in lexer:
        token_file.write(f"Token: {token.type}, Value: {token.value}\n")
